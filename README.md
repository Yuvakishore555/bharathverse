[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Open in Streamlit](https://bharathverse-bwwxvff2ozzxqoaswsbfpt.streamlit.app/)

[📦 GitHub Repository](https://github.com/Yuvakishore555/bharathverse)  
[🛠 GitLab Repository](https://code.swecha.org/soai2025/soai-hackathon/Bharathverse)

# 📚 BharatVerse — An Expert of Indian Epics!

**BharatVerse** is an interactive AI-powered platform designed to explore Indian history, epics, and cultural legends — like the *Mahabharata*, *Ramayana*, and *Puranas* — using Wikipedia, Wikidata, and open-source language models. It makes the rich legacy of Indian *itihaas* accessible, understandable, and globally appreciated — without reducing it to just “myth.”

---

## 🔗 Chatbot Link  
👉 [https://udify.app/chat/afeCzONr7l2ifH5e](https://udify.app/chat/afeCzONr7l2ifH5e)

> ⚠️ *Cloud-hosted chatbot built using Dify LLM orchestration platform*

## 🔗 Streamlit App  
👉 (https://bharathverse-bwwxvff2ozzxqoaswsbfpt.streamlit.app/)

---

## 🎯 Purpose

- Bridge the gap between mythology and verified historical knowledge.
- Help students and enthusiasts learn Indian epics through modern tech.
- Use AI and voice narration to preserve and promote *itihaasa*.
- Deliver language accessibility across English, Hindi, and Telugu.

---

## 🧠 Features

- **🧬 Character-Based Search**
  - Explore popular characters across all three languages via dropdown.

- **🗣️ AI-Powered Summaries**
  - Wikipedia-based summaries with fallback to English if content is missing.

- **🎧 Multilingual Audio Narration**
  - Streamlit + gTTS speech playback in Telugu, Hindi, and English.

- **📍 Future: Myth Meets History**
  - Maps + locations like Kurukshetra, Lanka (Wikidata mapping planned).

- **🌳 Family Tree Visualizer**
  - Coming soon using SVG and Wikidata relationship graphs.

---

## 🌐 Supported Characters (Examples)

| English     | हिंदी (Hindi) | తెలుగు (Telugu)   |
|-------------|---------------|--------------------|
| Rama        | राम           | రాముడు             |
| Krishna     | कृष्ण         | శ్రీకృష్ణుడు       |
| Arjuna      | अर्जुन        | అర్జునుడు           |
| Draupadi    | द्रौपदी       | ద్రౌపది            |
| Hanuman     | हनुमान        | హనుమంతుడు         |
| Karna       | कर्ण          | కర్ణుడు            |
| Bhishma     | भीष्म         | భీష్ముడు           |
| Duryodhana  | दुर्योधन      | దుర్యోధనుడు       |
| Lakshmana   | लक्ष्मण        | లక్ష్మణుడు          |
| Ravana      | रावण          | రావణాసురుడు        |

---

## 👥 Team BharatVerse

- Yuva Kishore  
- Yashwanth  
- Charitesh Reddy
- Samanyu  

---

## 🚀 Tech Stack

- 🧠 **Dify** – LLM Bot Integration (Chat App)
- 📄 **Wikipedia/Wikidata REST APIs**
- 🐍 **Python (3.10+)**
- 🌐 **Streamlit** – Interactive UI
- 🔊 **gTTS** – Google Text-to-Speech
- 📊 **SVG** – (Planned) Family Trees

---

## 📈 Roadmap

- [x] Character selection dropdown
- [x] Multilingual summaries with fallback
- [x] Audio narration using gTTS
- [ ] Integrate Wikidata for Family Tree
- [ ] Timeline + Geographical Maps
- [ ] Mobile-first UI optimization

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/Yuvakishore555/bharathverse.git
cd bharathverse
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run bharathverse_app.py
