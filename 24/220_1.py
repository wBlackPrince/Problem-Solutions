#with open("24data/24-215.txt") as f:
    #a = f.read()

c = 0
count = 0
maxi = 0
a = "A1BC2AA1B"
f = False

for i in range(len(a)-2):
    if c != 0:
        c -= 1
        continue
    elif (a[i] in "ABC" and a[i+1] in "123" and f):
        count += 1
        c = 1
        f = True
    elif (a[i] in "ABC" and a[i+1] in "123" and a[i+2] in "ABC"):
        count += 1
        c = 2
        f = True
    else:
        maxi = count if maxi < count else maxi
        count = 0
        f = False if a[i] in "123" else True



maxi = count if maxi < count else maxi

print(maxi)

#TODO  пока 4