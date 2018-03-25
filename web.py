import webbrowser
import time

for i in range(1,4,1):
    time.sleep(7200)
    print ("Current time is : "+time.ctime())
    webbrowser.open("http://listenasong.com/")
