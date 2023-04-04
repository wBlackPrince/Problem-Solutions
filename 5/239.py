def convert(n,a):
   t = ""
   while n>0:
      t+=str(n%a)
      n//=a
   return t[::-1]

def f(n):
   octi = convert(n,6)
   octi += octi[-1]
   
   bini = bin(int(octi,6))[2:]
   bini += bini[-1]
   
   return int(bini,2)

maxi = 0
for i in range(10_000,100_000):
   n = f(i)
   maxi = n if n > maxi and n < 344 else maxi
   
print(maxi)
#331