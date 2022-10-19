import numpy
#numpy的n维数组
A = numpy.array([[1,2],[3,4]])
print(A); print(A.shape); print(A.dtype)

#NumPy数组的广播功能---对于常量
A *= 10
print("A*10"); print(A)

#不同NumPy数组之间的
B = numpy.array([1,2])
print("这是B",B)
print("这是A*B");print(A*B,B.dtype,B.shape)
'''原理： B的一位数组被扩充成与A的规格一致的二维数组[[1,2],[1,2]],再与A相乘'''

#1.5.6访问元素
X = numpy.array([[0,1],[2,3],[4,5]])
print("这是原数组X: \n",X,"\nX的规格")
xflatten = X.flatten()
print("这是降维后的数组xflatten:\n",xflatten,"\n太牛辣!")
print("那在比较大小的时候,布尔型的数组?\n运用 X[X>N] !")
print("1st: 先输出判断出的布尔数组 X>2",X>2)
print("2nd: 再输出依靠上述布尔数组输出的符合比较条件的数组\n",X[X>=3])