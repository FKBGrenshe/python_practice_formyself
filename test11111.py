def foo(x,y='default',*z):
    print('arg1',x)
    print('arg2',y)
    print('arg3',z)
    for i in z:
        print('variablr args',i)

foo('first','second','3','4','5')
