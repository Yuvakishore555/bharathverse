import streamlit as st
import requests
from gtts import gTTS
import os

st.set_page_config(page_title="BharathVerse", page_icon="🌿")
st.title("🌿 BharathVerse — Explore Indian Epics")

st.markdown("Enter a character, event, or place from Indian epics like Ramayana, Mahabharata.")

query = st.text_input("🔍 Search Term", placeholder="e.g., Arjuna, Lanka, Kurukshetra")
lang = st.selectbox("Choose Language", ["en", "hi"])

def fetch_from_wikipedia(term, lang_code):
    url = f"https://{lang_code}.wikipedia.org/api/rest_v1/page/summary/{term}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json().get("extract", "No summary found.")
    return "❌ Couldn’t fetch info."

def generate_audio(text, filename="output.mp3", lang_code="en"):
    tts = gTTS(text=text, lang=lang_code)
    tts.save(filename)
    return filename

if st.button("📖 Tell Me"):
    if query:
        result = fetch_from_wikipedia(query, lang)
        st.markdown(f"### 📘 {query}")
        st.write(result)

        with st.spinner("Generating voice..."):
            audio_file = generate_audio(result, f"{query}_{lang}.mp3", lang)
            audio_path = os.path.abspath(audio_file)
            st.audio(audio_path, format="audio/mp3")
    else:
        st.warning("Please enter a term to search.")

st.markdown("---")
st.caption("Made for WikiVerse Hackathon 2025 by Team BharathVerse")