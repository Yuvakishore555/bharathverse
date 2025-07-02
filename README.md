---
title: BharathVerse
emoji: 🌿
colorFrom: green
colorTo: indigo
sdk: streamlit
sdk_version: 1.46.1
app_file: bharathverse_app.py
pinned: false
---

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)  
[📦 GitHub Repository](https://github.com/Yuvakishore555/bharathverse)  
[🛠 GitLab Repository](https://code.swecha.org/soai2025/soai-hackathon/Bharathverse)

# 📚 BharatVerse — An Expert of Indian Epics!

**BharatVerse** is an interactive AI-powered platform designed to explore Indian history, epics, and cultural legends — like the *Mahabharata*, *Ramayana*, and *Puranas* — using Wikipedia and open-source tools. It makes the rich legacy of Indian *itihaas* accessible, understandable, and globally appreciated — without reducing it to just “myth.”

---

## 🔗 Streamlit App  
👉 [Live on Streamlit](https://bharathverse-bwwxvff2ozzxqoaswsbfpt.streamlit.app/#bharath-verse)

## 🔗 Hugging Face Space  
👉 [Live on Hugging Face](https://huggingface.co/spaces/YuvaKishoreM/bharathverse)

---

## 🎯 Purpose

- Bridge the gap between mythology and verified historical knowledge.
- Help students and enthusiasts learn Indian epics through modern tech.
- Use AI and voice narration to preserve and promote *itihaasa*.
- Deliver language accessibility across English, Hindi, and Telugu.

---

## 🧠 Features

- **🧬 Character-Based Search**
- **🗣️ AI-Powered Wikipedia Summaries**
- **🎧 Multilingual Audio Narration (gTTS)**
- **🌐 Language Support:** English, Hindi, Telugu
- *(🔜 Family Tree, Maps coming soon)*

---

## 🌐 Supported Characters

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

- 🧠 Dify – LLM Bot Integration (for future roadmap)
- 📄 Wikipedia REST API
- 🔊 gTTS (Google Text-to-Speech)
- 🐍 Python 3.10+
- 🌐 Streamlit UI

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/Yuvakishore555/bharathverse.git
cd bharathverse
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run bharathverse_app.py