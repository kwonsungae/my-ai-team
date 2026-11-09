import os
import sys

import jwt
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from auth.jwt_auth import login, current_user, ALGORITHM
from auth.middleware import check_request

SECRET = "test-secret"


@pytest.fixture(autouse=True)
def jwt_secret(monkeypatch):
    monkeypatch.setenv("JWT_SECRET", SECRET)


def test_login():
    token = login("alice")
    assert current_user(token) == "alice"


def test_expired_token_rejected():
    token = login("alice", expires_in=-10)
    assert current_user(token) is None


def test_tampered_token_rejected():
    token = login("alice")
    forged = jwt.encode({"sub": "mallory", "exp": 9999999999}, "other-secret", algorithm=ALGORITHM)
    assert current_user(forged) is None
    assert current_user(token + "x") is None


def test_none_and_empty_token():
    assert current_user(None) is None
    assert current_user("") is None
    assert current_user("not-a-jwt") is None


def test_missing_secret_raises(monkeypatch):
    monkeypatch.delenv("JWT_SECRET")
    with pytest.raises(RuntimeError):
        login("alice")


def test_check_request_bearer():
    token = login("alice")
    assert check_request({"Authorization": f"Bearer {token}"}) == "alice"


def test_check_request_non_bearer_rejected():
    token = login("alice")
    assert check_request({"Authorization": f"Basic {token}"}) is None
    assert check_request({}) is None
