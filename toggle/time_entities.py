import config

daily_name = "Daily meeting"
english_name = "Lesson"

beginning_of_the_day = "10:30"


def create_time_entity(name, date, time, duration):
    seconds = int(duration * 3600)
    return {
        "description": name,
        "start": f"{date}T{time}:00+02:00",
        "duration": seconds,
        "pid": config.project_id,
        "wid": config.workspace_id,
        "created_with": "API"
    }
