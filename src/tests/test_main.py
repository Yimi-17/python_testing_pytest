import pytest
from src.main import sum, siesmayor, login, resta, siesmenor


def test_sum():
    assert sum(2, 6) == 8

def test_sum1():
    assert sum(4, 6) == 10

def test_resta():
    assert resta(1220, 109) == 1111

def testsiesmayor():
    assert siesmayor(3, 2)

def testsiesmenor():
    assert siesmenor(1, 8)

#Decorador con valores a añadir en el parametrizador
@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (5, 1, 6),
        (6, sum(4, 2), 12),
        (sum(19, 1), 15, 35),
        (-7, 10, sum(-7, 10))
    ]
)

#Funcion con entradas y valor esperado
def test_sum_params(input_x, input_y, expected):
    assert sum(input_x, input_y) == expected


def test_login_pass():
    login_passes = login("yimicr", "123456")
    assert login_passes

#Funcion que corrobora que el valor es negativo
def test_login_fail():
    login_fails = login("yimicrXD", "12345678")
    assert not login_fails