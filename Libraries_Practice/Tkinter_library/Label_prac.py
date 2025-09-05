
from tkinter import *

# padx=30, pady=300
root = Tk()
root.geometry('1100x700')

f1 = Frame(root, bg="black", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)
label1 = Label(f1, text="Project Menu ")
label1.pack(fill=Y)
f2 = Frame(root, bg="black", borderwidth=6, relief=SUNKEN)
f2.pack(side=TOP, fill=X)
label2 = Label(f2, text="View Menu")
label2.pack()



root.mainloop()





