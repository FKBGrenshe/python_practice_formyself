#一般数学方法
print("一般数学方法".center(20,"-"))
pi = 0
N = 100
for k in range(N):
    pi += 1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
print("圆周率值是：{}".format(pi))
#蒙特卡罗方法
print("蒙特卡罗方法".center(20,"-"))
from random import random
from time import perf_counter
DARTS = 1000*1000*100 #DARTS=总撒点数
hits = 0.0 #撒到圆内部的点数
start = perf_counter() #开始时间
for i in range(1, DARTS+1):
    x,y = random(),random() #撒点的坐标
    dist = pow(x**2 + y**2,0.5) #撒点坐标到原点距离
    if dist <=1.0:
        hits += 1
pi = 4*(hits/DARTS)
print("圆周率值是：{}".format(pi))
print("运行时间={}".format(perf_counter()-start))
