from decimal import Decimal
from fair_share import calculate_balances


def main() -> None:
    example_expenses = {"Ruth": 150, "Yael": 50, "Shulamit": 100}
    balances: dict[str, Decimal] = calculate_balances(example_expenses)
    print(balances)


if __name__ == "__main__":
    main()
