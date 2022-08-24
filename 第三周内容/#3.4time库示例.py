from re import A
import time
timestart = time.perf_counter()
print(timestart)
#time库示例
'''time库获取函数 '''
a_time = time.time()
print(a_time)
a_ctime = time.ctime()
print(a_ctime)
a_gmtime = time.gmtime()
print(a_gmtime)
a_strftime = time.strftime("%Y-%m-%d %H:%M:%S",a_gmtime)
print(a_strftime)
a_strptime = time.strptime(a_strftime,"%Y-%m-%d %H:%M:%S")
print(a_strptime)
time.sleep(10.0)
'''time库程序及时应用'''
timeend = time.perf_counter()
time_perf_counter = timeend - timestart
print(timeend)
print(time_perf_counter)