# 测试BMI指数
user_weight = float(input("请输入您的体重 （单位：kg）:"))
user_height = float(input("请输入您的身高 （单位：m）:"))
user_BMI = user_weight / user_height ** 2
print("您的BMI指数为：" + str(user_BMI))
if user_BMI <= 18.5:
    print("此BMI指数属于偏廋范围")
elif 18.5 < user_BMI <= 25:
    print("此BMI指数属于正常范围")
elif 25 < user_BMI <= 30:
    print("此BMI指数属于偏胖范围")
else:
    print("此BMI指数属于肥胖范围")


def user_bmi(weight, height):
    BMI = weight / height ** 2
    if BMI <= 18.5:
        category = "偏廋"
    elif BMI <= 25:
        category = "正常"
    elif BMI <= 30:
        category = "偏胖"
    else:
        category = "肥胖"
    print(f"{category}")
    return BMI
