# Function definition

def CalSum(a, b):
    return a + b


# Function call
sum_result = CalSum(1, 3)
print("Sum:", sum_result)
CalSum(25, 6)
CalSum(45, 7)
CalSum(5, 9)
CalSum(5, 6)
CalSum(2, 6)
CalSum(25, 6)
CalSum(25, 60)


def average(c, d, e):
    sum1 = c + d + e
    avg = sum1 / 3
    print("The average is:", avg)
    return sum1


average(3, 4, 5)


try:
    c = int(input("Enter first number: "))
    d = int(input("Enter second number: "))
    op = input("Enter Operator (+, -, *, /): ")

    if op == "+":
        print("+ operator is used:", c + d)
    elif op == "-":
        print("- operator is used:", c - d)
    elif op == "*":
        print("* operator is used:", c * d)
    elif op == "/":
        if d != 0:
            print("/ operator is used:", c / d)
        else:
            print("0 / The input is wrong.")
    else:
        print("Invalid operator.")

except ValueError:
    print("Invalid input. Please enter numeric values.")
finally:
    print("In this code no error found.")


try:
    f = open("demofile.txt", "w")
    try:
        f.write("Lorum Ipsum")
    except Exception:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except Exception:
    print("Something went wrong when opening the file")