def calculator(x,y,z):
    if z == '+':
        return x + y
    elif z == '-':
        return x - y
    elif z == '*':
        return x * y
    elif z == '/':
        return x/y
x = input("Enter number: ")
x = int(x)
y = input("Enter another number: ")
y = int(y)
z = input("Enter the sign(+,-,*,/): ")
print(calculator(x,y,z))
