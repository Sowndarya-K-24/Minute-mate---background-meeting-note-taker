import os
from transcriber import transcribe_audio  

def test_transcription_output_exists():
    transcript = transcribe_audio("tests/sample.wav")
    assert isinstance(transcript, str)
    assert len(transcript) > 10  