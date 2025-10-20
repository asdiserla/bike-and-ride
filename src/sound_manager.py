import pygame
import random
from config import SEASON_SOUNDS, VOLUME_TIME_OF_DAY, DING_SOUND_PATH
from utils import get_time_of_day
from seasons import get_season
import datetime

pygame.mixer.init()

class SoundManager:
    def __init__(self):
        self.current_sound = None
        self.current_sound_name = None
        self.is_playing = False
        self.ding_sound = pygame.mixer.Sound(DING_SOUND_PATH)

    def get_current_season_sounds(self):
        today = datetime.date.today()
        season_name = get_season(today)
        return SEASON_SOUNDS.get(season_name, [])

    def play_random_seasonal_sound(self):
        if self.is_playing:
            return

        available_sounds = self.get_current_season_sounds()
        if not available_sounds:
            print("No sounds found for current season.")
            return

        self.current_sound_name = random.choice(available_sounds)
        self.current_sound = pygame.mixer.Sound(self.current_sound_name)

        # Set volume based on time of day
        self.current_sound.set_volume(VOLUME_TIME_OF_DAY[get_time_of_day()])

        # Play ding first
        ding_channel = pygame.mixer.find_channel()
        seasonal_channel = pygame.mixer.find_channel()
        if not ding_channel or not seasonal_channel:
            print("No free audio channels available!")
            return

        ding_channel.play(self.ding_sound)
        while ding_channel.get_busy():
            pygame.time.wait(10)

        # Play seasonal sound
        seasonal_channel.play(self.current_sound, loops=-1, fade_ms=1000)
        self.is_playing = True
        print(f"Now playing: {self.current_sound_name}")

    def stop_sound(self):
        if self.is_playing and self.current_sound:
            print(f"Stopping sound: {self.current_sound_name}")
            self.current_sound.fadeout(1000)
            self.is_playing = False
            self.current_sound = None
            self.current_sound_name = None
