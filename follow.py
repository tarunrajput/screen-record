import os
import pyautogui as pyg
from tkinter import *
from PIL import Image, ImageTk


class about:
    def __init__(self):
        self.win = Tk()
        self.win.title('About | FollowScreen')
        self.win.geometry('800x300+200+100')
        self.heading = Label(self.win,text='FollowScreen-About',fg='black',font=('arial',30,'bold'))
        self.pnamel = Label(self.win,text='This is a Screen Recorder developed by Shubham Sawant in Python.',fg='blue',font=('arial',15))

    def wakeup(self):
        self.heading.pack()
        self.pnamel.pack()
        self.win.mainloop()
        return

class help:
    def __init__(self):
        self.win = Tk()
        self.win.title('Help | FollowScreen')
        self.win.geometry('800x300+200+100')
        self.heading = Label(self.win,text='FollowScreen-Help',fg='black',font=('arial',30,'bold'))
        self.pnamel = Label(self.win,text='Some Instructions\nThen Some more Instructions\nSome precautions \n again a few steps',fg='blue',font=('arial',15))

    def wakeup(self):
        self.heading.pack()
        self.pnamel.pack()
        self.win.mainloop()
        return

class fms:

    def start(self):
        self.pro = self.pname.get()
        if self.pro not in self.folders:
            try:
                os.makedirs('projects\\'+self.pro+'\\')
                self.startbutton.destroy()
                self.pnamel.destroy()
                self.pnamet.destroy()
                self.pausebutton.pack()
                self.stopbutton.pack()
                self.active = True
                self.follow()
            except:
                self.palready.config(text='Enter valid name.')
        else:
            self.palready.config(text='Project already exsits')

    def stop(self):
        self.active = False
        #self.finalize()
        self.win.destroy()
        self.__init__()
        self.wakeup()
        return

    def finalize(self):
        files = os.listdir('projects\\'+self.pro)
        i=0
        for file in files:
            try:
                i+=1
                img = Image.open('projects\\'+self.pro+'\\'+file)
                temp = img.resize((1280,720))
                temp.save('projects\\'+self.pro+'\\'+file)
            except:
                print('exception in finalize')

        return

    def pause(self):
        self.active = False
        self.pausebutton.destroy()
        self.resumebutton = Button(self.win,text='Resume Following',fg='green',bg='black',command=self.resume,font=('arial',15,'bold'))
        self.resumebutton.pack()
        return

    def resume(self):
        self.active = True
        self.resumebutton.destroy()
        self.pausebutton = Button(self.win,text='Pause Following',fg='blue',bg='black',command=self.pause,font=('arial',15,'bold'))
        self.pausebutton.pack()
        self.follow()
        return

    def follow(self):
        def shot():
            if self.i!=0 and self.active == True:
                pyg.screenshot('projects\\'+self.pro+'\\'+str(self.i)+'.png')
                self.i+=1
                self.palready.config(text='Started Following '+self.pro+' '+str(self.i))
                self.palready.after(200,shot)
        shot()

    def __init__(self):
        self.win = Tk()
        self.pro = ''
        self.i=1
        self.active = False
        self.pname = StringVar()
        self.folders = os.listdir('projects\\')
        self.win.title('FollowScreen')
        self.win.geometry('300x500+175+50')
        self.pnamet = Entry(self.win,textvar=self.pname,font=('arial',15,'italic'))
        self.palready = Label(self.win,text='',fg='black',font=('arial',15,'italic'))
        self.pnamel = Label(self.win,text='Project Name',fg='blue',font=('arial',15,'italic'))
        self.heading = Label(self.win,text='FollowScreen',fg='black',font=('arial',30,'bold'))
        self.startbutton = Button(self.win,text='Start Following',fg='green',bg='black',command=self.start,font=('arial',15,'bold'))
        self.stopbutton = Button(self.win,text='Stop Following',fg='red',bg='black',command=self.stop,font=('arial',15,'bold'))
        self.pausebutton = Button(self.win,text='Pause Following',fg='blue',bg='black',command=self.pause,font=('arial',15,'bold'))
        self.listf = Menu(self.win)
        self.listf.add_command(label='Quit',command=self.win.destroy)
        self.listh = Menu(self.win)
        self.listh.add_command(label='Help',command=self.fhelp)
        self.listh.add_command(label='About',command=self.fabout)
        self.wmenu = Menu(self.win)
        self.wmenu.add_cascade(label='File',menu=self.listf)
        self.wmenu.add_cascade(label='Help',menu=self.listh)
        self.win.config(menu=self.wmenu)

    def fabout(self):
        a = about()
        a.wakeup()
        return

    def fhelp(self):
        h = help()
        h.wakeup()
        return

    def wakeup(self):
        self.heading.pack()
        self.pnamel.pack()
        self.pnamet.pack()
        self.startbutton.pack()
        self.palready.pack()
        self.win.mainloop()

follow = fms()
follow.wakeup()



