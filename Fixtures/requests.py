import pytest
import requests


@pytest.fixture(scope="session")
def postman_post_request():
    url = "https://postman-rest-api-learner.glitch.me//info"
    payload = {"name": "Add your name in the body"}
    response = requests.request("POST", url, json=payload)
    yield response


@pytest.fixture(scope="session")
def postman_get_request():
    url = "https://postman-rest-api-learner.glitch.me//info?id=1"
    payload = {}
    response = requests.request("GET", url, json=payload)
    yield response
