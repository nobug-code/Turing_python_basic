from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        # master is master widget
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")

        # pack 은 부모의 위젯을 사용할 수 있게 도와준다.
        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit", command = self.client_exit)

        quitButton.place(x=0, y=0)

    def client_exit(self):
        exit()

root = Tk()

root.geometry("400x300")

app = Window(root)

root.mainloop()

#버튼을 하나 더 만들기 , 버튼을 클릭하면 print("hello") 나 특정단어가 출력 되도록 한다.