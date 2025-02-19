a = int(input("Enter first number : "))
c = input("Enter Sign :")
b = int(input("Enter second number : "))
if c == "+":
    print(f"{a} + {b} = {a+b}")
elif c == "-":
    print(f"{a} - {b} = {a-b}")
elif c == "*":
    print(f"{a} * {b} = {a*b}")
elif c == '/' and b != 0:
    print(f"{a} / {b} = {a/b}")
else:
    print("Invalid Operation")