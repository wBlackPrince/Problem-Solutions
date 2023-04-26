with open("158.txt") as f:
   a = [[int(j) for j in i.split("\t")] for i in f.readlines()]

def checker(arr):
   return sum([i for i in arr if i%2 != 0]) > sum([i for i in arr if i%2 == 0])

c = 0
for i in a:
   if checker(i):
      c+=1
print(c)

#1549