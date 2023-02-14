def f(a):
    for x in range(1,100):
        if ((x%a !=0) and (x%15==0)) <= ((x%18 != 0) or (x%15 != 0)):
            continue
        else:
            return False
    return True

for a in range(1,10000):
    if f(a):
        print(a)

#90