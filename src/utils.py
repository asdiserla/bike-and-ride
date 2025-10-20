import datetime

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