with open("24_836.txt") as f:
   a = f.read()

c = 0
for i in range(len(a)-4):
   s = a[i]+a[i+1]+a[i+2]+a[i+3]+a[i+4]
   if s == s[::-1]:
      c+=1
print(c)

