import streamlit as st
import requests
from gtts import gTTS
import urllib.parse
import tempfile
import os

# -------------------- CONFIGURATION --------------------
st.set_page_config(page_title="BharathVerse", page_icon="🌿", layout="centered")

if "chanting_played" not in st.session_state:
    st.session_state.chanting_played = False

# -------------------- STYLING --------------------------
st.markdown("""
    <style>
    body, .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        font-size: 16px;
        border-radius: 16px;
        border: none;
        width: 100%;
    }
    .stSelectbox > div > div, .stTextInput > div > div > input {
        border-radius: 16px;
    }
    h1, h2, h3, h4, h5, h6 {
        color: white;
        text-align: center;
    }
    .title-text {
        font-size: 22px;
        color: gold;
        font-family: 'Sanskrit Text', 'Noto Sans', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- LANGUAGES & CHARACTERS --------------------------
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

# -------------------- WIKI FETCH --------------------------
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

# -------------------- TTS GENERATOR --------------------------
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

# -------------------- TITLE --------------------------
st.markdown('<p class="title-text">धर्मो रक्षति रक्षितः</p>', unsafe_allow_html=True)
st.markdown('<h1>🌿 BharathVerse</h1>', unsafe_allow_html=True)
st.markdown('<h2>Explore Ramayana, Mahabharata & Puranas</h2>', unsafe_allow_html=True)
st.markdown("---")

# -------------------- AUDIO PLAYER --------------------------
om_audio_path = os.path.join("assets", "om_chanting.mp3")

# HTML for autoplay and hidden player
audio_html = f"""
<audio autoplay loop style="display:none;" id="bg-audio">
  <source src="{om_audio_path}" type="audio/mp3">
</audio>
<script>
  var audio = document.getElementById("bg-audio");
  var playPromise = audio.play();
  if (playPromise !== undefined) {{
    playPromise.catch(() => {{
      document.getElementById("audio-btn").style.display = "inline-block";
    }});
  }}
</script>
"""

# Manual button fallback if autoplay fails (for mobile)
st.markdown(audio_html, unsafe_allow_html=True)

if not st.session_state.chanting_played:
    if st.button("🔊 Tap to Play Om Chanting", key="audio-btn"):
        st.audio(om_audio_path, format="audio/mp3", loop=True)
        st.session_state.chanting_played = True

# -------------------- SELECTORS --------------------------
col1, col2 = st.columns([1, 2])

with col1:
    selected_lang = st.selectbox("🌍 Choose Language", list(LANGUAGES.keys()))
    lang_code = LANGUAGES[selected_lang]

with col2:
    search_term = st.selectbox("🧙‍♂️ Choose a Character", CHARACTERS[lang_code])

# -------------------- SEARCH HANDLER --------------------------
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

# -------------------- FOOTER --------------------------
st.markdown("---")
st.caption("Built by Team BharathVerse for WikiVerse Hackathon 2025 🇮🇳")
