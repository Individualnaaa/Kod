# musi być aktywne środowisko venv: python -m venv .venv
# włączanie środowiska .\.venv\Scripts\activate.bat

from kalkulator import *

def test_dodawanie():
    # assert
    assert dodawanie(1, 1) == 2

def test_odejmowanie():
    assert odejmowanie(3, 1) == 2

# pytest testy_python\test_kalkulator.py::test_dodawanie - do terminala-> i wykonuje konkretny test


# parametryzacja
import pytest
@pytest.mark.wip
@pytest.mark.parametrize("podstawa, wykladnik, oczekiwany_wynik", [
    (2, 3, 8), # krotki tuples
    (10, 2, 100),
    (5, 3, 125)
])

def test_potegowanie(podstawa, wykladnik, oczekiwany_wynik):
    assert potegowanie(podstawa, wykladnik) == oczekiwany_wynik