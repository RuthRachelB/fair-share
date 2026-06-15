from collections.abc import Mapping
from decimal import Decimal


def calculate_balances(expenses: Mapping[str, int | float]) -> dict[str, float]:
    if not expenses:
        return {}
    for person, paid_amount in expenses.items():
        if isinstance(paid_amount, bool) or not isinstance(paid_amount, (int, float)):
            raise TypeError(f"Expense for {person} must be numeric")
        if paid_amount < 0:
            raise ValueError(f"Expense for {person} cannot be negative")
    total_expenses = sum(Decimal(str(amount)) for amount in expenses.values())
    num_people = len(expenses)
    fair_share = total_expenses / Decimal(str(num_people))

    balances = {}
    for person, paid_amount in expenses.items():
        balances[person] = float(
            (Decimal(str(paid_amount)) - fair_share).quantize(Decimal("0.01"))
        )

    return balances
