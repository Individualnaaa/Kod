import pytest

@pytest.fixture
def employee_fixture():
    employee = {
        "name": "Artur", 
        "age": 25
    }
    return employee 