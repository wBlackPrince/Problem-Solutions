def checker(n):
   return n[:3] == "270" and n[4] == "5" and n[-2:] == "43"

for i in range(10):
   for j in range(10):
      n = "270" + str(i) + "5" + str(j) + "43"
      if int(n) > 10**9: continue
      if checker(n) and int(n)%21 == 0:
         print(n, int(n)//21)