from gtts import gTTS

story_audio = {
    "sita_haran_en.wav": "Ravana disguised as a saint and kidnapped Sita when Rama and Lakshmana were away.",
    "abhimanyu_vadh_en.wav": "Abhimanyu entered the Chakravyuha and was killed despite fighting bravely.",
    "vishnu_dashavatara_en.wav": "Dashavatara refers to the ten avatars of Vishnu taken to restore cosmic balance."
}

for filename, text in story_audio.items():
    tts = gTTS(text=text, lang='en')
    tts.save(f"audio/{filename}")
