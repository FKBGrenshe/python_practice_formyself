'''
基本思路:
    1. 先绘制单个数字对应的数码管
    2. 获得一串数字, 绘制对应的数码管
    3. 真实获得当前系统时间, 绘制对应数码管
    4. 使用time库获得系统当前时间--未作太麻烦
    5. 增加"年""月""日"标记--未作太麻烦--用turtle.wirte可以绘制汉字
'''
import turtle
def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw): #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(digit): #e.g.整数=8每一条线段都要绘制；整数=0第一条线段不绘制
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup() #为绘制后续数字确定位置
    turtle.fd(20)
def drawDate(date):
    for i in date:
        drawDigit(eval(i)) #通过eval()函数将数字变为整数
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate('20220826')
    turtle.hideturtle()
    turtle.done
main()
