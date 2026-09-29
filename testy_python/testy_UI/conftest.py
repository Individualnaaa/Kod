from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("http://127.0.0.1:8000")
    yield driver
    driver.quit()

@pytest.fixture
def logowaniewUI():
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    assert driver.find_element(By.ID, "form-title").is_displayed()

@pytest.fixture
def employee_data():
    return {
        "name":"Basia",
        "salary": 1889,
        "age": 30,
        "on_leave": True,
        "position": "Junior QA"
    }