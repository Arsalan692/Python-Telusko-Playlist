from tkinter import *


def back_space():
    entry_bar.delete(len(entry_bar.get())-1, END)


def delete():
    entry_bar.delete(0, END)


def evalute():
    try:
        value1 = eval(entry_bar.get())
        entry_bar.delete(0, END)
        entry_bar.insert(0, value1)
    except SyntaxError:
        entry_bar.delete(0, END)
        entry_bar.insert(0, "ERROR")
    except ZeroDivisionError:
        entry_bar.delete(0, END)
        entry_bar.insert(0, "♾")


window = Tk()
window.title("Akuma Calculator")
icon_pic = PhotoImage(file="Akuma_logo.png")
window.iconphoto(True, icon_pic)
window.geometry("387x396")
window.minsize(387, 396)
window.maxsize(387, 396)
window.config(bg="#2e2d2d")
entry_bar = Entry(window,
                  bg="black",
                  fg="#00FF00",
                  font=("Comic Sans", 35, "bold"),
                  bd=4,
                  relief=SUNKEN,
                  width=50,
                  insertbackground="#00FF00")
entry_bar.pack()

button_for_0 = Button(window,
                      text="0",
                      pady=10,
                      padx=34,
                      bg="black",
                      fg="#00FF00",
                      font=("Comic Sans", 14, "bold"),
                      bd=3,
                      relief=SUNKEN,
                      activebackground="black",
                      command=lambda: entry_bar.insert(END, 0)
                      )
button_for_0.place(x=0, y=337)

button_for_00 = Button(window,
                       text="00",
                       pady=9.5,
                       padx=31,
                       bg="black",
                       fg="#00FF00",
                       font=("Comic Sans", 14, "bold"),
                       bd=3,
                       relief=SUNKEN,
                       activebackground="black",
                       command=lambda: entry_bar.insert(END, "00")
                       )
button_for_00.place(x=99, y=337)

button_for_dot = Button(window,
                        text=".",
                        pady=9.5,
                        padx=34,
                        bg="black",
                        fg="#00FF00",
                        font=("Comic Sans", 14, "bold"),
                        bd=3,
                        relief=SUNKEN,
                        activebackground="black",
                        command=lambda: entry_bar.insert(END, ".")
                        )
button_for_dot.place(x=203, y=337)

button_for_equal = Button(window,
                          text="=",
                          pady=9.5,
                          padx=31,
                          bg="black",
                          fg="#00FF00",
                          font=("Comic Sans", 14, "bold"),
                          bd=3,
                          relief=SUNKEN,
                          activebackground="black",
                          command=evalute
                          )
button_for_equal.place(x=296, y=337)
button_for_1 = Button(window,
                      text="1",
                      pady=10,
                      padx=34,
                      bg="black",
                      fg="#00FF00",
                      font=("Comic Sans", 14, "bold"),
                      bd=3,
                      relief=SUNKEN,
                      activebackground="black",
                      command=lambda: entry_bar.insert(END, 1)
                      )
button_for_1.place(x=0, y=277)
button_for_4 = Button(window,
                      text="4",
                      pady=10,
                      padx=34,
                      bg="black",
                      fg="#00FF00",
                      font=("Comic Sans", 14, "bold"),
                      bd=3,
                      relief=SUNKEN,
                      activebackground="black",
                      command=lambda: entry_bar.insert(END, 4)
                      )
button_for_4.place(x=0, y=217)
button_for_7 = Button(window,
                      text="7",
                      pady=10,
                      padx=34,
                      bg="black",
                      fg="#00FF00",
                      font=("Comic Sans", 14, "bold"),
                      bd=3,
                      relief=SUNKEN,
                      activebackground="black",
                      command=lambda: entry_bar.insert(END, 7)
                      )
button_for_7.place(x=0, y=157)
button_for_underroot = Button(window,
                              text="√",
                              pady=10,
                              padx=34,
                              bg="black",
                              fg="#00FF00",
                              font=("Comic Sans", 14, "bold"),
                              bd=3,
                              relief=SUNKEN,
                              activebackground="black",
                              command=lambda: entry_bar.insert(0, int(entry_bar.get())**0.5)
                              )
button_for_underroot.place(x=0, y=97)
label1 = Label(window,
               text="CREATED BY AKUMA",
               width=32,
               padx=80,
               height=1,
               bg="black",
               fg="#00FF00",
               bd=3,
               relief=SUNKEN,
               font=("COMIC SANS", 14, "bold", "italic"))
label1.pack()
button_for_2 = Button(window,
                      text="2",
                      pady=9.5,
                      padx=36,
                      bg="black",
                      fg="#00FF00",
                      font=("Comic Sans", 14, "bold"),
                      bd=3,
                      relief=SUNKEN,
                      activebackground="black",
                      command=lambda: entry_bar.insert(END, 2)
                      )
button_for_2.place(x=99, y=277)
button_for_3 = Button(window,
                      text="3",
                      pady=10,
                      padx=31,
                      bg="black",
                      fg="#00FF00",
                      font=("Comic Sans", 14, "bold"),
                      bd=3,
                      relief=SUNKEN,
                      activebackground="black",
                      command=lambda: entry_bar.insert(END, 3)
                      )
button_for_3.place(x=203, y=277)
button_for_plus = Button(window,
                         text="+",
                         pady=9.5,
                         padx=31,
                         bg="black",
                         fg="#00FF00",
                         font=("Comic Sans", 14, "bold"),
                         bd=3,
                         relief=SUNKEN,
                         activebackground="black",
                         command=lambda: entry_bar.insert(END, "+")
                         )
button_for_plus.place(x=296, y=277)
button_for_5 = Button(window,
                      text="5",
                      pady=9.5,
                      padx=36,
                      bg="black",
                      fg="#00FF00",
                      font=("Comic Sans", 14, "bold"),
                      bd=3,
                      relief=SUNKEN,
                      activebackground="black",
                      command=lambda: entry_bar.insert(END, 5)
                      )
button_for_5.place(x=99, y=217)
button_for_6 = Button(window,
                      text="6",
                      pady=10,
                      padx=31,
                      bg="black",
                      fg="#00FF00",
                      font=("Comic Sans", 14, "bold"),
                      bd=3,
                      relief=SUNKEN,
                      activebackground="black",
                      command=lambda: entry_bar.insert(END, 6)
                      )
button_for_6.place(x=203, y=217)
button_for_minus = Button(window,
                          text="−",
                          pady=9.5,
                          padx=31,
                          bg="black",
                          fg="#00FF00",
                          font=("Comic Sans", 14, "bold"),
                          bd=3,
                          relief=SUNKEN,
                          activebackground="black",
                          command=lambda: entry_bar.insert(END, "-")
                          )
button_for_minus.place(x=296, y=217)
button_for_8 = Button(window,
                      text="8",
                      pady=9.5,
                      padx=36,
                      bg="black",
                      fg="#00FF00",
                      font=("Comic Sans", 14, "bold"),
                      bd=3,
                      relief=SUNKEN,
                      activebackground="black",
                      command=lambda: entry_bar.insert(END, 8)
                      )
button_for_8.place(x=99, y=157)
button_for_9 = Button(window,
                      text="9",
                      pady=10,
                      padx=31,
                      bg="black",
                      fg="#00FF00",
                      font=("Comic Sans", 14, "bold"),
                      bd=3,
                      relief=SUNKEN,
                      activebackground="black",
                      command=lambda: entry_bar.insert(END, 9)
                      )
button_for_9.place(x=203, y=157)
button_for_multiply = Button(window,
                             text="×",
                             pady=9.5,
                             padx=31,
                             bg="black",
                             fg="#00FF00",
                             font=("Comic Sans", 14, "bold"),
                             bd=3,
                             relief=SUNKEN,
                             activebackground="black",
                             command=lambda: entry_bar.insert(END, "*")
                             )
button_for_multiply.place(x=296, y=157)
button_for_CE = Button(window,
                       text="CE",
                       pady=13,
                       padx=32,
                       bg="black",
                       fg="#00FF00",
                       font=("Comic Sans", 13, "bold"),
                       bd=3,
                       relief=SUNKEN,
                       activebackground="black",
                       command=delete
                       )
button_for_CE.place(x=99, y=97)
button_for_backspace = Button(window,
                              text="⌫",
                              pady=13,
                              padx=27,
                              bg="black",
                              fg="#00FF00",
                              font=("Comic Sans", 13, "bold"),
                              bd=3,
                              relief=SUNKEN,
                              activebackground="black",
                              command=back_space
                              )
button_for_backspace.place(x=203, y=97)
button_for_divide = Button(window,
                           text="÷",
                           pady=9.5,
                           padx=31,
                           bg="black",
                           fg="#00FF00",
                           font=("Comic Sans", 14, "bold"),
                           bd=3,
                           relief=SUNKEN,
                           activebackground="black",
                           command=lambda: entry_bar.insert(END, "/")
                           )
button_for_divide.place(x=297, y=97)


window.mainloop()
