import time
import serial
from sound_manager import SoundManager

ser = serial.Serial('/dev/cu.usbmodem1101', 9600, timeout=1)
sound_mgr = SoundManager()
last_command = None

while True:
    line = ser.readline().decode().strip()
    if not line:
        time.sleep(0.1)
        continue

    if line != last_command:  # only react to changes
        last_command = line
        if line == "SOUNDON":
            sound_mgr.play_random_seasonal_sound()
        elif line == "SOUNDOFF":
            sound_mgr.stop_sound()
