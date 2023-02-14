max_a = -1
min_a = 55

min_v = 0
max_v = 0

for a in range(1,55):
    n1 = 35*55**3 + a*55**2 + 34*55 +33
    n2 = 2*55**3 + 33*55**2 + a*55 + 34
    v = n1-n2

    if (v)%29 == 0:
        if a < min_a:
            min_a = a
            min_v = v
        if a > max_a:
            max_v = v
            max_a = a
print(max_v-min_v)
#86130