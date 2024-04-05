numbers = input("请输入数字")
total = 0
count = 0
while numbers != "q":
    num = float(numbers)
    total += num
    count += 1
    numbers = input("请输入数字")
if count == 0:
    result = 0
else:
    result = total / count
print(str(result))
