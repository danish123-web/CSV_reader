from tkinter import *

window = Tk()

def TkinterFile(height, width, title):
    window.title(title)
    w=height
    h=width
    sw=window.winfo_screenwidth()
    sh=window.winfo_screenheight()
    x=(sw/2)-(w/2)
    y=(sh/2)-(h/2)
    window.geometry("%dx%d+%d+%d" % (w,h,x,y))
    window.mainloop()