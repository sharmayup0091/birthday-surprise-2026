import streamlit as st
import random

# ---------------- CONFIG ----------------

NAME = "Somya"   # Yahan naam change kar de

st.set_page_config(
    page_title="Birthday Surprise",
    page_icon="🎂",
    layout="centered"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #ffd6e7,
        #ffe4ef,
        #fff5fa
    );
}

.main-card{
    background:black;
    padding:30px;
    border-radius:25px;
    box-shadow:0px 8px 25px rgba(255,105,180,0.25);
    text-align:center;
}

.big{
    text-align:center;
    font-size:30px;
}

.stButton > button{
    border-radius:15px;
    border:none;
    background:#ff6fae;
    color:black;
    font-weight:bold;
    padding:10px 20px;
}

.stButton > button:hover{
    background:#ff4f9a;
    color:black;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------

if "step" not in st.session_state:
    st.session_state.step = 1

# ---------------- STEP 1 ----------------

if st.session_state.step == 1:

    st.markdown("""
    <div class='big'>
    🌸 💖 ✨ 🎂 ✨ 💖 🌸
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="main-card">
    <h1>🎂 Happy Birthday {NAME}! 🎂</h1>
    <h3>🌷 Aaj tere liye ek special surprise hai 🌷</h3>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("Open Surprise 💝"):
        st.session_state.step = 2
        st.rerun()

# ---------------- STEP 2 ----------------

elif st.session_state.step == 2:

    st.markdown("""
    <div class="main-card">
    <h2>👀 Kya tu surprise dekhna chahegi?</h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes 💖"):
            st.session_state.step = 3
            st.rerun()

    with col2:
        st.info(
            random.choice([
                "🥺 Pakka?",
                "😭 Itni mehnat ki hai yrr",
                "🌸 Ek baar dekh to le",
                "💔 Mat mana kar"
            ])
        )

# ---------------- STEP 3 ----------------

elif st.session_state.step == 3:

    compliments = [
        "😊 Teri smile bahut achhi hai.",
        "🌟 Tu bahut kind hai.",
        "✨ Tera vibe positive hai.",
        "💖 Tu logo ka din better bana deti hai.",
        "🌷 Tera sense of humor mast hai."
    ]

    st.markdown("""
    <div class="main-card">
    <h2>💖 Tere baare me ek baat...</h2>
    </div>
    """, unsafe_allow_html=True)

    st.success(random.choice(compliments))

    if st.button("Next ✨"):
        st.session_state.step = 4
        st.rerun()

# ---------------- STEP 4 ----------------

elif st.session_state.step == 4:

    st.markdown("""
    <div class="main-card">
    <h2>🎉 Birthday Challenge 🎉</h2>
    </div>
    """, unsafe_allow_html=True)

    st.radio(
        "Cake ka sabse important part kya hai? 😌",
        [
            "Cake 🍰",
            "Candles 🕯️",
            "Friends ❤️",
            "Photos 📸"
        ]
    )

    if st.button("Submit 🎁"):
        st.session_state.step = 5
        st.rerun()

# ---------------- STEP 5 ----------------

elif st.session_state.step == 5:

    st.balloons()

    st.markdown("""
    <div class="main-card">
    <h1>🎈 Surprise Complete 🎈</h1>
    <h3>😌 Answer galat tha...</h3>
    <h2>💖 Sabse important Birthday Girl hoti hai 💖</h2>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Gift 🎁"):
        st.session_state.step = 6
        st.rerun()

# ---------------- STEP 6 ----------------

elif st.session_state.step == 6:

    st.balloons()

    st.markdown(f"""
    <div class="main-card">
    <h1>🎁 Gift Unlocked 🎁</h1>

    <h3>💌 Dear {NAME},</h3>

    <p>
    🌸 Happy Birthday! 🌸
    </p>

    <p>
    Hamesha khush reh 😊<br>
    Haste reh 😆<br>
    Apne goals achieve kar 🚀<br>
    Aur aaj ka din full enjoy kar ✨
    </p>

    <p>
    💖 Unlimited Good Wishes Activated 💖
    </p>

    <p>
    🍰 Virtual Cake Delivered 🍰
    </p>

    <h2>🎂 Have an Amazing Birthday 🎂</h2>

    </div>
    """, unsafe_allow_html=True)

    st.success("🌷 Thank You For Opening The Surprise 🌷")

    st.snow()

    st.markdown("""
    <div style='text-align:center;font-size:30px'>
    🌸 💖 ✨ 🎂 🎁 ✨ 💖 🌸
    </div>
    """, unsafe_allow_html=True)