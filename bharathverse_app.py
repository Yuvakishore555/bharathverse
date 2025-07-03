import streamlit as st
import requests
from gtts import gTTS
import urllib.parse
import tempfile
import os

# --- CONFIG & STYLING ---
st.set_page_config(page_title="BharathVerse", page_icon="🌿", layout="centered")

st.markdown("""
    <style>
        .main { background-color: #0e1117; }
        .stButton>button {
            background-color: #4CAF50; color: white;
            padding: 10px 24px; border: none; font-size: 16px;
            border-radius: 16px; width: 100%;
        }
        .stSelectbox>div>div, .stTextInput>div>div>input {
            border-radius: 16px;
        }
        h1, h2 { text-align: center; }
        .sanskrit-header {
            font-family: 'Sanskrit Text', 'Devanagari', serif;
            font-size: 36px;
            color: gold;
            text-align: center;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- LANGUAGES & CHARACTERS ---
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

# --- DISPLAY SANSKRIT LINE ---
st.markdown('<div class="sanskrit-header">धर्मो रक्षति रक्षितः</div>', unsafe_allow_html=True)
st.markdown("---")

# --- FETCH WIKIPEDIA SUMMARY ---
@st.cache_data(ttl=3600)
def fetch_wikipedia_summary(term: str, lang_code: str):
    try:
        encoded_term = urllib.parse.quote(term.strip())
        url = f"https://{lang_code}.wikipedia.org/api/rest_v1/page/summary/{encoded_term}"
        headers = {'User-Agent': 'BharathVerseApp/1.0'}
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            return None
        data = res.json()
        return data.get("extract", None)
    except Exception as e:
        st.error(f"🌐 Network error: {e}")
        return None

# --- GENERATE AUDIO SAFELY ---
def generate_audio(text: str, lang_code: str) -> str | None:
    try:
        if not text.strip():
            return None
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            tts = gTTS(text=text, lang=lang_code)
            tts.save(tmp_file.name)
            return tmp_file.name
    except Exception as e:
        st.error(f"🔇 Audio error: {e}")
        return None

# --- APP LAYOUT ---
st.title("🌿 BharathVerse")
st.markdown("<h2>Explore Ramayana, Mahabharata & Puranas</h2>", unsafe_allow_html=True)
st.markdown("---")

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

st.markdown("---")

# --- FOOTER + OM CHANTING ---
st.caption("Built by Team BharathVerse for WikiVerse Hackathon 2025 🇮🇳")

# Om chanting from local file
om_path = "assets/om_chanting.mp3"
if os.path.exists(om_path):
    st.markdown("""
        <audio controls loop>
            <source src="assets/om_chanting.mp3" type="audio/mp3">
        </audio>
    """, unsafe_allow_html=True)
else:
    st.warning("🔇 Om chanting file not found. Please place it in `assets/om_chanting.mp3`.")
