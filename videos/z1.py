from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from tkinter.messagebox import *
import os
#import matplotlib.pyplot as plt
#import numpy

def about():
    showinfo(title='使用说明',message='文件路径中请勿带空格')
def file_encode():
    Label(root, text=empty, foreground="Black", font=('黑体', 12)).place(x=100, y=0)
    file_path = filedialog.askopenfilename()
    global para8
    para8 = file_path
    Label(root, text=file_path, foreground="Black", font=('黑体', 12)).place(x=100, y=0)
def file_decode():
    Label(root, text=empty, foreground="Black", font=('黑体', 12)).place(x=100, y=250)
    file_path = filedialog.askopenfilename()
    global para9
    para9 = file_path
    Label(root, text=file_path, foreground="Black", font=('黑体', 12)).place(x=100, y=250)
def encode():
    global para8
    if(para2.get()!=''):
        pa2='-s '+para2.get()
    else:
        pa2=''
    if (para3.get() != ''):
        pa3 = '-r ' + para3.get()
    else:
        pa3 = ''
    if (para4.get() != ''):
        pa4 = '-b ' + para4.get()
    else:
        pa4 = ''
    if (para5.get() != ''):
        pa5 = '-g ' + para5.get()
    else:
        pa5 = ''
    if (para6.get() != ''):
        pa6 = '-bf ' + para6.get()
    else:
        pa6 = ''
    cmd = 'ffmpeg -s %s -i %s %s %s %s %s %s -vcodec h264 %s.mp4' % (para1.get(), para8, pa2,pa3,pa4,pa5,pa6,para7.get())
    while True:
        try:
            os.popen(cmd)
            showinfo(message='编码完成')
            break
        except KeyboardInterrupt:
            showinfo(message='发生错误')
def decode():
    global para9
    cmd = 'ffmpeg -i %s %s.yuv' % (para9, para10.get())
    while True:
        try:
            os.popen(cmd)
            showinfo(message='解码完成')
            break
        except KeyboardInterrupt:
            showinfo(message='发生错误')
def psnr():
    file_path = filedialog.askopenfilenames()
    a='lab'.txt'
    Label(root, text=file_path, foreground="Black", font=('黑体', 12)).place(x=230, y=350)
    cmd = 'psnr %s 420 %s %s >%s' % (para11.get(),file_path[0],file_path[1],a)
    p=os.popen(cmd)
    y = []
    infile = open(file='lab.txt')
    for line in infile:
        trainingSet = line.split('\n')
        y.append(float(trainingSet[0]))
    length = len(y)
    sum=0
    for i in range(length):
        sum+=y[i-1]
    sum=float(sum/length)
    print(sum)
    Label(root, text='psnr平均值:', foreground="Blue", font=('黑体', 12)).place(x=200, y=380)
    Label(root, text=sum, foreground="Black", font=('黑体', 12)).place(x=300, y=380)
    # x=numpy.array(range(length))
    # plt.figure(1)
    # plt.ylim(0,50)
    # plt.scatter(x,y,c='r',marker='.')
    # plt.show()


root = Tk()
root.title('多媒体通信第四次作业实验')
root.geometry('700x500')
menubar = Menu(root)
# 创建下拉菜单File，然后将其加入到顶级的菜单栏中
# filemenu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label="File", menu=filemenu)
# 创建另一个下拉菜单Edit
# editmenu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label="Edit", menu=editmenu)
# 创建下拉菜单Help
helpmenu = Menu(menubar,tearoff=0)
helpmenu.add_command(label="关于", foreground='Black',command=about)
menubar.add_cascade(label="帮助", menu=helpmenu)
# 显示菜单
root.config(menu=menubar)

para1 = StringVar()  # 源文件分辨率
para2 = StringVar()  # 目标文件的分辨率
para3 = StringVar()  # 帧率
para4 = StringVar()  # 码率
para5 = StringVar()  # I帧间隔
para6 = StringVar()  # B帧间隔
para7 = StringVar()  # 要保存的文件名
para8 = StringVar()  # 编码文件位置
para9 = StringVar()  # 解码文件位置
para10 = StringVar() # 要保存的文件名
para11 = StringVar() # psnr比较文件的分辨率
empty = '                                                                                    '  # 清除显示

Button(root, text='选择.yuv文件', command=file_encode).place(x=10, y=0)
Button(root, text='选择.mp4文件', command=file_decode).place(x=10, y=250)
Button(root, text='编码', command=encode).place(x=350, y=180)
Button(root, text='解码', command=decode).place(x=350, y=280)
Button(root, text='PSNR分析', command=psnr).place(x=130, y=350)
Label(root, text='源文件的分辨率:', foreground="Blue", font=('黑体', 12)).place(x=0, y=27)
Label(root, text='分辨率:', foreground="Black", font=('黑体', 12)).place(x=0, y=50)
Label(root, text='帧率:', foreground="Black", font=('黑体', 12)).place(x=0, y=75)
Label(root, text='码率  :', foreground="Black", font=('黑体', 12)).place(x=0, y=100)
Label(root, text='I帧间隔:', foreground="Black", font=('黑体', 12)).place(x=0, y=125)
Label(root, text='B帧数目:', foreground="Black", font=('黑体', 12)).place(x=0, y=150)
Label(root, text='要保存的文件名:', foreground="Blue", font=('黑体', 12)).place(x=0, y=180)
Label(root, text='要保存的文件名:', foreground="Blue", font=('黑体', 12)).place(x=0, y=280)
Label(root, text='(比较文件的分辨率)', foreground="Blue", font=('黑体', 12)).place(x=0, y=380)
Entry(root, textvariable=para7).place(x=150, y=180)
Entry(root, textvariable=para10).place(x=150, y=280)
Combobox(root, textvariable=para1, values=['qcif', 'cif']).place(x=150, y=25)
Combobox(root, textvariable=para2, values=['qcif', 'cif']).place(x=150, y=50)
Combobox(root, textvariable=para3, values=['10', '20', '25', '30', '40', '50','60','70']).place(x=150, y=75)
Combobox(root, textvariable=para4, values=['50k', '100k', '200k', '300k', '500k','800k','1000k']).place(x=150, y=100)
Combobox(root, textvariable=para5, values=['0', '10', '20', '30', '50', '80','100','200']).place(x=150, y=125)
Combobox(root, textvariable=para6, values=['0', '20', '50', '100', '200', '250']).place(x=150, y=150)
Combobox(root, width=12,textvariable=para11, values=['176 144', '352 288']).place(x=10, y=350)
mainloop()