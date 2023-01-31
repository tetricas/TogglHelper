#!/bin/bash
cd "$(dirname "$0")" || echo "cd error"

FILE=config.py
if [ ! -f "$FILE" ]; then
   touch "$FILE"
   echo "username_toggle = ''
password_toggle = ''

username_work = ''
api_key_rally = ''

jira_domain = ''
api_key_jira = ''

country = ''
vacation = []

project_id =
organization_id =
workspace_id =
internal_id =
english_id = " > "$FILE"
fi

pip install -r requirements.txt