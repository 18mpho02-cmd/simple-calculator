def simple_calculator():
    try:
        # 1. Ask for two numbers
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))

        # 2. Ask for an operation
        print("choose an operation: +, -, *, /")
        op = input("Enter operation: ")

        # 3. Perform the operation and print the result
        if op == '+':
            print("Answer:", first + second)
        elif op == '-':
            print("Answer:", first - second)
        elif op == '*':
            print("Answer:", first * second)
        elif op == '/':
            if second != 0:
                print("Answer:", first / second)
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation")
    except ValueError:
        print("Error: Please enter valid numbers only,not text.")

# 4. Run the calculator function
simple_calculator()