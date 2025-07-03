import streamlit as st
import requests
from gtts import gTTS
import urllib.parse
import tempfile
import base64
import os

# ------------------- PAGE CONFIG -------------------
st.set_page_config(page_title="BharathVerse", page_icon="🌿", layout="centered")

# ------------------- THEME STYLING -------------------
st.markdown("""
    <style>
        html, body, .main, [data-testid="stAppViewContainer"], .block-container {
            background-color: #0e1117 !important;
            color: #FAFAFA !important;
        }
        .sanskrit {
            text-align: center;
            font-size: 34px;
            font-family: 'Noto Serif', serif;
            color: gold;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }
        .welcome-label {
            font-size: 20px;
            color: #A0A0A0;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        h1, h2 {
            color: #FAFAFA !important;
            text-align: center;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 20px;
            padding: 10px 26px;
            border: none;
            border-radius: 14px;
            font-family: 'Noto Serif', serif;
            margin-top: 0.8rem;
        }
        .stTextInput>div>div>input {
            border-radius: 12px;
            font-size: 16px;
            padding: 8px;
        }
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-thumb {
            background: #888;
            border-radius: 10px;
        }
        ::-webkit-scrollbar-track {
            background: #0e1117;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------- SESSION STATE -------------------
if "app_started" not in st.session_state:
    st.session_state.app_started = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# ------------------- WELCOME SCREEN -------------------
if not st.session_state.app_started:
    st.markdown('<div class="sanskrit">Welcome to BharathVerse</div>', unsafe_allow_html=True)
    st.markdown('<div class="welcome-label">Enter your name to begin:</div>', unsafe_allow_html=True)
    name = st.text_input("", key="name_input")
    if st.button("🔱 Begin BharathVerse"):
        if name.strip():
            st.session_state.user_name = name.strip()
            st.session_state.app_started = True
            st.rerun()
        else:
            st.warning("Please enter your name before proceeding.")
    st.stop()

# ------------------- AUTO PLAY OM CHANT -------------------
def autoplay_audio(file_path: str):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            audio_bytes = f.read()
        b64 = base64.b64encode(audio_bytes).decode()
        autoplay_html = f"""
            <audio autoplay loop hidden>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        st.markdown(autoplay_html, unsafe_allow_html=True)

autoplay_audio("assets/om_chanting.mp3")

# ------------------- HEADER -------------------
st.markdown(f'<div class="sanskrit">धर्मो रक्षति रक्षितः</div>', unsafe_allow_html=True)

st.markdown(f"""
    <div style="text-align: center; font-size: 32px; font-weight: bold; color: white;">
        BharathVerse
    </div>
    <div style="text-align: center; font-size: 32px; font-weight: bold; color: white; margin-top: 0.5rem;">
        Explore Ramayana, Mahabharata & Puranas
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# ------------------- LANGUAGES & CHARACTERS -------------------
LANGUAGES = {
    "English": "en",
    "हिन्दी (Hindi)": "hi",
    "తెలుగు (Telugu)": "te"
}

CHARACTERS = {
    "en": ["Rama", "Krishna", "Arjuna", "Draupadi", "Hanuman",
           "Karna", "Bhishma", "Duryodhana", "Lakshmana", "Ravana"],
    "hi": ["राम", "कृष्ण", "अर्जुन", "द्रौपदी", "हनुमान",
           "कर्ण", "भीष्म", "दुर्योधन", "लक्ष्मण", "रावण"],
    "te": ["రాముడు", "శ్రీక్రిష్ణుడు", "అర్జునుడు", "ద్రౌపది", "హనుమంతుడు",
           "కర్ణుడు", "భీష్ముడు", "దుర్యోధనుడు", "లక్ష్మణుడు", "రావణాసురుడు"]
}

# ------------------- WIKIPEDIA FETCH -------------------
@st.cache_data(ttl=3600)
def fetch_wikipedia_summary(term: str, lang_code: str):
    try:
        encoded_term = urllib.parse.quote(term.strip())
        url = f"https://{lang_code}.wikipedia.org/api/rest_v1/page/summary/{encoded_term}"
        headers = {'User-Agent': 'BharathVerseApp/1.0'}
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            return None
        return res.json().get("extract", None)
    except Exception as e:
        st.error(f"🌐 Network error: {e}")
        return None

# ------------------- AUDIO GENERATOR -------------------
def generate_audio(text: str, lang_code: str) -> str | None:
    try:
        if not text.strip():
            return None
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            gTTS(text=text, lang=lang_code).save(tmp.name)
            return tmp.name
    except Exception as e:
        st.error(f"🔇 Audio error: {e}")
        return None

# ------------------- MAIN INTERFACE -------------------
col1, col2 = st.columns([1, 2])
with col1:
    selected_lang = st.selectbox("🌍 Choose Language", list(LANGUAGES.keys()))
    lang_code = LANGUAGES[selected_lang]
with col2:
    search_term = st.selectbox("🧙‍♂️ Choose a Character", CHARACTERS[lang_code])

if st.button("🔍 Explore"):
    st.markdown("---")
    with st.spinner(f"🔍 Searching for '{search_term}' in {selected_lang}..."):
        summary = fetch_wikipedia_summary(search_term, lang_code)

    fallback_used = False
    if not summary and lang_code != "en":
        st.info("📘 Not found in selected language. Trying English fallback...")
        with st.spinner("🔀 Searching in English..."):
            summary = fetch_wikipedia_summary(search_term, "en")
            lang_code = "en"
            fallback_used = True

    if summary:
        st.markdown(f"### 📖 Summary of {search_term}")
        if fallback_used:
            st.warning("⚠️ English fallback used due to missing article.")
        st.info(summary)

        with st.spinner("🎿 Generating audio..."):
            audio_path = generate_audio(summary, lang_code)
            if audio_path:
                st.audio(audio_path, format="audio/mp3")
            else:
                st.error("🔇 Could not play audio.")
    else:
        st.error("❌ No information found in any language.")

# ------------------- FOOTER -------------------
st.markdown("---")
st.caption(f"Welcome {st.session_state.user_name} | Built by Team BharathVerse 🇮🇳")
