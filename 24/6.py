with open("24_2504.txt") as f:
   a = f.read()

d = {}
for i in range(len(a)-4):
   if a[i] == "C" and a[i+1] == "B" and a[i+3] == "B" and a[i+4] == "C":
      d[a[i+2]] = d.setdefault(a[i+2],0)+1

maxi = max(d.values())
for i in d.keys():
   if d[i] == maxi:
      print(i,maxi)
