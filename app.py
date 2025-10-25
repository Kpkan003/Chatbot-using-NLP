import streamlit as st
import json
import random

# Load intents.json
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# File paths (make sure this path is correct for your system)
json_file_path = '/Users/kanch/OneDrive/Desktop/Chatbot_Project/intents.json'  # Adjust the path if necessary
# Load intents
intents = load_json(json_file_path)

# Function to get response
def get_response(user_input):
    for intent in intents['intents']:
        if any(pattern.lower() in user_input.lower() for pattern in intent['patterns']):
            return random.choice(intent['responses'])
    return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Streamlit app
st.title("Chatbot Interface 🤖")

# Persistent chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# User input section
with st.form("chat_form"):
    user_input = st.text_input("Type your message here:", key="user_input")
    submitted = st.form_submit_button("Send")

# If user submits a message
if submitted and user_input.strip():
    # Get bot response
    bot_response = get_response(user_input)
    
    # Update chat history
    st.session_state.chat_history.append({"user": user_input, "bot": bot_response})

# Display chat history
st.header("Chat History")
for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.experimental_rerun()
