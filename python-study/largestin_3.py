x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
a = 54
if x > y:
    if x > z:
        print("largest: ",x)
    else :
        print("largest: ",z)
else:
    if y > z:
        print("largest: ",y)
    else:
        print("largest: ",z)

res = max(x, y, z, a)
print(res)