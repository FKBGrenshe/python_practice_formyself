#1年365天，每天进步1%，累计进步多少？
#1年365天，每天退步1%，累计退步多少？

# the first qustion: progress or retrogress 1‰ everyday
progress1000 = pow(1.01, 365)
retrogress1000 = pow(0.999, 365)
print("天天向上1‰:{:.2f},天天向下1‰:{:.2f}".format(progress1000,retrogress1000))
#the second question :if the progress or retrogress is different and virable ,how can i finish this work?
"""i need to set a variable to instead these numbers which cannot be changed."""
provariable = 0.005
retrovariable = 0.01
"provariable represent the number of progress and retrovariable represent the number of retrogress"
progress = pow(1+provariable,  365)
retrogress = pow(1-retrovariable, 365)
print("天天向上1‰:{:.2f},天天向下1‰:{:.2f}".format(progress,retrogress))
#the third question : what if progress only affects on workday and you will retrogress 1% every rest day?
"""i need to set a new variable named value to save up-to-date value"""
provariable = retrovariable = 0.01
value = 1
for i in range (365):
    if i % 7 in [6,0]:
        value *= (1-retrovariable)
    else:
        value *= (1+provariable)
    print("在第",i+1,"天，效率为:{:.2f}".format(value))
#the fourth question : i want to know how hard i need to work in the third situation that can be like in the first situation.
"""i need o set a fuction"""
def pro(prov):
    value = 1
    for i in range (365):
        if i % 7 in [6,0]:
            value *= (1-0.01)
        else:
            value *= (1+prov)
    return value
provariable = 0.01
while pro(provariable) < 37.78:
    provariable +=0.001
print("工作日的努力参数是{:.3f}".format(provariable))