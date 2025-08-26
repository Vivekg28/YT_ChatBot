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

<h2>📂 Project Structure</h2>
<ul>
  <li><code>app.py</code> → Streamlit app</li>
  <li><code>chatbot.py</code> → Core chatbot logic (LangChain + FAISS)</li>
  <li><code>requirements.txt</code> → Dependencies</li>
  <li><code>data/</code> → (optional) saved FAISS index</li>
</ul>

<h2>⚙️ Installation</h2>
<ol>
  <li>Clone repo
    <pre><code class="language-bash">git clone https://github.com/your-username/youtube-chatbot.git
cd youtube-chatbot
</code></pre>
  </li>
  <li>Create &amp; activate virtual environment
    <pre><code class="language-bash">python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
</code></pre>
  </li>
  <li>Install dependencies
    <pre><code class="language-bash">pip install -r requirements.txt
</code></pre>
  </li>
  <li>Add NVIDIA API key in <code>.env</code>
    <pre><code class="language-ini">NVIDIA_API_KEY=your_api_key_here
</code></pre>
  </li>
</ol>

<h2>▶️ Usage</h2>
<ul>
  <li>Run the app
    <pre><code class="language-bash">streamlit run app.py
</code></pre>
  </li>
  <li>Enter a <strong>YouTube URL</strong></li>
  <li>Ask questions → get <strong>AI-powered answers</strong></li>
</ul>

<h2>📸 Demo</h2>
<ul>
  <li>Add screenshots or a GIF (e.g., <code>docs/demo.gif</code>)</li>
</ul>

<h2>🚀 Future Work</h2>
<ul>
  <li>Support multiple videos</li>
  <li>Show timestamps in answers</li>
  <li>Summarization mode</li>
  <li>Deploy to Streamlit Cloud / Hugging Face Spaces</li>
</ul>

<h2>🤝 Contributing</h2>
<ol>
  <li>Fork the repo</li>
  <li>Create a feature branch</li>
  <li>Open a pull request</li>
</ol>

<h2>📜 License</h2>
<ul>
  <li>MIT License © 2025 <em>Your Name</em></li>
</ul>

<hr>

<!-- Optional collapsible: env & troubleshooting -->
<details>
  <summary><strong>🔧 Troubleshooting & Tips</strong></summary>
  <ul>
    <li>If transcripts aren’t found, ensure the video has captions or pass <code>languages=[&quot;en&quot;]</code> to the transcript fetcher.</li>
    <li>For long videos, increase chunk size/overlap in your text splitter to preserve context.</li>
    <li>Persist FAISS index in <code>data/</code> for faster repeated queries.</li>
  </ul>
</details>
