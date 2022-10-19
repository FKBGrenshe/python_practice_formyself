#1.3~1.4
class Man:
    def __init__(self,name):
        self.name = name
        print("Initialized")
    
    def hello(self):
        print("Hello"+self.name+"!")
    def goodbye(self):
        print("Goodbye"+self.name+"!")


m = Man("Tom")
m.hello()
m.goodbye()

'''Numpy数组类(numpy.array)提供了很多便捷的方法'''
#1.5.1--Numpy的导入
from time import process_time_ns
import numpy as np  #将numpy导入，并用np运用
#1.5.2--生成Numpy数组
x = np.array([1.0,2.0,3.0])
print(x)
print(type(x))
#1.5.3--numpy数组的算术运算
print


x1 = np.array([1.0,2.0,3.0])
y1 = np.array([2.0,4.0,6.0])
print(x1+y1); print(x1-y1); print(x1*y1); print(x1/y1)
k = 2; print(x1/k)
