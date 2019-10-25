import sys
from tkinter import *
import time
# Simple enough, just import everything from tkinter.
from tkinter import *

#here introduce menu
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)
        # reference to the master widget, which is the tk window
        self.master = master
        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()
        #stopwatch variable
        self.start = 0.0
        self.elapsedtime = 0.0
        self.runing = 0.0
        self.timestr = StringVar()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("GUI")
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        # creating a menu instance
        time_btn = Button(self, text="time", command = self.show_time)
        sw_btn = Button(self, text="Stop watch", command=self.sw_time)
        #location button
        time_btn.grid(row=0, column=1)
        sw_btn.grid(row=0)

    def show_time(self):

        clock = Label(root, font=('times', 100, 'bold'), bg='green')
        clock.place(x=10,y=100)
        # get the current local time from the PC
        time_string = time.strftime('%H:%M:%S')
        # if time string has changed, update it
        clock.config(text=time_string)
        clock.after(200, self.show_time)

    def sw_time(self):
        sw_label = Label(self,textvariable=self.timestr)
        start_btn = Button(root, text ="start", command=self.set_start).pack(side=LEFT)
        stop_btn = Button(root, text="stop", command=self.set_stop).pack(side=LEFT)
        reset_btn = Button(root, text="reset", command=self.set_reset).pack(side=LEFT)
        quit_btn = Button(root, text="quit", command=root.quit).pack(side=LEFT)
        self.set_time(self.elapsedtime)
        sw_label.place(x=10,y=100)

    def set_start(self):
        if not self.runing:
            self.start = time.time() - self.elapsedtime
            self.set_update()
            self.runing = 1

    def set_time(self,time):
        min = int(time/60)
        sec = int(time - min*60)
        hsec = int((time - min*60 - sec)*100)
        self.timestr.set('%02d:%02d:%02d'%(min,sec,hsec))

    def set_stop(self):
        if self.runing:
            self.after_cancel(self.timer)
            self.elapsedtime = time.time() - self.start
            self.set_time(self.elapsedtime)
            self.runing = 0

    def set_reset(self):
        self.start = time.time()
        self.elapsedtime = 0.0
        self.set_time(self.elapsedtime)

    #set update is call it self!
    def set_update(self):
        print("hi")
        self.elapsedtime = time.time() - self.start
        self.set_time(self.elapsedtime)
        self.timer = self.after(20,self.set_update)

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()
#set the size
root.geometry("400x300")
# creation of an instance
app = Window(root)
# mainloop
root.mainloop()