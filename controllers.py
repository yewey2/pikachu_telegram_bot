import json, csv, datetime
from os import path, mkdir, listdir, makedirs

def get_user(chat_id):
    try:
        if not path.exists('./database/users'):
            makedirs('./database/users')
        with open(f'./database/users/{chat_id}.json', 'r') as f:
            user_data = json.load(f)
    except FileNotFoundError: # User doesn't exist!
        user_data = None
    return user_data

def update_user(user_data):
    chat_id = user_data.get('chat_id', None)
    if not chat_id:
        return None
    if not path.exists('database/users'):
        makedirs('database/users')
    with open(f'database/users/{chat_id}.json', 'w') as f:
        json.dump(user_data, f, sort_keys=True, indent=4)
    return True

def new_user(chat_id: int, username:str="", first_name: str="", last_name:str=""):
    if not path.exists('./database/users'):
        makedirs('./database/users')
    user_data = {
        'chat_id': chat_id,
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'saved': [],
    }
    with open(f'database/users/{chat_id}.json', 'w') as f:
        json.dump(user_data, f, sort_keys=True, indent=4)

