#事件處理
def rbVideo():
    global getvideo
    labelMsg.config(text="")
    getvideo=videorb.get()

def checking():
    global IsChecking
    if url.get()=="":
        labelMsg.config(text="網址欄尚未輸入!")
        return
    else:
        yt=YouTube(url.get())
        labelYTName.config(text=yt.title)
        IsChecking=True

def clickDown():
    global getvideo,strftype,listradio,IsChecking
    labelMsg.config(text="")
    if IsChecking==False:
        labelMsg.config(text="影片尚未選擇!")
        return
    pathdir=filedialog.askdirectory(title='選擇下載位置(預設存於本程式所在位置之download夾)')
    if pathdir=="":
        pathdir='download'
    try:
        yt=YouTube(url.get())
        if DLname.get()=="":
            Fname=yt.title
        else:
            Fname=DLname.get()
        labelMsg.config(text="影片開始下載！")
        
        if getvideo=="1080p" or getvideo=="2160p":
            yt.streams.filter(subtype='mp4',res=getvideo,progressive=False).first().download(output_path=pathdir,filename=Fname+'-video.mp4')
            yt.streams.filter(subtype='mp4',type="audio",progressive=False).last().download(output_path=pathdir,filename=Fname+'-audio.mp4')

        else:
            yt.streams.filter(subtype='mp4',res=getvideo,progressive=True).first().download(output_path=pathdir,filename=Fname+'.mp4')
        labelMsg.config(text="下載完成！")
        os.startfile(pathdir)
        IsChecking=False
    except:
        labelMsg.config(text="影片無法下載！影片或選取的格式可能不存在。")
        '''錯誤測試指令
        print(url.get())
        print(pathdir)
        print(yt.title)
        print(yt.streams.filter(subtype='mp4',res=getvideo,progressive=True))
        print(IsChecking)
        '''
        

#功能匯入
from pytube import YouTube
import tkinter as tk
from tkinter import Variable, filedialog
import os,sys

#主視窗設定
mainw=tk.Tk()
mainw.geometry("560x450")
mainw.resizable(0,0)
mainw.title("Shuba_YT影片下載器 v1.1")
#mainw.iconphoto(True, tk.PhotoImage(file='D:\育綸專屬資料夾\高中(11022)\Personal\Learning\python\YT下載器/icon1.png'))
mainw.iconbitmap('icon_icon.ico')
mainw['bg']='#e0ff2c'
dltype='mp4'
getvideo="360p"
videorb=tk.StringVar()
url=tk.StringVar()
DLname=tk.StringVar()
IsChecking=False

#網址列
labelUrl=tk.Label(mainw,text="Youtube網址：",bg='#e0ff2c')
labelUrl.place(x=130,y=20)
entryUrl=tk.Entry(mainw,textvariable=url)
entryUrl.config(width=45)
entryUrl.place(x=220,y=20)

#網址確定鈕
checkbutton=tk.Button(mainw,text="選擇",command=checking)
checkbutton.place(x=225,y=100)

#影片名稱顯示
labelYT=tk.Label(mainw,text="影片名稱： ",bg='#e0ff2c')
labelYT.place(x=154,y=45)
labelYTName=tk.Message(mainw,text="",justify='left',width=310,anchor='w',bg='#e0ff2c')
labelYTName.place(x=220,y=45)
    
#存檔路徑輸入列
'''
labelPath=tk.Label(mainw,text="存檔路徑(預設為 download 資料夾)：",bg='#e0ff2c')
labelPath.place(x=10,y=140)
pathbutton=tk.Button(mainw,text="選擇資料夾",command=filechoose)
pathbutton.place(x=225,y=140)

entryPath=tk.Entry(mainw,textvariable=path)
entryPath.config(width=45)
entryPath.place(x=220,y=140)
'''

#檔案名稱列
labelName=tk.Label(mainw,text="檔案名稱：",bg='#e0ff2c')
labelName.place(x=154,y=140)
entryName=tk.Entry(mainw,textvariable=DLname)
entryName.config(width=45)
entryName.place(x=220,y=140)

#存檔路徑顯示
'''廢除
labelPA=tk.Label(mainw,text="下載位置： ",bg='#e0ff2c')
labelPA.place(x=154,y=95)
labelPAName=tk.Label(mainw,text="",bg='#e0ff2c')
labelPAName.place(x=220,y=95)
'''

#下載按鈕
downloadbutton=tk.Button(mainw,text="下載影片",command=clickDown)
downloadbutton.place(x=200,y=370)

#品質選擇
rb360=tk.Radiobutton(mainw,text=('360p, mp4'),variable=videorb,value='360p',command=rbVideo,bg='#e0ff2c')
rb360.place(x=200,y=210)
rb360.select()
rb480=tk.Radiobutton(mainw,text=('480p, mp4'),variable=videorb,value='480p',command=rbVideo,bg='#e0ff2c')
rb480.place(x=200,y=240)
rb720=tk.Radiobutton(mainw,text=('720p, mp4'),variable=videorb,value='720p',command=rbVideo,bg='#e0ff2c')
rb720.place(x=200,y=270)
rb1080=tk.Radiobutton(mainw,text=('1080p, mp4(影音分開)'),variable=videorb,value='1080p',command=rbVideo,bg='#e0ff2c')
rb1080.place(x=200,y=300)
rb2160=tk.Radiobutton(mainw,text=('2160p, mp4(影音分開)'),variable=videorb,value='2160p',command=rbVideo,bg='#e0ff2c')
rb2160.place(x=200,y=330)

#訊息標籤
labelMsg=tk.Label(mainw,text="",fg="#ff0000",bg='#e0ff2c')
labelMsg.place(x=200,y=410)

mainw.mainloop()
