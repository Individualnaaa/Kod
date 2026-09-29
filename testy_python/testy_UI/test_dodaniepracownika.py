from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pytest

@pytest.mark.dodanieui
def test_dodanieui():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.get("http://127.0.0.1:8000")

    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

    assert driver.find_element(By.ID, "form-title").is_displayed()


    driver.find_element(By.ID, "name").send_keys("Rocket")
    driver.find_element(By.ID, "age").send_keys("19")
    driver.find_element(By.ID, "salary").send_keys("100000")
    driver.find_element(By.ID, "on_leave").click() if employee_data["on_leave"] else None
    Select(driver.find_element(By.ID, "position")).select_by_visible_text("Junior QA")
    driver.find_element(By.ID, "submitBtn").click()

    # tds = driver.find_elements(By.TAG_NAME, "td")
    # print([td.text for td in tds])

    table_body = driver.find_element(By.ID, "employees")
    table_rows = table_body.find_elements(By.TAG_NAME, "tr")
    ostatni_wiersz_tabeli = table_rows[-1]
    komorki_ostatniego_wiersza = ostatni_wiersz_tabeli.find_elements(By.TAG_NAME, "td")
    print(komorki_ostatniego_wiersza)
    dane_ostatniego_wiersza = [element.text for element in komorki_ostatniego_wiersza][:-1]
    print(dane_ostatniego_wiersza)

    assert dane_ostatniego_wiersza[1] == "Rocket"




