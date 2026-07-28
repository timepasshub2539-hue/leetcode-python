def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(f"Success: {a}/{b}")
