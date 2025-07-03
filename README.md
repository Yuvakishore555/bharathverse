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

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live-green?logo=streamlit)](https://bharathverse-oj8yak8w3afqijpomlwkq6.streamlit.app/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)  
[📦 GitHub Repository](https://github.com/Yuvakishore555/bharathverse)  
[🛠 GitLab Repository](https://code.swecha.org/soai2025/soai-hackathon/Bharathverse)

# 🌿 BharathVerse — An Expert of Indian Epics!

**BharathVerse** is a Streamlit-powered app that brings Indian *Itihasa*—*Mahabharata*, *Ramayana*, and *Puranas*—to life using AI narration, multilingual search, and immersive background chanting.

> **“धर्मो रक्षति रक्षितः” — Dharma protects those who protect it.**

✨ **The webpage auto-plays with Om chanting for spiritual immersion.**

---

## 🔗 Live App Links

- 🚀 **Streamlit**: [bharathverse.streamlit.app](https://bharathverse-oj8yak8w3afqijpomlwkq6.streamlit.app/)
- 🤗 **Hugging Face Space**: [huggingface.co/spaces/YuvaKishoreM/bharathverse](https://huggingface.co/spaces/YuvaKishoreM/bharathverse)

---

## 🎯 Purpose

- Bridge mythology with historically contextual knowledge.
- Help students explore Indian culture using modern tech.
- Promote *itihaasa* through audio-visual storytelling.
- Ensure accessibility in English, Hindi, and Telugu.

---

## 🧠 Features

- 🔍 **Character-Based Search**
- 📖 **Wikipedia-Powered Summaries**
- 🗣️ **AI Voice Narration with gTTS**
- 🎵 **Auto-Playing Om Chanting Background**
- 🌐 **Multilingual Support:** English, Hindi, Telugu
- 🖤 **Dark Mode UI with Golden Sanskrit Styling**

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

## 👨‍💻 Team BharathVerse

- **Yuva Kishore**  
- **Yashwanth**  
- **Charitesh Reddy**  
- **Samanyu**  

---

## 🚀 Tech Stack

- 🧠 Dify (planned) – LLM Bot Integration
- 📄 Wikipedia REST API
- 🔊 Google Text-to-Speech (gTTS)
- 🐍 Python 3.10+
- 🎛️ Streamlit (1.26.0+)
- 🎨 Custom CSS, HTML, and embedded audio

---

## 🧪 Run Locally

```bash
git clone https://github.com/Yuvakishore555/bharathverse.git
cd bharathverse
python3 -m venv venv
source venv/bin/activate  # or .\\venv\\Scripts\\activate on Windows
pip install -r requirements.txt
streamlit run bharathverse_app.py
