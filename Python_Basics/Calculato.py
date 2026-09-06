# Here we make a simple calculator using python 

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operator = input("Enter operator(+, -, *, /, %): ")

if operator == "+":
   print("the sum of ", number1, "and", number2, "is", number1 + number2)
elif operator == "-":
   print("the difference of ", number1, "and", number2, "is", number1 - number2)
elif operator == "*":
   print("the product of ", number1, "and", number2, "is", number1 * number2)
elif operator == "/":
   print("the quotient of ", number1, "and", number2, "is", number1 / number2)
elif operator == "%":
   print("the remainder of ", number1, "and", number2, "is", number1 % number2)
else:
   print("Invalid operator")