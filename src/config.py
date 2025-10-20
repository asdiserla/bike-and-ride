import os

BASE_DIR = os.path.dirname(__file__)
SOUND_DIR = os.path.join(BASE_DIR, "sounds")

SEASON_SOUNDS = {
    "Spring": [
        os.path.join(SOUND_DIR, "bird1.wav"),
        os.path.join(SOUND_DIR, "bird2.wav"),
        os.path.join(SOUND_DIR, "bird3.wav"),
    ],
    "Summer": [
        os.path.join(SOUND_DIR, "bird3.wav"),
        os.path.join(SOUND_DIR, "bird5.wav"),
    ],
    "Autumn": [
        os.path.join(SOUND_DIR, "bird1.wav"),
        os.path.join(SOUND_DIR, "bird2.wav"),
    ],
    "Winter": [
        os.path.join(SOUND_DIR, "bird3.wav"),
        os.path.join(SOUND_DIR, "bird4.wav"),
    ],
}

VOLUME_TIME_OF_DAY = {
    "morning": 0.7,
    "afternoon": 1.0,
    "evening": 0.6,
    "night": 0.5
}

DING_SOUND_PATH = os.path.join(SOUND_DIR, "ding.mp3.wav")
