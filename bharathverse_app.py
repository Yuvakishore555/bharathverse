import streamlit as st
import requests
from gtts import gTTS
import os
import urllib.parse

# --- 1. APP CONFIGURATION & STYLING ---

st.set_page_config(
    page_title="BharathVerse",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="auto",
)

st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 16px;
            width: 100%;
        }
        .stTextInput>div>div>input {
            border-radius: 16px;
        }
        .stSelectbox>div>div {
            border-radius: 16px;
        }
        h1, h2 {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)


# --- 2. HELPER FUNCTIONS ---

@st.cache_data(ttl=3600)
def fetch_wikipedia_summary(term: str, lang_code: str):
    encoded_term = urllib.parse.quote(term.strip())
    api_url = f"https://{lang_code}.wikipedia.org/api/rest_v1/page/summary/{encoded_term}"

    headers = {
        'User-Agent': 'BharathVerseApp/1.0 (bharathverse@example.com)'
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if data.get("type") == "standard" and "extract" in data:
            return data["extract"]
        else:
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Network error: {e}")
        return None
    except Exception:
        return None


@st.cache_data(ttl=3600)
def generate_audio(text: str, lang_code: str) -> str | None:
    try:
        if not text or not text.strip():
            return None

        tts = gTTS(text=text, lang=lang_code, slow=False)
        audio_filename = "temp_audio.mp3"
        tts.save(audio_filename)
        return audio_filename
    except Exception as e:
        st.error(f"😔 Apologies, could not generate audio for this language. Error: {e}")
        return None


# --- 3. UI LAYOUT & USER INPUT ---

st.title("🌿 BharathVerse")
st.markdown("<h2>Explore the Rich World of Indian Epics</h2>", unsafe_allow_html=True)
st.markdown("---")

LANGUAGES = {
    "English": "en",
    "हिन्दी (Hindi)": "hi",
    "తెలుగు (Telugu)": "te"
}

col1, col2 = st.columns([1, 2])

with col1:
    selected_lang_name = st.selectbox("🗣️ Choose Language", options=list(LANGUAGES.keys()))
    lang_code = LANGUAGES[selected_lang_name]

with col2:
    search_term = st.text_input("🧘‍♂️ Enter a Character, Place, or Event", placeholder="e.g., Arjuna, Ayodhya, Kurukshetra War")

submit_button = st.button("🔍 Explore")


# --- 4. MAIN LOGIC & OUTPUT ---

if submit_button:
    if not search_term:
        st.warning("⚠️ Please enter a search term.")
    else:
        summary = None
        fallback_used = False

        with st.spinner(f"Searching for '{search_term}' in {selected_lang_name}..."):
            summary = fetch_wikipedia_summary(search_term, lang_code)

        if summary is None and lang_code != 'en':
            fallback_used = True
            st.info(f"'{search_term}' not found in {selected_lang_name}. Attempting to fetch in English...")
            with st.spinner("Searching in English..."):
                summary = fetch_wikipedia_summary(search_term, 'en')
                if summary:
                    lang_code = 'en'

        st.markdown("---")
        if summary:
            st.markdown(f"### 📖 Summary for: {search_term.title()}")

            if fallback_used:
                st.warning("📜 Displaying result from English Wikipedia as the primary language version was not found.")

            st.info(summary)

            with st.spinner("🧘‍♂️ Generating audio..."):
                audio_file = generate_audio(summary, lang_code)
                if audio_file:
                    st.audio(audio_file, format="audio/mp3")
                    if os.path.exists(audio_file):
                        os.remove(audio_file)
                else:
                    st.error("Could not generate audio for the summary.")
        else:
            st.error(f"❌ Sorry, could not find any information for '{search_term}' on Wikipedia in the selected languages.")


# --- 5. BONUS: FAMILY TREE PLACEHOLDER ---

st.markdown("---")
with st.expander("🌳 View Family Tree (Placeholder)"):
    st.markdown("This is a placeholder for a future feature where a family tree or event timeline will be displayed.")
    svg_placeholder = """
    <svg width="100%" height="150" viewBox="0 0 400 150" xmlns="http://www.w3.org/2000/svg">
      <rect width="400" height="150" fill="#EFEFEF"/>
      <text x="50%" y="50%" font-family="Arial, sans-serif" font-size="16" fill="#888" text-anchor="middle" dy=".3em">
        Family Tree/Timeline Visualization Coming Soon...
      </text>
    </svg>
    """
    st.markdown(svg_placeholder, unsafe_allow_html=True)


# --- 6. FOOTER ---

st.markdown("---")
st.caption("Made with ❤️ for the Indian AI Hackathon by **Team BharathVerse**.")
