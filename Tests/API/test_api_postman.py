import pytest


@pytest.mark.smoke
def test_post(postman_post_request):
    assert postman_post_request.status_code == 200


def test_post_response_message(postman_post_request):
    assert postman_post_request.json()["message"] == "You made a POST request with the following data!"


@pytest.mark.smoke
def test_get(postman_get_request):
    assert postman_get_request.status_code == 200


def test_get_response_message(postman_get_request):
    assert  postman_get_request.json()["message"] == "You made a GET request!"
