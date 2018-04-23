import time
while True:
    x = 0
    while x<=110:
        color = '\033['+str(x)+'m'
        print(str(x) + color + "XXX")
        x+=1
        time.sleep(0.3)
