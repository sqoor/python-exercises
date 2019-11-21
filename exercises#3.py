# 1
l1 = [1, 2, 3, 4, 5]
for item in l1:
    print(item)

# 2
print(sum(l1))

# 3
print(max(l1))

# 4
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
a = list(set(a))
print(a)

# 5
l5_1 = [1, 2, 3, 4, 5]
l5_2 = []
if print(len(l5_1) < 1):
    print('list is empty')
if print(len(l5_2) > 0):
    print('list is NOT empty')
if not a:
    print('list is empty')

# 6
t6 = 'a string', 1, True, [1, 2]
for item in t6:
    print(item)

# 7
num_set = set([0, 1, 2, 3, 4, 5])
for item in num_set:
    print(item)

# 8
set1 = (1, 2, 3, 4)
set2 = (2, 3, 4)
print(set1 or set2)

# 9
setx = set(['green', 'blue'])
sety = set(['blue', 'yellow'])
seta = setx | sety
print(seta)

# 10
seta = set([5, 10, 3, 15, 2, 20])
print(len(seta))


# 11
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
dic4 = {}
for d in (dic1, dic2, dic2):
    dic4.update(d)
print(dic4)

# 12
a = 'Hello, World!'
print(a[1])
print(a[2:5])
print(b[-5:-2])
print(len(a))
print(a.lower())
print(a.replace('H', 'J'))
