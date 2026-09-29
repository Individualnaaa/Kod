from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.mark.logowanieUI
def test_logowanieUI():
    driver = webdriver.Chrome()
    # driver.implicity_wait(2) mamy czekać 2 sekundy aż coś się pojawi
    driver.get("http://127.0.0.1:8000")
    input("wpisz cokolwiek by wpisać hasło")

    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin")
    # driver.find_element(By.CSS_SELECTOR, "#loginForm > button").click() by selector
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/button').click()

    assert driver.find_element(By.ID, "form-title").is_displayed()

    input("wpisz cokolwiek by zamknąć kartę")