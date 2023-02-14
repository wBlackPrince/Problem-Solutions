p = [i for i in range(22,36)]
q = [i for i in range(15,31)]

def f(a,p,q):
    for x in range(1,100):
        if x in p and x not in q and x in a:
            continue
        else:
            return False
    return True

mas = []
for x1 in range(10,100):
    for x2 in range(x1+2,x1+101):
        a = [i for i in range(x1,x2)]
        if f(a,p,q):
            mas.append(a[-1]-a[0])
print(min(mas))