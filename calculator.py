# Simple Calculator

input1 = float(input("Enter the first number: "))
input2 = float(input("Enter the second number: "))
while True:
    operation = str(input("Enter '+' or '-' or 'x' or '/' "))
    
    if operation == "+":
        print(input1 + input2)
        break
    elif operation == "-":
        print(input1 - input2)
        break
    elif operation == "x":
        print(input1 * input2)
        break
    elif operation == "/":
        if input2 == 0:
            print("Division by zero is not allowed.")
            continue
        print(input1 / input2)
        break
    else:
        print('Invalid Input, please try again.')