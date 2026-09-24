import pytest

@pytest.fixture
def employee_fixture():
    employee = {
        "name": "Artur", 
        "age": 25
    }
    return employee 

@pytest.fixture(scope="session", autouse=True)
def start_sesji_testowej():
    print("\nRozpoczynam testy")
    yield
    print("\nKoniec testów")
