# Entry Widget = Textbox that accepts a single line of user input
from tkinter import *
def query():
    user_query = entry1.get()
    print(user_query)
    # entry1.config(state=DISABLED)

def delete():
    entry1.delete(0, END)


def backspace():
    entry1.delete(len(entry1.get())-1, END)

window = Tk()
window.geometry("444x444")

entry1 = Entry(window,
               bg="black",
               fg="#00FF00",
               font=("Arial", 15, "bold"),
               bd=3,
               relief=SUNKEN,
               insertbackground="#00FF00",     # <--- Cursor color
               # show="*",
               )
entry1.pack()

entry1.insert(0, "Write here..")
submit_button = Button(window,
                       text="Submit",
                       bg="#000000",
                       fg="#00FF00",
                       activebackground="#000000",
                       activeforeground="#00FF00",
                       command=query)
submit_button.pack()
delete_button = Button(window,
                       text="Delete",
                       bg="#000000",
                       fg="#00FF00",
                       activebackground="#000000",
                       activeforeground="#00FF00",
                       command=delete)
delete_button.place(x=246, y=32)
backspace_button = Button(window,
                          text="Backspace",
                          bg="#000000",
                          fg="#00FF00",
                          activebackground="#000000",
                          activeforeground="#00FF00",
                          command=backspace)

backspace_button.place(x=131, y=32)
window.mainloop()