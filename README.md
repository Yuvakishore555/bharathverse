import streamlit as st
import requests
from gtts import gTTS
import os
import urllib.parse
import uuid

# --- CONFIG & STYLE ---
st.set_page_config(page_title="BharathVerse", page_icon="🌿", layout="centered")

st.markdown("""
    <style>
        .main { background-color: #f5f5f5; }
        .stButton>button {
            background-color: #4CAF50; color: white;
            padding: 10px 24px; border: none; font-size: 16px;
            border-radius: 16px; width: 100%;
        }
        .stSelectbox>div>div, .stTextInput>div>div>input {
            border-radius: 16px;
        }
        h1, h2 { text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- CLEANUP OLD AUDIO ---
if "last_audio" in st.session_state:
    old_file = st.session_state["last_audio"]
    if os.path.exists(old_file):
        os.remove(old_file)
    del st.session_state["last_audio"]

# --- LANGUAGE & CHARACTER SETUP ---
LANGUAGES = {
    "English": "en",
    "हिन्दी (Hindi)": "hi",
    "తెలుగు (Telugu)": "te"
}

CHARACTERS = {
    "en": [
        "Rama", "Krishna", "Arjuna", "Draupadi", "Hanuman",
        "Karna", "Bhishma", "Duryodhana", "Lakshmana", "Ravana"
    ],
    "hi": [
        "राम", "कृष्ण", "अर्जुन", "द्रौपदी", "हनुमान",
        "कर्ण", "भीष्म", "दुर्योधन", "लक्ष्मण", "रावण"
    ],
    "te": [
        "రాముడు", "శ్రీకృష్ణుడు", "అర్జునుడు", "ద్రౌపది", "హనుమంతుడు",
        "కర్ణుడు", "భీష్ముడు", "దుర్యోధనుడు", "లక్ష్మణుడు", "రావణాసురుడు"
    ]
}

# --- WIKI FETCH FUNCTION ---
@st.cache_data(ttl=3600)
def fetch_wikipedia_summary(term: str, lang_code: str):
    encoded_term = urllib.parse.quote(term.strip())
    url = f"https://{lang_code}.wikipedia.org/api/rest_v1/page/summary/{encoded_term}"
    headers = {'User-Agent': 'BharathVerseApp/1.0'}

    try:
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            return None
        data = res.json()
        return data.get("extract", None)
    except Exception as e:
        st.error(f"🌐 Network error: {e}")
        return None

# --- AUDIO GENERATION ---
@st.cache_data(ttl=3600)
def generate_audio(text: str, lang_code: str) -> str | None:
    try:
        if not text.strip(): return None
        filename = f"audio_{uuid.uuid4().hex}.mp3"
        tts = gTTS(text=text, lang=lang_code)
        tts.save(filename)
        return filename
    except Exception as e:
        st.error(f"🔇 Audio error: {e}")
        return None

# --- UI ---
st.title("🌿 BharathVerse")
st.markdown("<h2>Explore the World of Ramayana, Mahabharata & Puranas</h2>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    selected_lang = st.selectbox("🌍 Choose Language", list(LANGUAGES.keys()))
    lang_code = LANGUAGES[selected_lang]

with col2:
    search_term = st.selectbox("🧙‍♂️ Choose a Character", CHARACTERS[lang_code])

submit = st.button("🔍 Explore")

# --- MAIN LOGIC ---
if submit:
    st.markdown("---")
    st.spinner(f"Fetching summary of '{search_term}'...")

    summary = fetch_wikipedia_summary(search_term, lang_code)
    fallback = False

    if not summary and lang_code != "en":
        st.info("Not found in selected language. Trying English...")
        summary = fetch_wikipedia_summary(search_term, "en")
        lang_code = "en"
        fallback = True

    if summary:
        st.markdown(f"### 📖 Summary of {search_term}")
        if fallback:
            st.warning("⚠️ English fallback used due to unavailable article.")

        st.info(summary)

        audio_file = generate_audio(summary, lang_code)
        if audio_file:
            st.audio(audio_file, format="audio/mp3")
            st.session_state["last_audio"] = audio_file
    else:
        st.error("❌ Could not fetch information.")

# --- FAMILY TREE PLACEHOLDER ---
st.markdown("---")
with st.expander("🌳 View Family Tree (Coming Soon)"):
    st.markdown("""
    <svg width="100%" height="150" xmlns="http://www.w3.org/2000/svg">
        <rect width="100%" height="150" fill="#eee" />
        <text x="50%" y="50%" font-size="16" fill="#777" text-anchor="middle" dy=".3em">
            Family Tree Visualization Coming Soon...
        </text>
    </svg>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.caption("Built by Team BharathVerse for WikiVerse Hackathon 2025 🇮🇳")
