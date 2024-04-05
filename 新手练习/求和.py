# 求1到100内的数字之和

def get_num(min_num, max_num):
    i = min_num
    result = 0
    while i <= max_num:
        i += 1
        if i % 2 > 0:
            continue
        result += i
        print(result)


num_1 = int(input('输入最小数字'))
num_2 = int(input('输入最大数字'))
get_num(min_num=num_1, max_num=num_2)
