max_x = -1
max_v = 0

for x in range(44):
    num1 = 44**3 + 44**2*x + 44*2 + 3
    num2 = 44**3*3 + 44**2*2 + 44*x + 1

    if (num1 + num2)%42==0:
        if x > max_x:
            max_x = x
            max_v = num1+num2
print(max_v/42)
#10140