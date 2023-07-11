from typing import Optional, Tuple, Union
from customtkinter import CTkFrame, set_appearance_mode
from tkinter import PhotoImage, Tk
import customtkinter

from utils import Assets
from present import *

class Main(Tk):
    def __init__(self):
        super().__init__()

        container = CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for f in [HomePage]:
            page = f.__name__
            frame = f(container, self)
            frame.grid(row=0, column=0, sticky="NSEW")
            self.frames[page] = frame

        self.show_frame

    def show_frame(self, page, id=None):
        self.id = id
        self.frames[page].tkraise()


set_appearance_mode("Light")

app = Main()
app.title("SaLitrato")
app.resizable(True, True)
width = 1024
height = 576
x = (app.winfo_screenwidth()/2) - width/2
y = (app.winfo_screenheight()/2) - height/2
app.geometry('%dx%d+%d+%d' % (width, height, x, y))
app.minsize(1024, 576)
app.iconphoto(True, PhotoImage(file=Assets.asset_path('salitrato_icon.png')))

    
def Folder():
    new_window=customtkinter.CTkToplevel(app)
    new_window.title("New Folder")
    new_window.geometry("300x200")
    
    label1 = customtkinter.CTkLabel(new_window,text="Add Folder")
    label1.pack()
    
    
    # will get user entry 
    user_entry=customtkinter.CTkEntry(new_window, width=30,height=1)
    user_entry.pack(padx= 10, pady= 10)
    
    #Small box that houses cancel and save buttons
    newFrame = customtkinter.CTkFrame(new_window,bg_color="#ffffff")
    newFrame.pack(padx=10, pady=50)
    
    # button for cancel
    btn1 = customtkinter.CTkButton(newFrame, text="Cancel",
                   command=new_window)
    btn1.pack(side="LEFT",padx=15, pady=20)
    
    # button for save
    btn2 = customtkinter.CTkButton(newFrame, text="Save",
                   command=new_window)
    btn2.pack(side="LEFT",padx=15, pady=20)
    
# button widget which will open a new window to add new folder
Add_Folder = customtkinter.CTkButton(app,text="Add Folder", corner_radius=3, hover_color="#18308f" ,command=Folder)
Add_Folder.pack(side="left",fill="both", expand="False",padx=35, pady=20)

app.mainloop()

