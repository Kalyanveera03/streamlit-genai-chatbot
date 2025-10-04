from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

#loading the environment variables

load_dotenv()

#setting up the streamlit app

st.set_page_config(
    page_title="💬Chatbot",
    page_icon="🤖",
    layout="centered",
)

st.title("💬 Generative AI Chatbot")


#initializing the chat history

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
chat_history = []

#show the chat history

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


#llm initialization

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature=0.0,


)


user_prompt = st.chat_input("Enter your message here...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    response = llm.invoke(
        input = [{"role": "system","content":"You are a helpful assistant."}, *st.session_state.chat_history]
    )
    assistant_response = response.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)

        

