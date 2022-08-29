# 1.字符串反转
'''将字符串s反转后输出'''
'''
法1--使用字符串切片的方法>>>s[::-1]
'''
'''
法2--递归
'''
#ver1.0--written by myself
s = input()
a = len(s)
def output_reverse(a):
    if a == 1:
        print(s[-a],end="")
    else:
        output_reverse(a-1)
        print("{}".format(s[-a]),end="")
output_reverse(a)
#ver2.0--written by 嵩天
def rvs(s):
    if s =="":
        return s
    else:
        return rvs(s[1:])+s[0]
