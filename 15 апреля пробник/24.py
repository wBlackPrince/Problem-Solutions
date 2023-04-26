f = open('24.txt')
n=f.read()
n=n.replace('AB','x')
n=n.replace('CB','x')
k=0
m=0
for i in range(len(n)):
    if n[i]=='x':
        k+=1
        m=max(m,k)
    else:
        k=0
print(m)