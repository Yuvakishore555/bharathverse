import streamlit as st
import requests

st.set_page_config(page_title="BharatVerse", page_icon="🌿")
st.title("🌿 BharatVerse — Explore Indian Epics with AI")

st.markdown("Ask about characters, places, or events from Ramayana, Mahabharata & more.")

# Input
query = st.text_input("🔍 Who or what do you want to know about?", placeholder="e.g., Arjuna, Lanka, Kurukshetra")

# Language toggle (optional)
lang = st.selectbox("Choose Language", ["en", "hi"])

def fetch_from_wiki(term, lang_code='en'):
    url = f"https://{lang_code}.wikipedia.org/api/rest_v1/page/summary/{term}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("extract", "No content available.")
    else:
        return "I couldn’t find anything matching that."

if st.button("Tell me 📜"):
    if query:
        result = fetch_from_wiki(query, lang)
        st.markdown(f"### 📖 About {query}")
        st.write(result)
    else:
        st.warning("Please type something!")

# Optional Placeholder for future features
with st.expander("📍 View Family Tree (Coming Soon)"):
    st.markdown("Family tree visualizations are under development.")

with st.expander("🎧 Listen to Story (Beta)"):
    st.markdown("_Voice narration coming in next version!_")

st.markdown("---")
st.caption("Built by Team BharatVerse — WikiVerse Hackathon 2025")
