from tkinter import *
from PIL import Image, ImageTk
root = Tk()                                                             # Important Label options
                                                                        # Text - adds the text
                                                                        # bd - background
                                                                        # fg - foreground
                                                                        # font - sets the font
                                                                        # padx - x padding
                                                                        # pady - y padding
                                                                        #

# Used initially describing the size of the window
root.geometry("349x447")
root.title("Akuma Calculator")

# Used for minimum size of window
# root.minsize(444, 444)

# Used for maximum size of the window
# root.maxsize(444, 444)
# photo = PhotoImage(file="AKuma pic.jpg")

photo = ImageTk.PhotoImage(Image.open("AKuma pic.jpg"))
label1 = Label(image=photo)
label1.pack()
root.mainloop()