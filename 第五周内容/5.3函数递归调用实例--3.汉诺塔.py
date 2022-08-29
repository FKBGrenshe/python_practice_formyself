#哈诺塔问题
'''
三根柱子
小的圆盘永远在大的圆盘上面
边上柱子从下往上由大到小累着64片圆盘
一次只能移动一个圆盘
从这边全部移动道另一边
'''
"""
1.给定数量的圆盘,从最左侧道最右侧需要多少步骤
2.如何搬运
"""
#version1.0--written by myself
'''思路； 
情况1: 3个圆盘--大中小; 3个柱子--ABC
    1st: 大中-A B 小-C
    2nd: 大-A 中-B 小-C
    3rd: 大-A 中小-B C
    4th: A 中小-B 大-C
    5th: 小-A 中-B 大-C
    6th: 小-A B 中大-C
    7th: A B 小中大-C
    完成
情况2: >3个圆盘--将除小大两个圆盘外, 其余全部视为中间--递归
'''
#version2.0--嵩天
'''
将n-1个圆盘全部移动到B
将最后的圆盘移动到C
再将n-1个圆盘由B经过A移动到C
'''
count = 0 #用来计算步数
n = eval(input()) #给定的盘子数
def hanoi(n,src,dst,mid): #src--当前圆盘的原柱子; dst--当前圆盘所在的目的柱子; mid--当前圆盘所经过的柱子
    global count
    if n == 1:
        #print("{}:{}->{}".format(1,src,dst))
        count += 1
    else:
        hanoi(n-1,'A','B','C')
        print("{}:{}->{}".format(n,src,dst))
        count += 1
        hanoi(n-1,'B','C','A')
hanoi(n,'A','C','B')
print("{}".format(count))