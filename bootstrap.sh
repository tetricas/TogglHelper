#!/bin/bash
cd "$(dirname "$0")" || echo "cd error"

FILE=config.py
if [ ! -f "$FILE" ]; then
   touch "$FILE"
   echo "username_toggle = ''
password_toggle = ''

username_rally = ''
api_key_rally = ''

country = ''
vacation = []

project_id =
organization_id =
workspace_id =
internal_id =" > "$FILE"
fi

pip install -r requirements.txt