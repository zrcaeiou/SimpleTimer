#Version 0.1
import tkinter
import time
#Gloable Variable
root = tkinter.Tk()
root.title('时钟')
targetTime=time.mktime(time.strptime("19 52 15 27 8 2021","%H %M %S %d %m %Y"))
lb = tkinter.Label(root,text='',fg='#f01020',font=("黑体",80),bg='#f0f0f0')

def gettime():
      timeInterval=time.time()-targetTime-86400#计算时间差
      timestr = time.strftime("%D-%H:%M:%S") # 获取当前的时间并转化为字符串
      lb.configure(text='\n当前时间:'+timestr+'\n\n玻璃固化热调试已连续运行\n'+time.strftime("%d天%H小时%M分%S秒",time.gmtime(timeInterval)))   # 重新设置标签文本
      root.after(1000,gettime) # 每隔1s调用函数 gettime 自身获取时间

def main():
      lb.pack()
      gettime()
      w = root.winfo_screenwidth()
      h = root.winfo_screenheight()
      root.geometry("%dx%d" %(w,h))
      root.attributes("-topmost",True)
      root.overrideredirect(True)
      root.mainloop()

if __name__ == '__main__':
      main()