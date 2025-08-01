# backend/api.py
from flask import Flask, jsonify, send_from_directory
import threading

app = Flask(__name__, static_folder="../ui")

STATUS = {"state": "idle"}
MINUTES = {
    "summary": "",
    "actions": [],
    "reminders": []
}

@app.route("/status")
def status():
    return jsonify(STATUS)

@app.route("/minutes/<id>")
def minutes(id):
    return jsonify(MINUTES)

@app.route("/")
def serve_ui():
    return send_from_directory(app.static_folder, "index.html")

def start_api_server():
    app.run(debug=False, port=5000)