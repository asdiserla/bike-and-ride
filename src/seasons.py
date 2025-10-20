import datetime as dt

class Season:
    def __init__(self, name, start_month, start_day, end_month, end_day):
        self.name = name
        self.start_month = start_month
        self.start_day = start_day
        self.end_month = end_month
        self.end_day = end_day

    def includes(self, date: dt.date) -> bool:
        start = dt.date(date.year, self.start_month, self.start_day)
        end = dt.date(date.year, self.end_month, self.end_day)

        # Handle seasons that cross year boundaries (winter)
        if end < start:
            end = dt.date(date.year + 1, self.end_month, self.end_day)

        return start <= date <= end


# Define seasons
seasons = [
    Season("Spring", 3, 1, 5, 31),
    Season("Summer", 6, 1, 8, 31),
    Season("Autumn", 9, 1, 11, 30),
    Season("Winter", 12, 1, 2, 28),
]


def get_season(date: dt.date) -> str:
    for s in seasons:
        if s.includes(date):
            return s.name
    return "Unknown"
