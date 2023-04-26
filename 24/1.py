with open("24_2503.txt") as f:
   a = [i for i in f.readlines()]


def checker(s):
   count_aoa =0
   count_oao = 0
   
   for i in range(len(s)-2):
      if s[i]+s[i+1]+s[i+2] == "AOA":
         count_aoa +=1
      if s[i]+s[i+1]+s[i+2] == "OAO":
         count_oao+=1
   return count_oao < count_aoa

c = 0
for i in a:
   if checker(i):c+=1

print(c)