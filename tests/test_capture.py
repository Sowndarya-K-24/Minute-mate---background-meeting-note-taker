import pytest
from capture import AudioCapture  

def test_buffer_starts_and_stops():
    ac = AudioCapture()
    ac.start()
    assert ac.is_recording is True

    ac.stop()
    assert ac.is_recording is False