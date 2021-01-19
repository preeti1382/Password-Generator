import string
import random
from tkinter import *
from PIL import Image , ImageTk


root = Tk()

canvas = Canvas(root , height="200")  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("lock.png"))  
canvas.create_image(-100, -100, anchor=NW, image=img) 


root.geometry("500x500")
root.title("Generate Password")

# some other variables for difficulty level of password
poor = string.ascii_lowercase + string.ascii_uppercase
medium = string.ascii_letters + string.digits
advanced = string.ascii_letters + string.digits + string.punctuation
choice = IntVar()
title = StringVar()
lengthlabel = StringVar()
passlength = IntVar()
result = StringVar()
# password = StringVar()

# function for selecting difficulty level
def selection() :
    choice.get()


# function to generate the password
def gen_password():
    password = ""
    if(choice.get() == 1):
        password = password.join(random.sample(poor, passlength.get()))
    elif(choice.get() == 2):
        password = password.join(random.sample(medium, passlength.get()))
    elif(choice.get() == 3):
        password = password.join(random.sample(advanced, passlength.get()))
    else :
        password = "Try again!"
    result.set(password)


#user interface
label = Label(root , textvariable = title).pack()

title.set("The strength of the password:")

R1 = Radiobutton(root, text="Poor", variable=choice, value=1, command=selection).pack(anchor=CENTER)
R2 = Radiobutton(root, text="Medium", variable=choice, value=2, command=selection).pack(anchor=CENTER)
R3 = Radiobutton(root, text="Advanced", variable=choice, value=3, command=selection).pack(anchor=CENTER)

lengthlabel.set("Password length: (8 to 24)")
lengthtitle = Label(root, textvariable=lengthlabel).pack()

spinboxlength = Spinbox(root, from_=8, to_=24, textvariable=passlength, width=13).pack()

passgenButton = Button(root, text="Generate Password", command=gen_password)
passgenButton.pack(pady = 7)

# result.set(password)
result1 = Entry(root , textvariable=result).pack(pady = 3) 

root.mainloop()
