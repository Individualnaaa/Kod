# from przyklad import duze_imiona


# def fixture_z_lista_imion():
#     testowana_lista = ["Anna", "tomek"]
#     return testowana_lista


# def test_duze_imiona(lista_imion):
#     testowana_lista = lista_imion
#     oczekiwana_lista = ["ANNA", "MAREK"]
#     assert duze_imiona(testowana_lista) == (oczekiwana_lista)
#     # wziąć z zajęć bo coś nie działa


# w conftest jest fixture dla tej funkcji
def test_name_employee(employee_fixture):
    employee = employee_fixture
    assert employee["name"] == "Artur"

def test_name_employee(employee_fixture):
    employee = employee_fixture
    assert employee["age"] == 25

import pytest

# pytest testy_python\test_kalkulator.py::test_dodawanie - do terminala-> i wykonuje konkretny test

import logging
logger = logging.getLogger(__name__)

@pytest.mark.xfail(reason="to celowy błąd")
def test_imie_michal(employee_fixture):
    print(employee_fixture["name"])
    logger.warning("jestem warningiem")
    logger.error("jestem errore")
    logger.debug("debug")
    logger.critical("critical")
    assert employee_fixture["name"] == "Michal"

@pytest.mark.test_imienia
def test_imie_michal2(employee_fixture):
    print(employee_fixture["name"])
    logger.warning("jestem warningiem")
    logger.error("jestem errore")
    logger.debug("debug")
    logger.critical("critical")
    assert employee_fixture["name"] == "Michal"

@pytest.mark.skip(reason="nope skip")
def test_imie_michal3(employee_fixture):
    print(employee_fixture["name"])
    logger.warning("jestem warningiem")
    logger.error("jestem errore")
    logger.debug("debug")
    logger.critical("critical")
    assert employee_fixture["name"] == "Michal"



#logger?