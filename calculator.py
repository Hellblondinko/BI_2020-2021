a = float(input())
c = input()
b = float(input())

if c == '+':
    print (a + b)
elif c == '-':
    print (a - b)
elif c == '*':
    print (a * b)
elif c == 'pow':
    print(a ** b)
elif b == 0:
    print('Деление на 0!')

elif c == 'div' and b !=0:
    print(a // b)
elif c == '/' and b !=0:
    print(a / b)
print('Возвращайся скорей и давай считать!')
