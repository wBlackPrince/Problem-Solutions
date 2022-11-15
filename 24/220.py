with open("24data/24-215.txt") as f:
    a = f.read()

s = ""
for i in range(len(a)):
    if i < 2 or i > len(a)-2:
        s += a[i]
        continue
    elif a[i-1] in "123" and a[i] in "ABC" and a[i+1] in "123" and a[i-2] in "ABC" and a[i+2] in "ABC":
        s += a[i]*3
    else:
        s += a[i]

a = s
c = 0
count = 0
maxi = 0

for i in range(len(a)-2):
    if c > 0:
        c-=1
        continue
    if (a[i] in "ABC" and a[i+1] in "123" and a[i+2] in "ABC"):
        count += 1
        c = 2
    else:
        maxi = count if maxi < count else maxi
        count = 0
maxi = count if maxi < count else maxi

print(maxi)

#TODO  пока 4