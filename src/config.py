import os

BASE_DIR = os.path.dirname(__file__)
SOUND_DIR = os.path.join(BASE_DIR, "sounds")

SEASON_SOUNDS = {
    "Spring": [
        os.path.join(SOUND_DIR, "blackbird.wav"),
        os.path.join(SOUND_DIR, "blackbird.wav"),
        os.path.join(SOUND_DIR, "blackbird.wav"),
    ],
    "Summer": [
        os.path.join(SOUND_DIR, "blackbird.wav"),
        os.path.join(SOUND_DIR, "blackbird.wav"),
    ],
    "Autumn": [
        os.path.join(SOUND_DIR, "blackbird.wav"),
        os.path.join(SOUND_DIR, "blackbird.wav"),
    ],
    "Winter": [
        os.path.join(SOUND_DIR, "blackbird.wav"),
        os.path.join(SOUND_DIR, "blackbird.wav"),
    ],
}

VOLUME_TIME_OF_DAY = {
    "morning": 0.7,
    "afternoon": 1.0,
    "evening": 0.6,
    "night": 0.5
}

DING_ON_SOUND_PATH = os.path.join(SOUND_DIR, "ding_on.wav")
DING_OFF_SOUND_PATH = os.path.join(SOUND_DIR, "ding_off.wav")
