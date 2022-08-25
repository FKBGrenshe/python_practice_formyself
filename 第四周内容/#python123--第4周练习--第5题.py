i=1
while i<=3:
    i +=1
    user = input()
    password = eval(input())
    if user=='Kate' and password == 666666:
        print("登录成功！")
        break
else:
    print("3次用户名或者密码均有误!退出程序。")