import pytest
import requests 
# from api_client_employee_client import EmployeesClient

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



@pytest.fixture
def base_url():
    return "http://127.0.0.1:8000/api"

@pytest.fixture
def login_url(base_url):
    return f"{base_url}/login"

@pytest.fixture
def login_payload():
    return {
        'username': 'admin',
        'password': 'admin'
    }

@pytest.fixture
def auth_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

@pytest.fixture
def get_employees_url(base_url):
    return f"{base_url}/employees"


@pytest.fixture
def auth_headers(login_url, login_payload):
    login_response = requests.post(url=login_url, json=login_payload)
    access_token = login_response.json()['access_token']
    return {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_token}',
    }


@pytest.fixture
def post_payload():
    return {
    "name": "Kasia",
    "salary": 16547,
    "age": 22,
    "position": "Mid QA",
    "on_leave": False
    }
