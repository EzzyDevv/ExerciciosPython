a = [2, 3, 4, 5, 6]
b = a
b[2] = 9
print('Lista A {}'.format(a))
print('Lista B {}'.format(b))

print('+++++++++++++++++++++++++++++')

c = [1, 2, 3, 4, 5]
d = c[:]
d[2] = 9
print('Lista C {}'.format(c))
print('Lista D {}'.format(d))