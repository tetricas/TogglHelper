def createDaily(day):
    return {
        "time_entry":
            {
                "description": "Daily meeting",
                "start": f"2022-06-{day}T10:45:00+03:00",
                "duration": 900,
                "pid": 175371695,
                "created_with": "API"
            }
    }


def createEnglish(day):
    return {
        "time_entry":
            {
                "description": "Lesson",
                "start": f"2022-06-{day}T15:00:00+03:00",
                "duration": 3600,
                "pid": 176403548,
                "created_with": "API"
            }
    }
