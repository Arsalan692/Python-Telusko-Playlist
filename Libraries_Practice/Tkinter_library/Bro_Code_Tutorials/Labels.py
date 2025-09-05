# LABELS = An area widget that holds text and/or an image within a window
from tkinter import *

window = Tk()
window.geometry("400x400")
window.config(bg="black")
photo = PhotoImage(file="Akuma_logo.png")

label1 = Label(window,
               text="Hey Akuma",
               font=("Arial", 30, "bold"),
               foreground="#00FF00",
               background="red",
               relief=RAISED,
               borderwidth=5,
               padx=15,
               pady=10,
               image=photo,
               compound="left")
label1.pack()
# label1.place(x=0,y=0)
window.mainloop()

