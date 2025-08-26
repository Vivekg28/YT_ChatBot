🎥 YouTube Q&A Chatbot

An AI-powered YouTube Question-Answering Chatbot built with LangChain, NVIDIA Embeddings, FAISS, and Mixtral LLM, wrapped in a sleek Streamlit app.
This chatbot extracts transcripts from YouTube videos and allows users to ask questions in natural language. The bot then fetches the most relevant video segments and generates accurate, context-aware answers.

⚡ Features
🔗 Fetches YouTube transcripts automatically
🧠 Embeds video content using NVIDIA Embeddings
📚 Stores embeddings in FAISS Vector Database
🤖 Uses Mixtral LLM (via NVIDIA endpoints) for response generation
🎛️ Interactive Streamlit UI
🚀 Supports Q&A over long YouTube videos

🛠️ Tech Stack
LangChain
 – Orchestration
NVIDIA AI Endpoints
 – Embeddings + LLM
FAISS
 – Vector search
YouTube Transcript API
 – Transcript extraction
Streamlit
 – Web app UI

📂 Project Structure
📦 youtube-chatbot
 ┣ 📜 app.py              # Streamlit app
 ┣ 📜 chatbot.py          # Core chatbot logic (LangChain + FAISS)
 ┣ 📜 requirements.txt    # Dependencies
 ┣ 📜 README.md           # Project documentation
 ┗ 📂 data/               # (Optional) Saved FAISS index

⚙️ Installation
Clone the repo
git clone https://github.com/your-username/youtube-chatbot.git
cd youtube-chatbot

Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

Install dependencies
pip install -r requirements.txt

Set environment variables
Create a .env file and add your NVIDIA API key:
NVIDIA_API_KEY=your_api_key_here

▶️ Usage
Run the Streamlit app:
streamlit run app.py

Enter a YouTube video URL
Ask any question related to the video
Get AI-powered answers with context from the transcript 🎯

🚀 Future Improvements
Add support for multiple videos
Highlight timestamps in answers
Summarization mode
