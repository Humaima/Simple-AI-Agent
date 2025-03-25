import os
import streamlit as st
from groq import Groq
from duckduckgo_search import DDGS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Ensure API key is provided
if not GROQ_API_KEY:
    st.error("⚠️ Error: GROQ_API_KEY is missing. Please add it to the .env file.")
    st.stop()

# Initialize Groq client
groq_client = Groq(api_key=GROQ_API_KEY)

# Function to interact with Groq LLM
def chat_with_llm(prompt):
    try:
        response = groq_client.chat.completions.create(
            model="gemma2-9b-it",  
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error with LLM: {str(e)}"

# Function to perform DuckDuckGo search
def search_web(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=1))
            if results:
                return f"🔍 **Search Result:** [{results[0]['title']}]({results[0]['href']})"
        return "⚠️ No relevant search results found."
    except Exception as e:
        return f"⚠️ Error with search: {str(e)}"

# Streamlit UI Setup
st.set_page_config(page_title="ChatBot Agent", page_icon="🤖", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
    body {
        background-color: #f8f9fa;
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .stTextInput>div>div>input {
        font-size: 16px !important;
    }
    .stButton>button {
        background-color: #4CAF50 !important;
        color: white !important;
        font-size: 16px !important;
        border-radius: 8px !important;
    }
    .stMarkdown {
        font-size: 18px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.markdown("<h1 style='text-align: center;'>🤖 ChatBot Agent</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>An AI-powered chatbot with web search capabilities.</p>", unsafe_allow_html=True)

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Process user input
    if user_input.lower().startswith("search "):
        query = user_input.replace("search ", "").strip()
        bot_response = search_web(query)
    else:
        bot_response = chat_with_llm(user_input)

    # Store bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(bot_response)