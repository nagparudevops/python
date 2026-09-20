# def func_name():
#     print("Hello")

# func_name()

def calc(num1, num2, operator):
    if operator == "add":
        res = num1 + num2
    elif operator == "sub":
        res = num1 - num2
    elif operator == "mult":
        res = num1 * num2
    else:
        if num2 > num1:
            res = num1 / num2
        else:
            res = num2 / num1
    return res

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# operator = input("Enter the operation (Add/Sub/Mult/Div): ")
# operators_list = "add sub mult div".split()
# operator = operator.lower()
# if operator in operators_list:
#     res = calc(num1, num2, operator)
#     print(res)
# else:
#     print("Please check your inputs")

# Map
num1, num2 = map(int, input("Enter two numbers: ").split())
# num1, num2 = int(num1), int(num2)
# print(num1, num2, type(num1), type(num2))
operator = input("Enter the operation (Add/Sub/Mult/Div): ")
operators_list = "add sub mult div".split()
operator = operator.lower()
if operator in operators_list:
    res = calc(num1, num2, operator)
    print(res)
else:
    print("Please check your inputs")