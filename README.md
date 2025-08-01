MinuteMate – Background Meeting Note Taker

Overview:
MinuteMate captures live meeting audio, transcribes it using OpenAI Whisper (offline), summarizes key points, extracts action items & reminders, and displays everything in a web interface.

Installation:

git clone https://github.com/yourname/minutemate.git
cd minutemate
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm

Tech Stack:
Python
PyAudio (audio capture)
Whisper-tiny (offline transcription)
spaCy (NLP)
Flask (API + web backend)
HTML/JS (single-page frontend)

How to Run:

python run.py

This will:
1) Start the background audio listener
2) Begin recording until silence or manual stop
3) Transcribe the audio with Whisper-tiny
4) Summarize and extract minutes
5) Start the local web server
6) Then, open your browser to:  http://127.0.0.1:5000

Web UI Features:

Polls /status to check when transcription is ready
Displays loading animation during recording
Presents structured summary, action items, and dates

NLP Logic:

Chunking: Splits transcript into ≤1000-token chunks
Summary: Extracts 200-word summary per meeting
Action Items: Detected using keyword patterns like "will", "need to"
Reminders: Dates extracted with regex (\d{1,2} [A-Za-z]+ etc.)

Testing:
Run unit tests with: pytest tests/

Tests cover:
Audio capture module
Transcription function
REST API endpoints