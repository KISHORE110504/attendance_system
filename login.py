from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        self.bg = ImageTk.PhotoImage(file=r"Images\real_black.png")


if __name__ == "__main__":
    root = Tk()
    obj = Login_Window(root)
    root.mainloop()
