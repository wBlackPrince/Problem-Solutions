with open("24data/24-212.txt") as f:
    a = f.read()

c = 0
maxi = 0
f = False
for i in range(len(a)):
    if a[i] in "AO":
        f = True
    elif a[i] in "BCD" and f:
        c += 1
        f = False
    else:
        maxi = c if c > maxi else maxi
        c = 0
maxi = c if c > maxi else maxi
print(maxi)

# ответ 202