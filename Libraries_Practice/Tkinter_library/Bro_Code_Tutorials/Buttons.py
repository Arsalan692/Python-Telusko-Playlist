# button = You click it, then it does stuff
from tkinter import *

count = 0

def click():
    global count
    count += 1
    if count > 1:
        print(f"You have disturbed me {count} times")
    else:
        print(f"You have disturbed me {count} time")

window = Tk()
window.geometry("444x444")
photo = PhotoImage(file="Akuma_logo.png")
button1 = Button(window,
                 text="I am Akuma",
                 command=click,
                 font=("Comic Sans", 12, "bold"),
                 foreground="#00FF00",
                 bg="#000000",
                 bd=4,
                 relief=RAISED,
                 activeforeground="#00FF00",
                 activebackground="#000000",
                 state=ACTIVE,
                 image=photo,
                 compound="bottom")

button1.pack()
window.mainloop()









