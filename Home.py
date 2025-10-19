import streamlit as st
from src.helper import get_pdf_text, get_youtube_transcript, get_text_chunks, get_vector_store, get_conversational_chain

def main():
    st.set_page_config("Information Retrieval")
    st.header("Information Retrieval System")
    st.markdown(
        """
### *Ask. Search. Learn Smarter.*  

Welcome to the **Information Retrieval System**, an interactive tool that lets you ask questions directly from your favorite resources.  

You can chat with uploaded PDFs or YouTube videos to quickly find answers, summaries, or explanations - no more endless scrolling or manual searching.  

### **How to Use**
1. **Choose a Chatbot** - Select an option from the sidebar (PDF or YouTube).  
2. **Upload or Paste a Link** - Upload a PDF file or enter a YouTube video link.  
3. **Start Chatting** - Ask any question, and the chatbot will instantly retrieve and summarize the relevant information for you.  

### **Available Chatbots**
- **📄 PDF Chatbot** - Chat with documents like research papers, reports, or study materials.  
- **🎥 YouTube Chatbot** - Interact with YouTube videos (only English for now) through simple questions and get key insights instantly.  

""")
    


if __name__ == "__main__":
    main()