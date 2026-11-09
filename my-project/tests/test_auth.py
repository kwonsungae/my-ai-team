import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from auth.session import login, current_user

def test_login():
    sid = login("alice")
    assert current_user(sid) == "alice"
