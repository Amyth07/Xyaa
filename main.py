from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import tkinter.colorchooser
from tkinter.colorchooser import askcolor
import datetime
from tkinter.filedialog import askopenfilename, asksaveasfilename


def Open():
    text.delete(1.0, END)
    file = open(askopenfilename(), "r")
    if file != "":
        txt = file.read()
        text.insert(INSERT, txt)
    else:
        pass


def save():
    filename = asksaveasfilename()
    if filename:
        alltext = text.get(1.0, END)
        open(filename, "w").write(alltext)


def copy():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())


def paste():
    try:
        teext = text.selection_get(selection="CLIPBOARD")
        text.insert(INSERT, teext)
    except:
        tkMessageBox.showerror("Error", "Nothing to Paste !")


def clear():
    sel = text.get(SEL_FIRST, SEL_LAST)
    text.delete(SEL_FIRST, SEL_LAST)


def clearall():
    text.delete(1.0, END)


def background():
    (triple, color) = askcolor()
    if color:
        text.config(background=color)


def about():
    ab = Toplevel(core)
    txt = "This is a simple GUI based Text-editor \n Author: Amit"
    la = Label(ab, text=txt, foreground="blue")
    la.pack()


def line():
    lin = "_" * 217
    text.insert(INSERT, lin)


def date():
    data = datetime.date.today()
    text.insert(INSERT, data)


def normal():
    text.config(font=("NewTimesRoman", 15))


def bold():
    text.config(font=("NewTimesRoman", 15, "bold"))


def underline():
    text.config(font=("NewTimesRoman", 15, "underline"))


def italic():
    text.config(font=("NewTimesRoman", 15, "italic"))


def font():
    (triple, color) = askcolor()
    if color:
        text.config(foreground=color)


def kill():
    core.destroy()


core = Tk()
core.title("Xyaa")
menu = Menu(core)


filemenu = Menu(core)
core.config(menu=menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=Open)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Exit", command=kill)

modifymenu = Menu(core)
menu.add_cascade(label="Modify", menu=modifymenu)
modifymenu.add_command(label="Copy", command=copy)
modifymenu.add_command(label="Paste", command=paste)
modifymenu.add_command(label="Clear", command=clear)
modifymenu.add_command(label="ClearAll", command=clearall)


insertmenu = Menu(core)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Date", command=date)
insertmenu.add_command(label="Line", command=line)


formatmenu = Menu(menu)
menu.add_cascade(label="Format", menu=formatmenu)
formatmenu.add_cascade(label="Color", command=font)
formatmenu.add_separator()
formatmenu.add_radiobutton(label="Normal", command=normal)
formatmenu.add_radiobutton(label="Bold", command=bold)
formatmenu.add_radiobutton(label="Underline", command=underline)
formatmenu.add_radiobutton(label="Italic", command=italic)


Personalize = Menu(core)
menu.add_cascade(label="Personalize", menu=Personalize)
Personalize.add_command(label="Background", command=background)


helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)

text = Text(core, height=100, width=400, font=("NewTimesRoman", 15))
scroll = Scrollbar(core, command=text.yview)

scroll.config(command=text.yview)

text.config(yscrollcommand=scroll.set)

scroll.pack(side=RIGHT, fill=Y)

text.pack()

core.resizable(15, 15)


core.mainloop()
