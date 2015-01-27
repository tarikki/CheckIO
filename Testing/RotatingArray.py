__author__ = 'extradikke'

a = [x for x in range(0, 3)]

for i in range(0, 10):
    print(a[i % 3], a[(i + 1) % 3], a[(i + 2) % 3])