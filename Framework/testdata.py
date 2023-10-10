import os
import json
import requests
from dotenv import load_dotenv
from Framework.db_connector import DatabaseConnector


def create_test_data():
    """Берет информацию с сайта jsonplaceholer и записывает её в БД."""

    load_dotenv()
    resp = requests.get(os.getenv("TESTDATA_URL_SOURCE"))
    db = DatabaseConnector()
    db.insert_data(resp.text)


def _get_test_users():
    """Возвращает словарь с id пользователя, логином и паролем."""

    users = {}
    db = DatabaseConnector()
    db_data = db.select_testdata_by_id()
    list_users = json.loads(db_data)
    for i, user in enumerate(list_users):
        users[i+1] = {'login': user['email'], 'password': user['website']}
    return users


test_users = _get_test_users()
