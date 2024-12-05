def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")
    
    if operation not in ['1', '2', '3', '4']:
        print("Invalid operation. Please restart the program and choose a valid operation.")
        return
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    if operation == '1':
        result = num1 + num2
        operation_symbol = '+'
    elif operation == '2':
        result = num1 - num2
        operation_symbol = '-'
    elif operation == '3':
        result = num1 * num2
        operation_symbol = '*'
    elif operation == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        operation_symbol = '/'
    
    print(f"The result of {num1} {operation_symbol} {num2} is: {result}")

calculator()