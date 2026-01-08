import pytest
import requests
import json

def main_url():
    return "https://reqres.in/"

def test_login():
    url = "https://reqres.in/api/login"
    data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    responce =requests.post(url,data)
    token=json.loads(responce.text)
    assert responce.status_code == 200
    assert token['token'] == "QpwL5tke4Pnpja7X4"