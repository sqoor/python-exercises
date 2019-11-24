# Day #4 Exercises:

from functools import reduce


# 1
def one():
    o = lambda x=1, y=2, z=3: x + y + z
    print(o())
    print(o(10))
    print(o(10, 20))


# 2
def two():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nums_multiplied = reduce(lambda a, b: a * b, nums)
    print(nums_multiplied)


# 3
def three():
    result = lambda num1, num2: num1 * num2
    print(result(2, 2))


# 4

def four():
    less_than_zero = lambda num: num < 0
    numbers_list = range(-5, 5)
    negative_numbers = list(filter(less_than_zero, numbers_list))
    print(negative_numbers)


# 5
def five():
    x = lambda a, b, c: a + b + c
    print(x(5, 6, 2))  # 13


# 6
def six():
    x = ('Joey', 'Monica', 'Ross')
    y = ('Chandler', 'Pheobe')
    z = ('David', 'Rachel', 'Courtney')
    result = list(zip(z, y, z))
    print(result)  # [('David', 'Chandler', 'David'), ('Rachel', 'Pheobe', 'Rachel')]


# 7
def seven():
    coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
    code = ('BTC', 'ETH', 'XRP', 'LTC')
    d = dict(zip(coin, code))
    print(d)  # {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}


# 8
# function that filters vowels
def eight():
    def fun(variable):
        letters = ['a', 'e', 'i', 'o', 'u']
        if variable in letters:
            return True
        else:
            return False

    sequence = ['g', 'j', 'e', 'j', 'k', 'o', 'p' 'r']
    filtered = list(filter(fun, sequence))
    print(filtered)  # ['e', 'o']


# 9
def nine():
    x = list(map(int, input('Enter a multiple value:').split()))
    print('List of students: ', x)  # [1, 2, 3, 4] assuming the input is 1 2 3 4


# 10
def ten():
    def newfunc(a):
        return a * a

    x = list(map(newfunc, (1, 2, 3, 4)))
    print(x)  # [1, 4, 9, 16]


# 11
def eleven():
    def func(a, b):
        return a + b

    a = list(map(func, [2, 4, 5], [1, 2, 3, 2, 4]))
    print(a)  # [3, 6, 8]


# 12
def twelve():
    c = map(lambda x: x + x, filter(lambda x: (x >= 3), (1, 2, 3, 4, 5)))
    print(list(c))  # [6, 8, 10]


# 13
def thirteen():
    c = filter(lambda x: (x >= 3), map(lambda x: x + x, (1, 2, 3, 4)))
    print(list(c))  # [4, 6, 8]


# 14
def fourteen():
    nums = [1, 2, 3, 4, 9, 0, -1, -5, 11, -50]
    min_value = reduce(lambda a, b: a if a < b else b, nums)
    print(min_value)


# 15
def fifteen():
    numbers = [1, 2, 3]
    letters = ['a', 'b', 'c']
    result = tuple(zip(numbers, letters))
    print(result)


