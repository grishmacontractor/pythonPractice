# -------------------------functions
def fibo(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a
for c in range(0, 13):
    print (c+1, end='|\t')
print('\n----------------------------------------------------')

for c in range(0, 13):
    print(fibo(c), end='|\t')


def karlos():
    return 1, 2, 3

a, b, c = karlos()
print("\n----------------------")
print(a)
print(b)
print(c)