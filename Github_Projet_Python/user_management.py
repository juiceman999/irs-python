import os
import json

def save_user_info(info):
    with open('user_info.json', 'w') as file:
        json.dump(info, file)

def load_user_info():
    if os.path.exists('user_info.json'):
        with open('user_info.json', 'r') as file:
            return json.load(file)
    return None
