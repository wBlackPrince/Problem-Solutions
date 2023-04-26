with open("24_2509.txt") as f:
   a = f.read()

d = {}
for i in a:
   if i != a[-1]:
      d[i] = d.setdefault(i,0)+1

maxi,mini = max(d.values()),min(d.values())
print(maxi-mini)