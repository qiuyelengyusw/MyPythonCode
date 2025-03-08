# 九九乘法表
i = 1
while i <=9:
    j = 1
    while j <= i:
      print(j, "x" , i , "=", i*j , end = "  ")
      j += 1
    print()
    i = i + 1
print()
# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} x {i} = {i*j}", end="  ")
    print()
print()

for i in range(1, 3):
    print(i, end="\t")
print()
for i in range(5):
    print(i, end="\t")
print()
for i in range(1, 10, 2):
    print(i, end="\t")