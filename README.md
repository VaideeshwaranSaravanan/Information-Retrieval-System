# Information Retrieval System  
### *Ask. Search. Learn Smarter.*  
---

An interactive **information retrieval platform** built with **Streamlit**, designed to help users **chat directly with their content** — whether it’s a PDF document or a YouTube video.  
Powered by **Google Gemini** and **LangChain**, this project brings conversational intelligence to your study materials, lectures, and online resources.

---

## Features
- **PDF Chatbot** – Upload PDFs and ask questions directly from the document.  
- **YouTube Chatbot** – Paste a YouTube video link and chat with its transcript.  
- **Conversational Interface** – Clean, intuitive Streamlit design for smooth interaction.  
- **Google Gemini Integration** – Smarter, more accurate, and context-aware responses.  
- **LangChain-powered Retrieval** – For intelligent text splitting, embedding, and vector search.  

---

## How to Use
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/information-retrieval-system.git
   cd information-retrieval-system

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Set up your environment variables**
    Create a .env file and add your Gemini API key:
   ```bash
   GOOGLE_API_KEY = your_api_key_here

4. **Run the Streamlit App**
   ```bash
   streamlit run Home.py

5. **Access the Interface**
   ```bash
   Open http://localhost:8501 in your browser.

## How It Works

1. The system loads and preprocesses text from resources.  
2. **LangChain** splits text into smaller chunks and embeds them using a vector store.  
3. When you ask a question, the system retrieves the most relevant chunks using **similarity search**.  
4. **Google Gemini** generates a conversational, context-rich answer in real time.  

---

## Future Improvements

- Add **multi-file querying** for batch document or video comparison.  
- Support **web article** and **text file** retrieval.  
- Enable **voice input/output** for interactive Q&A.  
- Deploy online via **Streamlit Cloud** or **Hugging Face Spaces**.  

---

## Credits & Acknowledgment

This project was **inspired by a [YouTube tutorial](https://www.youtube.com/watch?v=X193V1CSZZE)** demonstrating a basic PDF chatbot using **Streamlit**, **LangChain**, and **Google PaLM**.  

### Enhancements:
- Added **YouTube Chatbot** and improvised **PDF Chatbot** functionality.  
- Integrated **Google Gemini** for superior response quality.  
- Upgraded **Streamlit UI** with sidebar navigation and better design.  
- Improved overall retrieval flow and efficiency.  

---

## AI Assistance

This project’s **homepage content**, and **README structure** were collaboratively written and refined with assistance from **ChatGPT (OpenAI GPT-5)**.   


