import argparse
from calculator import Calculator

def main():
    """The entry point of the application."""
    parser = argparse.ArgumentParser(description="A simple calculator.")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"])
    parser.add_argument("x", type=float)
    parser.add_argument("y", type=float)
    args = parser.parse_args()

    calculator = Calculator()

    if args.operation == "add":
        result = calculator.add(args.x, args.y)
    elif args.operation == "subtract":
        result = calculator.subtract(args.x, args.y)
    elif args.operation == "multiply":
        result = calculator.multiply(args.x, args.y)
    elif args.operation == "divide":
        result = calculator.divide(args.x, args.y)

    print(result)

if __name__ == "__main__":
    main()
