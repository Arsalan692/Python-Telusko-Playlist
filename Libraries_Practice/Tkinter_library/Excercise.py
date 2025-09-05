from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("1100x800")
root.title("Akuma Newspaper")
image1 = ImageTk.PhotoImage(Image.open("AKuma pic.jpg"))
heading_label = Label(text="NEWS 1:", font="monoscape 12 bold")
heading_label.pack(anchor="nw", padx=20)
img_label1 = Label(image=image1, borderwidth=3, bg="black")
img_label1.pack(anchor="nw", padx=20, pady=3)
text1_label = Label(text=f"This is Akuma which is invincible no one can ever defeat him.\n\
 He is the master of martial artsAkuma, known in Japan as Gouki, is a fictional character\n\
 and secondary antagonist of the Street Fighter series of fighting games by Capcom. Akuma\n\
 made his debut in Super Street Fighter II Turbo as a secret character and Boss", bg="black", fg="red",font=(10))
text1_label.pack(anchor="nw", side=LEFT, padx=20, pady=5)





root.mainloop()








