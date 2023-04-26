with open("24_1143.txt") as f:
   a = f.read()

def founder(n):
   c = 0
   for i in range(len(a)-n):
      if a[i] == "A" and a[i+n] == "F":
         c+=1
   return c

print(founder(6) + founder(7) + founder(8) + founder(9))