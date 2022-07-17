#第一周温度转换默写
a = input("please enter the content\n you must confirm that the string you enter is end with 'f' or 'c'! ")
if a[-1] in ['F','f']:
    print("the content is end of 'f'\n")
    b = (eval(a[0:-1])-32)/1.8
    print("the new content is {:.2f}C".format(b))
elif a[-1] in ['C','c']:
    print("the content is end of 'c'\n")
    b = (eval(a[0:-1])*1.8)+32
    print("the new content is {:.2f}".format(b))
else:
    print("wrong")