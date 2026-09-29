from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pytest

@pytest.mark.dodanieui1
def test_dodanieui1(driver, employee_data, logowaniewUI):

    logowaniewUI()

    name_input = (By.ID, "name")
    salary_input = (By.ID, "salary")
    age_input = (By.ID, "age")
    position_select = (By.ID, "position")
    on_vacation_checkbox = (By.ID, "on_leave")
    add_btn = (By.ID, "submitBtn")

    ed = employee_data

    def fill_name_input(name: str):
        driver.find_element(*name_input).send_keys(name)

    def fill_age_input(age: int):
        driver.find_element(*age_input).send_keys(age)

    def fill_salary_input(salary: int):
        driver.find_element(*salary_input).send_keys(salary)

    def select_vacation_checkbox(on_leave):
        driver.find_element(*on_vacation_checkbox).click() if employee_data["on_leave"] else None

    def select_position(position):
        Select(driver.find_element(*position_select)).select_by_visible_text(position)

    def click_add_button():
        driver.find_element(*add.btn).click()


    def fill_all_inouts(name, salary, age, position, on_leave):
        fill_name_input(ed["name"])
        fill_age_input(ed["age"])
        fill_salary_input(ed["salary"])
        select_vacation_checkbox(ed["on_vacation"])
        select_position(ed["position"])
        click_add_button()

    employee_manager_page.fill_employee_name(employee_data["name"])
    # tds = driver.find_elements(By.TAG_NAME, "td")
    # print([td.text for td in tds])

    table_body = driver.find_element(By.ID, "employees")
    ostatni_wiersz_tabeli = table_body.find_elements(By.TAG_NAME, "tr")[-1]
    komorki_ostatniego_wiersza = ostatni_wiersz_tabeli.find_elements(By.TAG_NAME, "td")
    dane_ostatniego_wiersza = [element.text for element in komorki_ostatniego_wiersza][:-1]
    print(dane_ostatniego_wiersza)


    assert int(dane_ostatniego_wiersza[0]) > 0
    assert dane_ostatniego_wiersza[1] == ed["name"]


# przerobić na kod artura w test_dodaj_pracownnika.py

