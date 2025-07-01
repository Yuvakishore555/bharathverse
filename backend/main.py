from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

stories = {
    "sita_haran": {
        "title": "Sita Haran",
        "summary": "Ravana disguised as a saint and kidnapped Sita when Rama and Lakshmana were away.",
        "audio": "/audio/sita_haran_en.wav"
    },
    "abhimanyu_vadh": {
        "title": "Abhimanyu Vadh",
        "summary": "Abhimanyu entered the Chakravyuha and was killed despite fighting bravely.",
        "audio": "/audio/abhimanyu_vadh_en.wav"
    },
    "vishnu_dashavatara": {
        "title": "Dashavatara",
        "summary": "Dashavatara refers to the ten avatars of Vishnu taken to restore cosmic balance.",
        "audio": "/audio/vishnu_dashavatara_en.wav"
    }
}

@app.get("/api/stories")
def list_stories():
    return [{"id": k, "title": v["title"]} for k, v in stories.items()]

@app.get("/api/story")
def get_story(id: str = Query(...)):
    return stories.get(id, {"error": "Story not found"})

@app.get("/audio/{filename}")
def get_audio(filename: str):
    return FileResponse(f"audio/{filename}")
