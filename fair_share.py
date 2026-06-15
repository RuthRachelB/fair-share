from collections.abc import Mapping
from decimal import Decimal


def _validate_expenses(expenses: Mapping[str, int | float | Decimal]) -> None:
    for person, paid_amount in expenses.items():
        if isinstance(paid_amount, bool) or not isinstance(
            paid_amount, (int, float, Decimal)
        ):
            raise TypeError(f"Expense for {person} must be numeric")
        if paid_amount < 0:
            raise ValueError(f"Expense for {person} cannot be negative")


def calculate_balances(
    expenses: Mapping[str, int | float | Decimal],
) -> dict[str, Decimal]:
    if not expenses:
        return {}

    _validate_expenses(expenses)

    total_expenses = sum(Decimal(str(amount)) for amount in expenses.values())
    num_people = len(expenses)
    fair_share = total_expenses / Decimal(str(num_people))

    balances: dict[str, Decimal] = {}
    for person, paid_amount in expenses.items():
        precise_balance = Decimal(str(paid_amount)) - fair_share
        balances[person] = precise_balance.quantize(Decimal("0.01"))

    return balances
