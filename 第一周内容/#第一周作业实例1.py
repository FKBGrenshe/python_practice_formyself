#第一周作业
'''
实例1:温度转换
'''
value = input()
if value[-1] in ["C", "c"]:
    answer = eval(value[0:-1])*1.8 + 32
    print("{:.2f}F".format(answer))
elif value[-1] in ["F","f"]:
    answer = (eval(value[0:-1]) - 32)/1.8
    print("{:.2f}C".format(answer))
else:
    print("输入格式错误")