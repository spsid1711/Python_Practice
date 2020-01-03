num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# You can use input() in python 3 and it will work.
# Using python 2, you must use raw_input to prevent EOF error.
op = raw_input("Enter the operator: ")

result = 0.0
if op == "+":
    result = num1 + num2
    print(result)
elif op == "-":
    result = num1 - num2
    print(result)
elif op == "*":
    result = num1 * num2
    print(result)
elif op == "/":
    result = num1 / num2
    print(result)
elif op == "%":
    result = num1 % num2
    print(result)
else:
    print("Invalid Operator! Please re-run the program and try again.")