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

# @pytest.mark.test_imienia
# def test_imie_michal(imie):
#     print(imie)
#     assert imie == "Michal"

    # zgłębić ten mark 

