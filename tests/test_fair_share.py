from decimal import Decimal
import pytest
from fair_share import calculate_balances


def test_empty_expenses():
    assert calculate_balances({}) == {}


def test_equal_split():
    expenses = {"Ruth": 100, "Yael": 100, "Shulamit": 100}
    expected_balances = {
        "Ruth": Decimal("0.00"),
        "Yael": Decimal("0.00"),
        "Shulamit": Decimal("0.00"),
    }
    assert calculate_balances(expenses) == expected_balances


def test_one_person_paid_all():
    expenses = {"Ruth": 300, "Yael": 0, "Shulamit": 0}
    expected_balances = {
        "Ruth": Decimal("200.00"),
        "Yael": Decimal("-100.00"),
        "Shulamit": Decimal("-100.00"),
    }
    assert calculate_balances(expenses) == expected_balances


def test_different_expenses():
    expenses = {"Ruth": 150, "Yael": 50, "Shulamit": 100}
    expected_balances = {
        "Ruth": Decimal("50.00"),
        "Yael": Decimal("-50.00"),
        "Shulamit": Decimal("0.00"),
    }
    assert calculate_balances(expenses) == expected_balances


def test_decimal_expenses():
    expenses = {"Ruth": 123.45, "Yael": 67.89, "Shulamit": 90.12}
    expected_balances = {
        "Ruth": Decimal("29.63"),
        "Yael": Decimal("-25.93"),
        "Shulamit": Decimal("-3.70"),
    }
    assert calculate_balances(expenses) == expected_balances


def test_rejects_non_numeric_expense():
    with pytest.raises(TypeError):
        calculate_balances({"Ruth": "100", "Yael": 50})  # type: ignore


def test_rejects_negative_expense():
    with pytest.raises(ValueError):
        calculate_balances({"Ruth": -10, "Yael": 50})


def test_rejects_boolean_expense():
    with pytest.raises(TypeError):
        calculate_balances({"Ruth": True, "Yael": 50})
