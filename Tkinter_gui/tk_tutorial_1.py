from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self,master)
        #master is master widget
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("lalala")

        #pack 은 부모의 위젯을 사용할 수 있게 도와준다.
        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="exit")

        quitButton.place(x=0, y=0)

root = Tk()

root.geometry("400x300")

app = Window(root)

root.mainloop()