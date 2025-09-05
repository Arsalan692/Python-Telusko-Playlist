from tkinter import *
from PIL import Image, ImageTk

def display():
    if x.get() == 1:
        print("You agreed! ")
    elif x.get() == 0:
        print("You disagreed! ")


window = Tk()

x = IntVar()
photo = ImageTk.PhotoImage(Image.open("Akuma_sign_logo.png"))
window.config(bg="#000000")
window.geometry("444x444")
check_button = Checkbutton(window,
                           text="Are you ready to join Akuma",
                           bg="#000000",
                           fg="#00FF00",
                           activeforeground="#00FF00",
                           activebackground="#000000",
                           font=("Arial", 12, "bold", "italic"),
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           image=photo,
                           compound=LEFT
                           )
check_button.pack()
window.mainloop()









