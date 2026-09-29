from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pytest

@pytest.mark.logowanieUI2
def test_logowanieUI2():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.get("http://127.0.0.1:8000")

    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    

    assert driver.find_element(By.ID, "form-title").is_displayed()
    Select(driver.find_element(By.ID, "position")).select_by_visible_text("Junior QA")

