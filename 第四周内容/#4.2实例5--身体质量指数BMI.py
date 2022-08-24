#BMI -- body mass index = 体重/(身高**2)
'''问题需求
    1. 输入: 给定体重和身高值
    2. 输出: BMI指标分类信息(国际+国内)'''
height,weight = eval(input("请输入身高(米)和体重(公斤)[逗号隔开]:"))
bmi = weight / pow(height,2)
print("BMI数值为{:.2f}".format(bmi))
who,nat = "",""
if bmi < 18.5:
    who,nat = "偏瘦","偏瘦"
else:
    print("其他省略")
print("who = {},nat = {}".format(who,nat))