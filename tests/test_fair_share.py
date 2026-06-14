from fair_share import calculate_balances

#test 1- empty expences dictionary
def test_empty_expenses():
    assert calculate_balances({}) == {}

#test 2- equal expenses 
def test_equal_split():
    expenses = {"Ruth":100, "Yael": 100, "shulamit":100} 
    expected_balances = {"Ruth": 0.0, "Yael": 0.0, "shulamit": 0.0}
    assert calculate_balances(expenses) == expected_balances

#test 3- one person paid all the expenses
def test_one_person_paid_all():
    expenses = {"Ruth":300, "Yael": 0, "shulamit":0} 
    expected_balances = {"Ruth": 200.0, "Yael": -100.0, "shulamit": -100.0}
    assert calculate_balances(expenses) == expected_balances 

#test 4- different expenses
def test_different_expenses():
    expenses = {"Ruth":150, "Yael": 50, "shulamit":100} 
    expected_balances = {"Ruth": 50.0, "Yael": -50.0, "shulamit": 0.0}
    assert calculate_balances(expenses) == expected_balances

#test 5- expenses with decimal values
def test_decimal_expenses():
    expenses = {"Ruth": 123.45, "Yael": 67.89, "shulamit": 90.12}
    expected_balances = {"Ruth": 18.44, "Yael": -37.12, "shulamit": 18.68}
    assert calculate_balances(expenses) == expected_balances


#test 6- zero expenses
def test_zero_expenses():
    expenses = {"Ruth": 0, "Yael": 0, "shulamit": 0}
    expected_balances = {"Ruth": 0.0, "Yael": 0.0, "shulamit": 0.0}
    assert calculate_balances(expenses) == expected_balances
