with open("24_2506.txt") as f:
   a = f.read()

d = {}
for i in a:
   d[i] = d.setdefault(i,0)+1
maxi = max(d.values())
for i in d.keys():
   if d[i] == maxi:
      print(i,maxi)