# Radio button = Similar to checkbox , but you can only select one from a group
from tkinter import *

def order():
    if x.get() == 0:
        print("Burger")
    elif x.get() == 1:
        print("Pizza")
    elif x.get() == 2:
        print("Roll")

window = Tk()
x = IntVar()
window.config(bg="#000000")
window.geometry("444x444")

food = ["Burger", "Pizza", "Roll"]

for i in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[i],  # add text to radio buttons
                               variable=x,    # Groups radiobuttons together if they share the same variable
                               value=i,        # Assigns each radio button a different value
                               bg="#000000",
                               fg="#00FF00",
                               font=("Arial", 12, "bold"),
                               activebackground="#000000",
                               activeforeground="#00FF00",
                               padx=180,
                               indicatoron=False,
                               command=order,
                               width=375
                               )
    radio_button.pack(anchor=W)

window.mainloop()