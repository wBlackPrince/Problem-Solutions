with open("198.txt") as f:
   a = [[int(j) for j in i.split("\t")] for i in f.readlines()]


def checker(a1,a2,a3,a4,a5,a6):
   bools = [a1%3 == 0, a2%3 == 0, a3%3 == 0,a4%3 == 0, a5%3 == 0, a6%3 == 0]
   return bools.count(True) == 3

def checker_1(a1,a2,a3,a4,a5,a6):
   mini,maxi = min([a1,a2,a3,a4,a5,a6]), max([a1,a2,a3,a4,a5,a6])
   summi = sum([i for i in [a1,a2,a3,a4,a5,a6] if i%3 == 0])
   return (maxi - mini) <= summi

c = 0
for i in a:
   if checker(i[0],i[1],i[2],i[3],i[4],i[5]) and checker_1(i[0],i[1],i[2],i[3],i[4],i[5]):
      c+=1
print(c)

#1835