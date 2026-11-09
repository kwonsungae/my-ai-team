import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from main import greet


def test_greet(capsys):
    result = greet("world")
    assert "Hello world" in capsys.readouterr().out
