# These are the diff - diff code of making two python calculators
# ================ Calculator1 ================
# Take input from the user
num1 = float(input("Enter first number:\n "))
num2 = float(input("Enter second number:\n "))
operator = input("Enter operator { +, -, *, / }:\n ")

# Perform calculation based on the operator
if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    result = num1 - num2
    print("Result:", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":
                    # Check that the second number is not zero
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Invalid operator.")



# ============== Calculator2 ================

# Take input from the user
num1 = float(input("Calculator2 --> Enter First Number:\n "))
num2 = float(input("Enter Second Number:\n "))
operator = input("Enter Operator { +, -, *, / }: ")


# Perform calculation based on the operator
if (operator == "+"):
    print(" Addition is performed. ", num1 + num2)

elif (operator == "-"):
    print(" Subtraction is performed. ", num1 - num2)

elif (operator == "*"):
    print(" Multiplication is performed. ", num1 * num2)

elif (operator == "/"):
                     # Check that the second number is not zero
    if num2 != 0:
        print(" Division is performed ", num1 / num2)
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid operator.")