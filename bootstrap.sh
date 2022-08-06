#!/bin/bash
cd "$(dirname "$0")" || echo "cd error"

FILE=config.py
if [ ! -f "$FILE" ]; then
   touch "$FILE"
   echo "username_toggle = ''
password_toggle = ''

username_rally = ''
api_key_rally = ''

country = ''" > "$FILE"
fi

pip install -r requirements.txt