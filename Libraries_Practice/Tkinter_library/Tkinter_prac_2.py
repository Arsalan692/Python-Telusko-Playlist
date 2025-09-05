from tkinter import *

root = Tk()
root.title("AKUMA CALCULATOR")
root.geometry("370x444")
# root.maxsize(370, 444)
# root.minsize(370, 444)
text_label = Label(text=f"This is akuma's text and its fun making a calculator\nMY name is Arsalan ",\
background="black", fg="white", padx=50, pady=200, font=("monokai", 12, "bold"), borderwidth=4, relief=SUNKEN)
text_label.pack()
# text_label.pack(anchor="s", side=LEFT, fill=Y, padx=34, pady=20)
root.mainloop()





