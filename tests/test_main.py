from fastapi.testclient import TestClient

from testbench_sardine import main

client = TestClient(main.app)


def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_get_pizza_size():
    response = client.get("/pizza-size", params={"diameter": 666})
    assert response.status_code == 200
    assert response.json() == {"area": 666}


def test_get_user_username_email_foo():
    response = client.get("/users/foo/email")
    assert response.status_code == 200
    assert response.json() == {"username": "foo", "email": "foo@example.com"}


def test_get_user_username_email_bar():
    response = client.get("/users/bar/email")
    assert response.status_code == 200
    assert response.json() == {"username": "bar", "email": "bar@example.com"}


def test_get_user_username_email_404():
    response = client.get("/users/fefefe/email")
    assert response.status_code == 404
