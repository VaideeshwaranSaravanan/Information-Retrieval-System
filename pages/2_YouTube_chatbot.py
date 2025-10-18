import streamlit as st
from src.helper import get_youtube_transcript, get_text_chunks, get_vector_store, get_conversational_chain


def user_input(user_question):
    response = st.session_state.conversation_1({'question':user_question})
    st.session_state.chatHistory_1 = response['chat_history']
    

def main():
    st.set_page_config("Information Retrieval")
    st.title("YouTube Chatbot")
    if "conversation_1" not in st.session_state:
        st.session_state.conversation_1 = None
    if "chatHistory_1" not in st.session_state:
        st.session_state.chatHistory_1 = None
    
    with st.container(border=True):
        yt_link = st.text_input("Enter your youtube link(s) here separated by vertical bar (|) if multiple")
        st.write("Click submit & process button once entered")
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_youtube_transcript(yt_link)
                text_chunks = get_text_chunks(raw_text)
                vector_store = get_vector_store(text_chunks)
                st.session_state.conversation_1 = get_conversational_chain(vector_store)
                st.success("Done")

    user_question = st.chat_input("Ask a Question from YouTube link")
    if user_question:
        user_input(user_question)
    
    if st.session_state.chatHistory_1:
        for i, message in enumerate(st.session_state.chatHistory_1):
            if i%2==0:
                st.write("User:", message.content)
            else:
                st.write("Reply:", message.content)
    


if __name__ == "__main__":
    main()