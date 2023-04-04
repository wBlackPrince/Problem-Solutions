def zap(n):
   while len(n)!= 4:
      n = "0"+n
   return n

def converter(n):
   mas = []
   while n > 0:
      mas.append(zap(bin(n%10)[2:]))
      n//=10
   mas = mas[::-1]
   
   for i in range(len(mas)):
      if mas[i].count("1") == 2:
         mas[i] += "0"
      else:
         mas[i] += "1"
   
   s = "".join(mas)
   s = "1"+s[2:]+"0"
   
   return int(s,2)

for i in range(400,10000):
   if converter(i)==674890:
      print(i)
      break