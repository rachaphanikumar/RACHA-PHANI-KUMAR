class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def calculate(self, a: float, b: float, operation: str) -> float:
        if operation == '+':
            return self.add(a, b)
        elif operation == '-':
            return self.subtract(a, b)
        elif operation == '*':
            return self.multiply(a, b)
        elif operation == '/':
            return self.divide(a, b)
        else:
            raise ValueError(f"Invalid operation: {operation}")

# output
if __name__ == "__main__":
    calc = Calculator()

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        result = calc.calculate(a, b, operation)
        print(f"Result: {result}")
    except ValueError as e:
        print("Error:", e)
