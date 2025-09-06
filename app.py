import streamlit as st

st.set_page_config(page_title="Anime Chat", page_icon="🎌")

st.title("🎌 Anime Chatbot")
st.write("Talk to the app by typing your favorite anime!")

# Text input from user
user_input = st.text_input("Type an anime name:")

# Responses dictionary (you can expand this)
responses = {
    "naruto": "Ah, a classic! Believe it! 🍜",
    "one piece": "Yo ho ho! Ready to find the One Piece? ☠️",
    "attack on titan": "Titans incoming! Get your ODM gear ready! 🔥",
    "death note": "Just don't write my name in the notebook... ✍️",
    "demon slayer": "Total concentration breathing! ⚔️",
    "bleach": "Bankai!! 🗡️",
}

# Normalize user input
anime = user_input.strip().lower()

if user_input:
    # Show user message
    st.markdown(f"🧑 **You:** {user_input}")

    # App response
    response = responses.get(anime, "Hmm... I haven't seen that one yet. Got any recommendations?")
    st.markdown(f"💬 **App:** {response}")
