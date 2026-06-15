import pytest
from fair_share import calculate_balances


def test_empty_expenses():
    assert calculate_balances({}) == {}


def test_equal_split():
    expenses = {"Ruth": 100, "Yael": 100, "Shulamit": 100}
    expected_balances = {"Ruth": 0.0, "Yael": 0.0, "Shulamit": 0.0}
    assert calculate_balances(expenses) == expected_balances


def test_one_person_paid_all():
    expenses = {"Ruth": 300, "Yael": 0, "Shulamit": 0}
    expected_balances = {"Ruth": 200.0, "Yael": -100.0, "Shulamit": -100.0}
    assert calculate_balances(expenses) == expected_balances


def test_different_expenses():
    expenses = {"Ruth": 150, "Yael": 50, "Shulamit": 100}
    expected_balances = {"Ruth": 50.0, "Yael": -50.0, "Shulamit": 0.0}
    assert calculate_balances(expenses) == expected_balances


def test_decimal_expenses():
    expenses = {"Ruth": 123.45, "Yael": 67.89, "shulamit": 90.12}
    expected_balances = {"Ruth": 29.63, "Yael": -25.93, "shulamit": -3.7}
    assert calculate_balances(expenses) == expected_balances


def test_rejects_non_numeric_expense():
    with pytest.raises(TypeError):
        calculate_balances({"Ruth": "100", "Yael": 50})  # type: ignore


def test_rejects_negative_expense():
    with pytest.raises(ValueError):
        calculate_balances({"Ruth": -10, "Yael": 50})
