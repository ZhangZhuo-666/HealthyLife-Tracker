class User:
    def __init__(self, name):
        self.name = name


class HealthRecord:
    def __init__(self, date, activity, duration, water_intake, sleep_hours):
        self.date = date
        self.activity = activity
        self.duration = duration
        self.water_intake = water_intake
        self.sleep_hours = sleep_hours


class Reminder:
    def __init__(self, reminder_type, message):
        self.reminder_type = reminder_type
        self.message = message
