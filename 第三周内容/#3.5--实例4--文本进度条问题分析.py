#"文本进度条"代码
'''1.0版本 -- 多行非动态文本进度条'''
import time
scale = 10
print("1.0版本 -- 多行非动态文本进度条")
print("------执行开始------")
for i in range (scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("------执行结果------")

'''2.0版本 -- 单行动态文本进度条'''
print("2.0版本 -- 单行动态文本进度条")
""" 刷新本质
        1. 用后打印字符覆盖之前打印字符
        2. 不能换行 -- print()需要被控制
        3. 需要回退 -- 打印后光标退回到之前的位置\r"""
print("------执行开始------")
for i in range (101):
    print("\r{:3}%".format(i),end=" ")
        #print(,,end="") -- end=""可以控制print输出，默认print输出后切换下一行，此处替换为输出一个空格
        #\r代表光标回到当前行行首
    time.sleep(0.1)
print("\n------执行结果------")

'''3.0版本 -- 完整动态进度条'''
print("3.0版本 -- 完整动态进度条")
scale = 50
print("执行开始".center(scale//2,"-"))
start = time.perf_counter()
for i in range (scale + 1):
    a = '*' * i
    b = '-' * (scale -i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end=' ')
    time.sleep(0.1)
print("\n" + "执行结束".center(scale//2,'-'))