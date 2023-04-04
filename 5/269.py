def f(n):
   bini = bin(n)[2:]
   if n%2 != 0:
      bini = "1" + bini + "11"
   else:
      bini = "11" + bini + "00"
   return int(bini,2)

maxi = 0
for i in range(10_000_000,10_500_000):
   n = f(i)
   maxi = n if n > maxi and n  < 127 else maxi
print(maxi)
#120