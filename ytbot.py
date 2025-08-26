import streamlit as st
from langchain_nvidia_ai_endpoints import ChatNVIDIA, NVIDIAEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from youtube_transcript_api._errors import NoTranscriptFound, CouldNotRetrieveTranscript
from gtts import gTTS
import speech_recognition as sr
import os, re, uuid
from dotenv import load_dotenv

# --- Streamlit Config ---
st.set_page_config(page_title="🎥 YouTube Chatbot", layout="wide")

# --- Session State Initialization ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "user_query_main" not in st.session_state:
    st.session_state["user_query_main"] = ""

# --- Sidebar Settings ---
with st.sidebar:
    st.title("⚙️ Configuration")
    theme = st.radio("Theme", ["Light", "Dark"], index=1)
    output_lang = st.selectbox(
        "🌐 Output Language",
        ["English", "Hindi", "Bengali", "Tamil", "Telugu", "Marathi", "Gujarati"]
    )
    model_name = st.selectbox("🧠 NVIDIA Model", [
        "mistralai/mixtral-8x7b-instruct-v0.1",
        "meta/llama3-8b-instruct"
    ])
    temp = st.slider("🔥 Creativity (temperature)", 0.0, 1.0, 0.2, 0.1)

# --- Optional Dark Theme CSS ---
if theme == "Dark":
    st.markdown("""
        <style>
            .stApp { background-color: #0E1117; color: white; }
        </style>
    """, unsafe_allow_html=True)

# --- Welcome Message ---
st.markdown("<h1 style='text-align: center;'>🤖 Welcome to YouTube Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;color: red;'>Paste a YouTube link, ask your question, or speak it aloud!</p>", unsafe_allow_html=True)

# --- YouTube Video Input ---
st.markdown("### 🔗 YouTube Video Link")
video_url = st.text_input("Paste YouTube URL here", key="video_url_main")

# --- Handle Voice Input BEFORE Drawing Textbox ---
st.markdown("### 🎙️ Ask your question")
mic_pressed = False
col1, col2 = st.columns([4, 1])
with col2:
    mic_pressed = st.button("🎤 Speak")

if mic_pressed:
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        st.info("🎙️ Listening...")
        audio = recognizer.listen(source)
    try:
        spoken_text = recognizer.recognize_google(audio)
        st.success(f"🗣️ You said: {spoken_text}")
        st.session_state["user_query_main"] = spoken_text
        st.rerun()
    except Exception as e:
        st.error(f"❌ Could not recognize speech: {e}")

# --- Question Input Box AFTER Mic Logic ---
with col1:
    user_query = st.text_input("Type your question here", key="user_query_main")

# --- Run Chatbot Button ---
run_btn = st.button("🚀 Run Chatbot")

load_dotenv()
api_key = os.getenv("NVIDIA_API_KEY")
if not api_key:
    st.error("❌ NVIDIA_API_KEY not found in .env")
    st.stop()
os.environ["NVIDIA_API_KEY"] = api_key  # ✅ Needed for NVIDIA SDK


# --- Extract Video ID ---
def extract_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    return match.group(1) if match else None

# --- Main Logic ---
if run_btn:
    if not video_url or not user_query:
        st.warning("Please provide both YouTube URL and your question.")
    else:
        video_id = extract_video_id(video_url)
        if not video_id:
            st.error("❌ Invalid YouTube URL")
        else:
            try:
                st.info("⏳ Fetching transcript...")
                transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
                transcript = " ".join([d["text"] for d in transcript_list])

                # Chunking
                splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
                chunks = splitter.create_documents([transcript])

                # Embedding + Retriever
                embeddings = NVIDIAEmbeddings(model="NV-Embed-QA")
                vector_store = FAISS.from_documents(chunks, embeddings)
                retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

                # Prompt & Model
                prompt = PromptTemplate(
                    template="""
                    You are a helpful AI assistant. Use the following context to answer the question below.

                    ⚠️ IMPORTANT: You must answer the question in the language specified below.

                    Language: {language}

                    Context:
                    {context}

                    Question:
                    {query}
                    """,
                    input_variables=["context", "query", "language"]
                )

                llm = ChatNVIDIA(model=model_name, temperature=temp)

                def format_docs(docs): 
                    return "\n\n".join(doc.page_content for doc in docs)

                parallel_chain = RunnableParallel({
                    "context": retriever | RunnableLambda(format_docs),
                    "query": RunnablePassthrough()
                })
                main_chain = parallel_chain | prompt.partial(language=output_lang) | llm | StrOutputParser()

                with st.spinner("💬 Generating response..."):
                    result = main_chain.invoke(user_query)
                    st.success("✅ Answer Ready!")

                    # Output
                    st.markdown("### 💬 Chatbot Response")
                    st.text_area("📌 Answer:", result, height=200)

                    # Add to history
                    st.session_state.chat_history.append((user_query, result))

                    # Voice Output (TTS)
                    tts_lang = {
                        "English": "en",
                        "Hindi": "hi",
                        "Bengali": "bn",
                        "Tamil": "ta",
                        "Telugu": "te",
                        "Marathi": "mr",
                        "Gujarati": "gu"
                    }.get(output_lang, "en")  # default to English

                    file_name = f"temp_{uuid.uuid4().hex}.mp3"
                    tts = gTTS(result, lang=tts_lang)
                    tts.save(file_name)
                    st.audio(file_name, format="audio/mp3")
                    os.remove(file_name)

            except (TranscriptsDisabled, NoTranscriptFound, CouldNotRetrieveTranscript):
                st.error("🚫 Transcript unavailable for this video.")
            except Exception as e:
                st.error(f"🔥 Error: {str(e)}")

# --- Chat History ---
if st.session_state.chat_history:
    st.markdown("## 🕘 Chat History")
    for i, (q, a) in enumerate(reversed(st.session_state.chat_history), 1):
        with st.expander(f"Q{i}: {q}"):
            st.markdown(a)
    chat_text = "\n\n".join([f"Q: {q}\nA: {a}" for q, a in st.session_state.chat_history])
    st.download_button("📥 Download Chat Log", chat_text, file_name="chat_log.txt")
