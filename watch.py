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


class tape:

    def __init__(self):
        self.win = Tk()
        self.pro = ''
        self.i=0
        self.end=0
        self.active = False
        self.pname = StringVar()
        self.var = IntVar()
        self.folders = os.listdir('projects\\')

        self.win.title('FollowScreen')
        self.win.geometry('1366x768+0+0')

        self.load = Image.open('Drawing.png')
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.win,image=self.render)
        self.img.image = self.render

        self.pnamet = Entry(self.win,textvar=self.pname,font=('arial',15,'italic'))
        self.palready = Label(self.win,text='',fg='black',font=('arial',15,'italic'))
        self.pnamel = Label(self.win,text='Project Name',fg='blue',font=('arial',15,'italic'))
        self.heading = Label(self.win,text='FollowScreen-Tapes',fg='black',font=('arial',30,'bold'))
        self.startbutton = Button(text='Start Watching',fg='green',bg='black',command=self.start,font=('arial',15,'bold'))
        self.pausebutton = Button(text='Pause',fg='red',bg='black',command=self.pause,font=('arial',10,'bold'))
        self.scale = Scale(self.win, variable = self.var ,from_=1,orient='horizontal',bd=0,width=5,length=1366,fg='black',cursor='dot',repeatdelay='100',command=self.toon)

        self.listf = Menu(self.win)
        self.listf.add_command(label='Open',command=newwin)
        self.listf.add_command(label='Quit',command=self.win.destroy)

        self.listh = Menu(self.win)
        self.listh.add_command(label='Help',command=self.fhelp)
        self.listh.add_command(label='About',command=self.fabout)


        self.wmenu = Menu(self.win)
        self.wmenu.add_cascade(label='File',menu=self.listf)
        #self.wmenu.add_cascade(label='Controls',command=self.controls)
        self.wmenu.add_cascade(label='Help',menu=self.listh)

        self.win.config(menu=self.wmenu)

        return


    def toon(self):
        self.active=False
        print('sliding')
        self.watch()

    def start(self):
        self.pro = self.pname.get()
        if self.pro in self.folders:
            self.end=len(os.listdir('projects\\'+self.pro+'\\'))
            self.heading.destroy()
            self.startbutton.destroy()
            self.pnamel.destroy()
            self.pnamet.destroy()
            self.palready.destroy()
            self.img.place(x=0,y=0)
            self.scale.config(to=self.end)
            self.scale.place(x=0,y=200)
            self.pausebutton.place(x=0,y=600)
            self.watch()
        else:
            self.palready.config(text='Project does not Exsist')
        return

    def pause(self):
        self.active = False
        self.pausebutton.destroy()
        self.resumebutton = Button(text='Resume',fg='blue',bg='black',command=self.resume,font=('arial',10,'bold'))
        self.resumebutton.place(x=0,y=600)
        print('pause clicked')
        return

    def resume(self):
        self.resumebutton.destroy()
        self.pausebutton = Button(text='Pause',fg='red',bg='black',command=self.pause,font=('arial',10,'bold'))
        self.pausebutton.place(x=0,y=600)
        print('resume clicked')
        self.watch()
        return

    def watch(self):
        self.active = True
        def show():
            try:
                self.i = self.var.get()
                if self.i + 1 <= self.end and self.active == True:
                    self.i+=1
                    self.scale.set(self.i)
                    self.load = Image.open('projects/'+self.pro+'/'+str(self.i)+'.png')
                    self.render = ImageTk.PhotoImage(self.load)
                    self.img.config(image=self.render)
                    self.img.image = self.render
                    print(str(self.i))
                    self.img.after(200,show)
                elif self.i + 1 > self.end:
                    temp = pyg.alert('That was all! Closing "'+self.pro +'" Tape Window!!')
                    if temp == 'OK':
                        self.win.destroy()

            except:
                print('error ocurred')
        show()

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
        return


def newwin():
    win = tape()
    win.wakeup()


watch = tape()
watch.wakeup()
