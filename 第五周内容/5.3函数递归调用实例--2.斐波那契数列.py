#2.斐波那契数列
'''
F(n) = 
    1               n = 1
    1               n = 2
    F(n-1) + F(n-2) otherwise
'''
figure = eval(input())
#ver1.0--written by myself
def value(figure):
    if figure == 1 or figure ==2:
        return 1
    else:
        return value(figure-1)+value(figure-2)
#version2.0--嵩天 as same as version1.0
