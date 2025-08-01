from backend.recorder import record_audio
from backend.transcriber import transcribe_audio
from backend.nlp_processor import process_transcript
from backend.api import start_api_server

import threading, time

def start_recording():
    print("🎤 Recording started...")
    audio_path = "audio/output.wav"
    record_audio(audio_path)
    print("✅ Recording finished. Transcribing...")
    transcript = transcribe_audio(audio_path)
    print("🧠 Transcription done. Processing NLP...")
    summary, actions, reminders = process_transcript(transcript)
    
    # Store results globally
    from backend.api import STATUS, MINUTES
    STATUS["state"] = "idle"
    MINUTES["summary"] = summary
    MINUTES["actions"] = actions
    MINUTES["reminders"] = reminders
    print("📄 Summary ready. Access through web UI.")

if __name__ == "__main__":
    threading.Thread(target=start_api_server).start()
    time.sleep(2)
    from backend.api import STATUS
    STATUS["state"] = "recording"
    start_recording()
