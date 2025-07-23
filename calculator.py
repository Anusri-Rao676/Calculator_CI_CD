# calculator.py
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else 'Cannot divide by zero'

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <add|sub|mul|div> num1 num2")
        sys.exit(1)

    op = sys.argv[1]
    x = float(sys.argv[2])
    y = float(sys.argv[3])

    if op == "add":
        print(add(x, y))
    elif op == "sub":
        print(subtract(x, y))
    elif op == "mul":
        print(multiply(x, y))
    elif op == "div":
        print(divide(x, y))
    else:
        print("Unknown operation.")
