while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Select an operation:")
    print(" +  Addition")
    print(" -  Subtraction")
    print(" *  Multiplication")
    print(" /  Division")
    print(" q  Quit")

    operation = input("Enter the operation (+, -, *, /, q): ")

    if operation == "q":
        print("Exiting calculator.")
        break
    elif operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        print("Invalid operation.")
        continue

    print("Result:", result)
