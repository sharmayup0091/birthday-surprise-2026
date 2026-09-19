import time
import streamlit as st

# Page setup
st.set_page_config(
    page_title="Birthday Surprise 🎉", page_icon="🎂", layout="centered"
)


# Streamlit ke liye Browser Animation Function
def type_text(text, delay=0.04):
    placeholder = st.empty()
    displayed_text = ""
    for char in text:
        displayed_text += char
        placeholder.markdown(f"### {displayed_text}▌")
        time.sleep(delay)
    placeholder.markdown(f"### {displayed_text}")


# Main App Title
st.title("🎉 BIRTHDAY SURPRISE 🎉")
st.write("------------------------------------")

# Step 1: User Name Input
name = st.text_input("Hey! What's your name?")

if name:
    type_text(f"Hey {name}! 👋")

    # Step 2: Button to start surprise
    if st.button("Click here to see your Surprise 🎁"):
        st.balloons()  # Browser balloon animation

        type_text("I have prepared something special for you... ✨")
        time.sleep(0.8)

        # Loading spinner animation
        with st.spinner("Unlocking your surprise... ⏳"):
            time.sleep(2)

        st.snow()  # Browser snow effect
        st.header("🎂 HAPPY BIRTHDAY! 🎉")
        st.write("------------------------------------")

        messages = [
            f"Dear {name}! ❤️",
            "Today is your special day.",
            "So forget all the stress for a while 🥳,",
            "Smile a little more today 😄,",
            "Laugh a little louder 😆,",
            "And enjoy every moment! 🎉",
        ]

        for msg in messages:
            type_text(msg, delay=0.03)
            time.sleep(0.4)

        st.write("------------------------------------")
        st.subheader("✨ A LITTLE MESSAGE ✨")

        type_text(
            "May your life always be filled with happiness, good people, and beautiful memories. ❤️"
        )
        time.sleep(0.5)
        type_text("And remember... You deserve a beautiful year ahead! ✨")

        st.write("------------------------------------")
        st.balloons()
        st.success("Made with ❤️ just for you. Now go enjoy your day! 🎉 🥳")
