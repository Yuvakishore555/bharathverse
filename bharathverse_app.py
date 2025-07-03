import streamlit as st
import requests
from gtts import gTTS
import urllib.parse
import tempfile

# --- CONFIG & STYLING ---
st.set_page_config(page_title="BharathVerse", page_icon="🌿", layout="centered")

st.markdown("""
    <style>
        html, body, .main {
            background: linear-gradient(rgba(13,17,23,0.9), rgba(13,17,23,0.95)),
                        url("https://i.ibb.co/3kmbxSR/epic-bg.jpg");
            background-size: cover;
            background-position: center;
            color: #e6edf3;
            font-family: 'Segoe UI', sans-serif;
        }

        .block-container {
            background-color: rgba(28, 31, 38, 0.6);
            backdrop-filter: blur(10px);
            padding: 2rem 2rem;
            border-radius: 16px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }

        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 20px;
            font-size: 16px;
            width: 100%;
            font-weight: bold;
            transition: all 0.3s ease-in-out;
        }

        .stButton>button:hover {
            background-color: #45a049;
            transform: scale(1.03);
        }

        .stSelectbox>div>div, .stTextInput>div>div>input {
            border-radius: 12px !important;
            background-color: rgba(255,255,255,0.07);
            color: white !important;
        }

        h1, h2, h3 {
            text-align: center;
            color: #f0f6fc;
        }

        footer {
            color: #8b949e;
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

# --- GENERATE AUDIO ---
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
st.caption("🚀 Built with 🇮🇳 love by Team BharathVerse for WikiVerse Hackathon 2025")
