from tkinter import *

window = Tk()
window.title("Scale")
window.geometry("500x640")
button = Button(window,
                text="Submit",
                bg="#000000",
                fg="red",
                command=lambda: print(f"The temperature is {scale.get()} degrees celsius"))
button.pack(side=BOTTOM, anchor=S)

fire_image = PhotoImage(file="Fire.png")
fire_label = Label(window,
                   image=fire_image)
fire_label.pack()

ice_image = PhotoImage(file="Ice.png")
ice_label = Label(window,
                  image=ice_image)
ice_label.pack(side=BOTTOM, anchor=S)

scale = Scale(window,
              from_=100,
              to=0,
              length=400,
              bg="#000000",
              fg="red",
              orient=VERTICAL,
              font=("consolas", 12, "bold"),
              tickinterval=10,
              # resolution=5 # Increment of slider
              troughcolor="#69EAFF",
              relief=SUNKEN
              )
scale.pack()

window.mainloop()






