"""CLI calculator supporting add, subtract, multiply, and divide."""

import argparse


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


OPERATIONS: dict[str, callable] = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


def build_parser() -> argparse.ArgumentParser:
    """Build and return the CLI argument parser."""
    parser = argparse.ArgumentParser(
        description="CLI calculator: add, subtract, multiply, divide."
    )
    parser.add_argument(
        "operation",
        choices=OPERATIONS.keys(),
        help="The operation to perform.",
    )
    parser.add_argument("a", type=float, help="First operand.")
    parser.add_argument("b", type=float, help="Second operand.")
    return parser


def main() -> None:
    """Parse arguments and execute the requested calculation."""
    parser = build_parser()
    args = parser.parse_args()
    try:
        result = OPERATIONS[args.operation](args.a, args.b)
        print(result)
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
