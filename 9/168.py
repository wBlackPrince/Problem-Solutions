with open("168.txt") as f:
   a = [[int(j) for j in i.split("\t")] for i in f.readlines()]


def checker(arr):
   sr = sum(arr)/len(arr)
   return [arr[0] > sr, arr[1] > sr, arr[2] > sr,arr[3] > sr, arr[4] > sr].count(True) >= 3

c = 0
for i in a:
   if checker(i):
      c+=1
print(c)
#1035