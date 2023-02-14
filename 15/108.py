p = [i for i in range(15,40)]
q = [i for i in range(44,57)]

def f(a,p,q):
    for x in range(1000):
        if x not in a or x in p or x in q:
            continue
        else:
            return False
    return True

mas = []
for x1 in range(1,50):
    for x2 in range(x1+1,x1+50):
        a = [i for i in range(x1,x2)]
        if f(a,p,q):
            mas.append(a[-1]-a[0])
print(max(mas))