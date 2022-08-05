def create_daily(date):
    return {
        "time_entry":
            {
                "description": "Daily meeting",
                "start": f"{date}T10:30:00+03:00",
                "duration": 900,
                "pid": 175371695,
                "created_with": "API"
            }
    }


def create_english(date):
    return {
        "time_entry":
            {
                "description": "Lesson",
                "start": f"{date}T15:00:00+03:00",
                "duration": 3600,
                "pid": 176403548,
                "created_with": "API"
            }
    }
