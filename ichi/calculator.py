#I want to create a simple calculator that can perform basic arithmetic operations
#  like addition, subtraction, multiplication, division, and modulus.
#  The user will input two numbers and the desired operation, and the calculator will return the result.
# I want to make it such that the user can choose to use calculator again or exit the program after each calculation.


def calculate(x, y, operation):
    if operation == "+":
        return float(x) + float(y)
    elif operation == "-":
        return int(x) - int(y)
    elif operation == "*":
        return float(x) * float(y)
    elif operation == "/":
        return float(x) / float(y)
    elif operation == "%":
        return float(x) % float(y)
    else:
            return "Invalid operation"

M = input(" X or C : ")
while M == "C":
    # Use it
    x = input("Enter 1st num: ")
    y = input("Enter 2nd num: ")
    operation = input("Enter the operation (+,-,/,*,%): ")
    print("Result:", calculate(x, y, operation))
    M = input(" X or C : ")

else:
    print("Exiting the calculator. Goodbye!")




