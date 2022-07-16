#货币转换
value = input()
if value[:3] in ["RMB"]:
    answer = eval(value[3:])/6.78
    print("USD{:.2f}".format(answer))
elif value[:3] in ["USD"]:
    answer = eval(value[3:])*6.78
    print("RMB{:.2f}".format(answer))