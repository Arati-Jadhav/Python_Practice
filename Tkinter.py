from tkinter import *
from PIL import Image ,ImageTk

#Que:-> other than tkinter what are other ways to create the GUI in python?
# root is object of tk class
root = Tk()

#width x height
root.geometry("500x500")
# #fix the minimum size of window
root.minsize(200,200)
#
# #fix the maximum size of window
root.maxsize(200,200)

# lable using text
# new_lable =Label(text="Dmart_billing_GUI")
# new_lable.pack()

# add image as lable
# for png file
# photo = PhotoImage(file="Ballons.png")

# for other format file like jpg,jfifi we install pillow
image =Image.open("images.jfif")
photo = ImageTk.PhotoImage(image)

image_lable =Label(image=photo)
image_lable.pack()


#to create new GUI window
root.mainloop()
