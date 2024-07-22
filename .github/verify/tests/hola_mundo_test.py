import sys
import os
import pytest

# Add the parent directory of hola_mundo.py to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

from hola_mundo import hola_mundo

def test_hola_mundo(capsys):
    result = hola_mundo()
    captured = capsys.readouterr()
    assert captured.out == "Hola Mundo!!!\n"
    assert result is None
