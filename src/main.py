import os
import time
import random
import datetime
import serial
import pygame

from seasons import get_season

BASE_DIR = os.path.dirname(__file__)
SOUND_DIR = os.path.join(BASE_DIR, "sounds")

pygame.mixer.init()

ser = serial.Serial('/dev/cu.usbmodem1101', 9600, timeout=1)

season_sounds = {
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

volume_time_of_day = {
    "morning": 0.7,
    "afternoon": 1.0,
    "evening": 0.6,
    "night": 0.5
}

current_sound = None
current_sound_name = None
is_playing = False

def get_time_of_day():
    now = datetime.datetime.now().time()

    if datetime.time(6) <= now < datetime.time(12):
        return "morning"
    elif datetime.time(12) <= now < datetime.time(18):
        return "afternoon"
    elif datetime.time(18) <= now < datetime.time(24):
        return "evening"
    else:
        return "night"
    
def get_current_season_sounds():
    today = datetime.date.today()
    season_name = get_season(today)
    return season_sounds.get(season_name, [])


while True:
    line = ser.readline().decode().strip()

    if not line:
        time.sleep(0.1)
        continue

    if line == "SOUNDON":
        print("Distance < 30 cm! Playing sound...")

        if not is_playing:
            available_sounds = get_current_season_sounds()
            if not available_sounds:
                print("No sounds found for current season.")
                continue

            # Get a random sound
            current_sound_name = random.choice(available_sounds)
            current_sound = pygame.mixer.Sound(current_sound_name)

            # Set the volume based on time of day
            time_of_day = get_time_of_day()
            volume = volume_time_of_day[time_of_day]
            current_sound.set_volume(volume)

            # Play the sound
            current_sound.play(loops=-1, fade_ms=1000)
            is_playing = True
            print(f"Now playing: {current_sound_name}")
        else:
            pass
    elif line == "SOUNDOFF":
        if is_playing and current_sound:
            print(f"Stopping sound: {current_sound_name}")
            current_sound.fadeout(1000)
            is_playing = False
            current_sound = None
            current_sound_name = None