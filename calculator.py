a = input('Enter first number: ')
operator = input('Enter operator(+, -, *, /, %): ')
b = input('Enter second number: ')
a = int(a)
b = int(b)

if operator == '+':
    print(a+b)
elif operator == '-':
    print(a-b)
elif operator == '*':
    print(a*b)
elif operator == '/':
    print(a/b)
elif operator == '%':
    print(a%b)
else:
    print('Invalid Operation')
    