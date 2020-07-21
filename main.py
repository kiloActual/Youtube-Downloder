from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

file_size = 0

def completeDownload(stream=None, file_path=None):
    print("done..")
    showinfo("Downloaded Finished","Downloaded successfully")
def progress_check(stream=None, chunk=None, bytes_remaining=None):
   
    percent = (100 * ((file_size - bytes_remaining) / file_size))
    dBtn['text']="{:00.0f}% downloaded".format(percent)

def startDownload():
    global file_size
    try:
        url = urlField.get()
        print(url)

        #changing button text
        dBtn.config(text="Please wait...")
        dBtn.config(state=DISABLED)

        path_to_save_video = askdirectory()
        print(path_to_save_video)
        if path_to_save_video is None:
            return

        #creating youtube object with url ..
        ob=YouTube(url)

        #st = ob.streams.all()
        #for s in strm:
        #   print(s)
        strm=ob.streams.get_by_itag('22')
        file_size=strm.filesize

        

        vTitle.config(text=strm.title)
        vTitle.pack(side=TOP)
        print(strm.filesize)
        

        ob.register_on_complete_callback(completeDownload)
        ob.register_on_progress_callback(progress_check)
        #now downloading the video
        strm.download(path_to_save_video)
      
        dBtn.config(text='Start Download')
        dBtn.config(state=NORMAL)
        
        urlField.delete(0,END)
        vTitle.pack_forget()

    except Exception as e:
        print(e)
        print("error!!")

#starting GUI        
main = Tk()

main.title("Youtube Downloader")

#set the icon
main.iconbitmap('downloader.ico')

main.geometry("400x500")

#heading icon
file=PhotoImage(file='downloader.png')
headingIcon=Label(main,image=file)
headingIcon.pack(side=TOP)

#url textfield
urlField=Entry(main,font=("verdana",18),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=10)

#download button
dBtn=Button(main,text="Start Download",font=("verdana",18),relief='ridge',command=startDownload)
dBtn.pack(side=TOP,pady=10)

vTitle= Label(main,text="video title")

vName= Label(main,text="Developed by Apurv Prajapati",font=("verdana",10))
vName.pack(side=BOTTOM)
main.mainloop()
