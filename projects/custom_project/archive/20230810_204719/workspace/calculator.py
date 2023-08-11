class Calculator:
    """A simple calculator."""

    @staticmethod
    def add(x, y):
        """Add two numbers."""
        return x + y

    @staticmethod
    def subtract(x, y):
        """Subtract y from x."""
        return x - y

    @staticmethod
    def multiply(x, y):
        """Multiply two numbers."""
        return x * y

    @staticmethod
    def divide(x, y):
        """Divide x by y."""
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
