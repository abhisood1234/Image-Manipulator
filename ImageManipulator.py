import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import simpledialog as sd
from PIL import Image
from PIL import Image, ImageFilter
im = ""
imagefile = ""
def exit():
    answer = messagebox.askyesno("Confirm","Are you sure you want to exit?")
    if answer == True:
        messagebox.showinfo("Information","Software created by Abhinav")
        window.destroy()
def directions():
    messagebox.showinfo("Directions", "Use edit button to edit your photo. Press file button to save your picture")
def version():
    messagebox.showinfo("Version","Version 1.0")
def openimage():
    global imagefile
    imagefile = fd.askopenfilename(title = "Selct Image file",filetype=(("JPEG FILES","*.jpg"),("BMP Files","*.bmp")))
    print(imagefile)
    global im
    im = Image.open(imagefile)
    im.show()
def saveas():
    global imagefile
    imagefile = sd.askstring(title = "Test",prompt = "Enter the file name")
    global im
    im.save(imagefile)
    messagebox.showinfo("Information","Image successfully saved")
def save():
    global imagefile
    global im
    if imagefile == "":
        saveas()
    else:
        im.save(imagefile)
        messagebox.showinfo("Information","Image successfully saved")
def rotate():
    global im
    if im == "":
        openimage()
    angle = sd.askstring(title = "Angle",prompt = "Enter the angle to rotate")
    angle = int(angle)
    im = im.rotate(angle)
    im.show()
    messagebox.showinfo("Information","Image successfully rotated")
def crop():
    global im
    if im == "":
        openimage()
    leftpoint = sd.askstring(title = "Left point", prompt = "Enter the left point")
    leftpoint = int(leftpoint)
    rightpoint = sd.askstring(title = "Right point", prompt = "Enter the right point")
    rightpoint = int(rightpoint)
    toppoint = sd.askstring(title = "Top point",prompt = "Enter the top point")
    toppoint = int(toppoint)
    bottompoint = sd.askstring(title = "Bottom Point", prompt = "Enter the bottom point")
    bottompoint = int(bottompoint)
    im = im.crop((leftpoint,rightpoint,toppoint,bottompoint))
    im.show()
    messagebox.showinfo("Information","Image successfully cropped")
def blurimage():
    global im
    if im == "":
        openimage()
    im = im.filter(ImageFilter.BLUR)
    im.show()
    messagebox.showinfo("Information","Image successfully blurred")
def GrayScale():
    global im
    if im == "":
        openimage()
    im = im.convert('L')
    im.show()
    messagebox.showinfo("Information","Image successfully grayed")

def Thumbnail():
    global im
    if im == "":
        openimage()
    leftpoint = sd.askstring(title = "Left point", prompt = "Enter the left point")
    leftpoint = int(leftpoint)
    rightpoint = sd.askstring(title = "Right point", prompt = "Enter the right point")
    rightpoint = int(rightpoint)
    im.thumbnail((leftpoint,rightpoint))
    im.show()
    messagebox.showinfo("Information","Watermark successfully inserted onto image")
        
        
    
                 
window = Tk()
window.geometry("500x100")
window.resizable(0,0)
l1 = Label(window,text = "Image Manipulator v 1.0",font = "Times 16 bold", fg= "red")
l1.grid(row = 0, column = 0,padx = 125,pady = 35 )
menubar = Menu(window)
filemenu = Menu(menubar)

filemenu.add_command(label="Open Image",command=openimage)

filemenu.add_command(label="Save Image",command = save)

filemenu.add_command(label = "Save as Image",command = saveas)

filemenu.add_command(label = "Exit",command = exit)

menubar.add_cascade(label = "File", menu=filemenu)

editmenu = Menu(menubar)

editmenu.add_command(label="Rotate",command = rotate)

editmenu.add_command(label = "Crop",command = crop)

editmenu.add_command(label = "Blur",command = blurimage)

editmenu.add_command(label = "Gray Scale",command = GrayScale)

editmenu.add_command(label = "Watermark",command = Thumbnail)

menubar.add_cascade(label = "Edit", menu= editmenu)

helpmenu = Menu(menubar)

helpmenu.add_command(label = "Directions",command = directions)

helpmenu.add_command(label = "Version",command = version)

menubar.add_cascade(label = "Help",menu = helpmenu)
                     

window.config(menu=menubar)
