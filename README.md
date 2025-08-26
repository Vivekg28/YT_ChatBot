<h1>🎥 YouTube Q&amp;A Chatbot</h1>

<!-- Optional: quick badges (replace # with real links/images) -->
<!-- <p>
  <img alt="License" src="https://img.shields.io/badge/License-MIT-green">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-blue">
  <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-app-red">
</p> -->

<h2>🔹 Overview</h2>
<ul>
  <li>AI-powered chatbot for <strong>YouTube video Q&amp;A</strong></li>
  <li>Built with <strong>LangChain</strong>, <strong>NVIDIA Embeddings</strong>, <strong>FAISS</strong>, and <strong>Mixtral LLM</strong></li>
  <li>Runs as a simple <strong>Streamlit</strong> web app</li>
</ul>

<h2>⚡ Features</h2>
<ul>
  <li>Auto-fetches <strong>YouTube transcripts</strong></li>
  <li>Converts transcript → <strong>NVIDIA embeddings</strong></li>
  <li>Stores &amp; searches with <strong>FAISS Vector DB</strong></li>
  <li>Generates answers via <strong>Mixtral</strong> (NVIDIA endpoints)</li>
  <li>Clean, interactive <strong>Streamlit UI</strong></li>
</ul>

<h2>🛠️ Tech Stack</h2>
<ul>
  <li>LangChain</li>
  <li>NVIDIA AI Endpoints (Embeddings + LLM)</li>
  <li>FAISS</li>
  <li>YouTube Transcript API</li>
  <li>Streamlit</li>
</ul>


<h2>▶️ Usage</h2>
<ul>
  <li>Run the app
    <pre><code class="language-bash">streamlit run app.py
</code></pre>
  </li>
  <li>Enter a <strong>YouTube URL</strong></li>
  <li>Ask questions → get <strong>AI-powered answers</strong></li>
</ul>


<h2>🚀 Future Work</h2>
<ul>
  <li>Support multiple videos</li>
  <li>Show timestamps in answers</li>
  <li>Summarization mode</li>
  <li>Deploy to Streamlit Cloud / Hugging Face Spaces</li>
</ul>


<!-- Optional collapsible: env & troubleshooting -->
<details>
  <summary><strong>🔧 Troubleshooting & Tips</strong></summary>
  <ul>
    <li>If transcripts aren’t found, ensure the video has captions or pass <code>languages=[&quot;en&quot;]</code> to the transcript fetcher.</li>
    <li>For long videos, increase chunk size/overlap in your text splitter to preserve context.</li>
    <li>Persist FAISS index in <code>data/</code> for faster repeated queries.</li>
  </ul>
</details>
