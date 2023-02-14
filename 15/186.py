def f(a):
    for x in range(1,100):
        if (((x&55)==0) or (x&10 != 0) or (x&a!=0)):
            continue
        else:
            return False
    return True

for a in range(1,10000):
    if f(a):
        print(a)
        break
#53