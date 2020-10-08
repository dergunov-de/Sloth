'''
Занятие 2

i = 10
name = 'Home'
print(type(name))

print(2 + 1 / 4 * 5)
f1 = int(input('Введите число'))
f2 = int(input('Введите число'))

print(f1 + f2)
'''
name1 = 10
name2 = 20

# Условные операторы
if name1 == name2:
    print('name1 == name2')
if name1 > name2:
    print('name1 > name2')
    if name2 is True:
        print("True")
if name1 >= name2:
    pass
elif name1 < name2:
    print('name1 < name2')
elif name1 != name2:
    pass
else:
    print('name1 = name2')

# Список [], Кортедж ()
n = [1, 2, 3, 'sorry']
print(n[0])
print(len(n))
n.append(7)
print(n)
# Циклы
for i in 'sorry':
    print(i)
# for i in n:
for i in 1, 2, 3, 'sorry':
    print(i)

m = 0
# while True
while m < 10:
    print(m)
    m += 1
