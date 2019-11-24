# Exercises day #2

# 1
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 < num2:
    print(num1, num1)
else:
    print(num2, num1)

# 2
num = int(input('Enter a number: '))

for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')

# 3
for x in range(10):
    for y in range(x):
        print('*', end='')
    print()
for x in range(1, 11):
    # print(x)
    for y in range(10 - x):
        print('*', end='')
    for z in range(x):
        print(' ', end='')
    print()

# 4
letters = ['x', 'y', 'z', 'a', 'b', 'c']
for i in letters:
    if i == 'a':
        continue
    elif i == 'c':
        break
    print(i)

# 5
for x in range(12, 25, 3):
    print(x)

# 6
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# 7
num = int(input('Enter a number: '))
sum = 0

for i in range(1, num + 1):
    sum += i

print(f'Sum = {sum}')

# 8
num8 = int(input('Enter a number: '))
if num8 % 2 == 0:
    print(f'{num8} is even')
else:
    print(f'{num8} is odd')

# 9
for x in range(10):
    n = 1
    for j in range(9 - x):
        print(' ', end='  ')
    for j in range(x - 1):
        print(n, end='  ')
        n += 1
    for j in range(x):
        print(x - j, end='  ')
    print('')

for x in range(10):
    n = 1
    for j in range(x + 1):
        print(' ', end='  ')
    for j in range((8 - x)):
        print(f'{n}', end='  ')
        n += 1
    for j in range(7 - x, 0, -1):
        print(j, end='  ')
    print('')


    # 10

while True:
    try:
        num10 = int(input('Enter a number: '))
        print(f'exercise # 10 number: {num10}')
        break;

    except ValueError:
        print('You\'ve passed a wrong entry, try again...')


    # 11
try:
    a = 3
    if a < 4:
        b = a / (a - 3)
    print('Value of b = ', b)
except(ZeroDivisionError, NameError):
    print('\nError Occurred and Handled')
