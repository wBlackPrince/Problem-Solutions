

for a in range(-10000,10000):
    a1 = a - 2
    b1 = -2*a
    c1 = 2*a - 3

    if a1 == 0:
        continue

    if c1/a1 > 0 and b1/a1 > 0:
        print(a)