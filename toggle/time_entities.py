import config

fifteen_min = 900
hour = 4 * fifteen_min


def create_daily(date):
    return {
        "description": "Daily meeting",
        "start": f"{date}T10:30:00+03:00",
        "duration": fifteen_min,
        "pid": config.project_id,
        "wid": config.workspace_id,
        "created_with": "API"
    }


def create_english(date):
    return {
        "description": "Lesson",
        "start": f"{date}T15:00:00+03:00",
        "duration": hour,
        "pid": config.internal_id,
        "wid": config.workspace_id,
        "created_with": "API"
    }


def create_rally(date, name):
    return {
        "description": f"{name}",
        "start": f"{date}T10:45:00+03:00",
        "duration": 7 * hour + 3 * fifteen_min,
        "pid": config.project_id,
        "wid": config.workspace_id,
        "created_with": "API"
    }


def create_rally_friday_before(date, name):
    return {
        "description": f"{name}",
        "start": f"{date}T10:00:00+03:00",
        "duration": 4 * hour,
        "pid": config.project_id,
        "wid": config.workspace_id,
        "created_with": "API"
    }


def create_rally_friday_after(date, name):
    return {
        "description": f"{name}",
        "start": f"{date}T16:00:00+03:00",
        "duration": 3 * hour,
        "pid": config.project_id,
        "wid": config.workspace_id,
        "created_with": "API"
    }
