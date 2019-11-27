import numpy as np
import matplotlib.pyplot as plt

# 1
print('one: -------------------------')
one_zeros = np.zeros(10, np.int)
print(one_zeros)

one_ones = np.ones(10, np.int)
print(one_ones)

one_fives = np.ones(10, np.int) * 5
print(one_fives)

# 2
print('\n\n\ntwo: -------------------------')
two = np.arange(30, 71)
print(two)

# 3
print('\n\n\nthree: -------------------------')
three = np.arange(30, 71, 2)
print(three)

# 4
print('\n\n\nfour: -------------------------')
four = np.arange(9).reshape(3, 3)
print(four)

# 5
print('\n\n\nfive: -------------------------')
rand_num = np.random.normal(0, 1, 1)
print(rand_num[0])

# 6
print('\n\n\nsix: -------------------------')
six = np.arange(12).reshape(3, 4)
print(six)

# 7
print('\n\n\nseven: -------------------------')
seven = np.arange(20)
seven[(seven > 8) & (seven < 16)] *= -1
print(seven)

# 8
print('\n\n\neight: -------------------------')
eight_x = np.array([1, 8, 3, 5])
eight_y = np.random.randint(0, 11, 4)
eight_z = eight_x * eight_y
print(eight_z)

# 9
print('\n\n\nnine: -------------------------')
nine = np.arange(6).reshape(2, 3)
print('nine:\n', nine)
print('"nine" array rows: ', nine.shape[0])
print('"nine" array columns: ', nine.shape[1])

# 10
print('\n\n\nten: -------------------------')
ten = np.arange(27).reshape(3, 3, 3)
print(ten)

# 11
print('\n\n\neleven: -------------------------')
a = np.array([9, -1, 2, 3])
b = np.array([1, -6, 0, 10])
c = np.array([[1, 8, 2, 5], [3, 1, 7, 9]])

print('a - b:', a - b)
print('a * b:', a * b)
print('a,dot(b):', a.dot(b))
print('a * 2:', a * 2)
print('np.sin(a):', np.sin(a))
print('a < 3:', a < 3)
print('a.sum(): ', a.sum())
print('a.sum(axis=0):', a.sum(axis=0))
print('c.sum():', c.sum())
print('c.sum(axis=0)', c.sum(axis=0))
print('a.min():', a.min())
print('a.mean():', a.mean())
print('a average(): ', np.average(a))
print('a median():', np.median(a))
print('a std(): ', np.std(a))
print('a var():', np.var(a))
print('c.cumsum():', c.cumsum())
print("a[1:2] : ", a[1:2])
print("a[2:] : ", a[2:])
print("c[-1] : ", c[-1])

# 12
print('\n\n\ntwelve: -------------------------')
x = np.arange(1, 50)
y = [value * 3 for value in x]
plt.plot(x, y)
plt.title('Draw a line .')
plt.ylabel('Y-axis')
plt.xlabel('X-axi')
plt.show()

# 13
print('\n\n\nthirteen: -------------------------')
x1 = [10, 20, 30]
x2 = [10, 20, 30]
plt.figure()
plt.plot(x1, [20, 40, 10], label="line1")
plt.plot(x2, [40, 10, 30], label="line2")
plt.title("Tow or more lines on same plot with suitable legends")
plt.legend(loc='upper right')
plt.show()

# 14
print('\n\n\nfourteen: -------------------------')
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
plt.show()

# 15
print('\n\n\nfifteen: -------------------------')

objects = ('Python', 'Java', 'PHP', 'JavaScript', 'C#', 'C++')
y_pos = np.arange(len(objects))
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.bar(y_pos, popularity, align='center', color=[
        'red', 'black', 'green', 'blue', 'yellow', 'blue'])
plt.xticks(y_pos, objects)
plt.ylabel('Popularity')
plt.title('Languages')
plt.show()
