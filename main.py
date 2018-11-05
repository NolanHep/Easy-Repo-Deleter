from tkinter import *
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="Settings", menu=file)
        edit = Menu(menu)
        edit.add_command(label="Login to Github", command=self.showText)
        menu.add_cascade(label="Login", menu=edit)

    def showText(self):
        text = Label(self, text="Opening Github")
        text = Label(self, text="Logged in!")
        text.pack()

    def client_exit(self):
        exit()

root = Tk()

root.geometry("500x400")

app = Window(root)

root.mainloop()
