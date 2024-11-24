import os

import streamlit as st # type: ignore
from dotenv import load_dotenv
import google.generativeai as gen_ai # type: ignore

# load environment variables
load_dotenv()

# Configure Streamlit page setting
st.set_page_config(
    page_title="Chat with GeminiPro", 
    page_icon=":brain",
    layout="centered")


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

#Setup Google GeminiPro AI Model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')


# Function to translate roles between GeminiPro and Streamlit terminology
def translate_role_fo_streamlit(user_role):
    if user_role == 'model':
        return "Assistant"
    else:
        return user_role
    

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


# Display the Chatbot's title on the page
st.title("🤖Gemini-Pro AI Chatbot")


# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_fo_streamlit(message.role)):
        st.markdown(message.parts[0].text) 


# Input field for user's message
user_prompt = st.chat_input("Ask GeminiPro")
if user_prompt:
    # Add users's message to chat and display it
    st.chat_message("user").markdown(user_prompt)


    # Send user's message to GeminiPro and get the respone
    gemini_response = st.session_state.chat_session.send_message(user_prompt)


    # Display GeminiPro's response
    with st.chat_message("Assistant"):
        st.markdown(gemini_response.text)