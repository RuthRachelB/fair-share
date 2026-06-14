from collections.abc import Mapping
def calculate_balances(expenses: Mapping[str,int | float]) -> dict[str, float]:
    if not expenses:
        return {}

    total_expenses = sum(expenses.values())
    num_people = len(expenses)
    fair_share = total_expenses / num_people

    balances = {}
    for person, paid_amount in expenses.items():
        balances[person] = round(paid_amount - fair_share, 2)
    return balances
