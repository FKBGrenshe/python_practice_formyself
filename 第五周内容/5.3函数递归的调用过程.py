"""
数学递归
n!=
    1       n=0
    n(n-1)! otherwise
"""
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)