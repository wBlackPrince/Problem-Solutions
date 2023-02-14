def f(a):
    for x in range(1,10000):
        if ((x%40!=0) and (x%64!=0)) or (x%a==0):
            continue
        else:
            return False
    return True

for a in range(1,1000):
    if f(a):
        print(a)

#8