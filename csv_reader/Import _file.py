from CenterScreen import *
from tkinter import ttk,messagebox,filedialog
import os
import pandas as pd
from selenium import webdriver

myframe = LabelFrame(window, text ="Import file")
myframe.pack(fill=BOTH, expand=True, padx=30, pady=10)

myframebtn=LabelFrame(window,text="Open File Dialog")
myframebtn.pack(fill=X,expand=True,padx=10)

lbl=Label(myframebtn, text="No File Selected", font=("times",15,"bold"),fg="blue")
lbl.grid(row=0,column=0,padx=10,pady=10)

def File_dialogue():
    filename=filedialog.askopenfilename(initialdir="/home/danish", title="Selct A File", filetypes=(("csv Files", "*.csv"),("xlsx Files","*.xlsx")))
    lbl["text"]=filename
    return None

def Load_data():
    file_path=lbl["text"]

    try:
        excel_filename=r"{}".format(file_path)
        filename,fileextension=os.path.splitext(excel_filename)
        if fileextension == ".xlsx":
            df = pd.read_excel(excel_filename)
        elif fileextension == ".csv":
            df = pd.read_csv(excel_filename)
    except ValueError:
        messagebox.showinfo("Messag","File is invalid")
        return None
    except FileNotFoundError:
        messagebox.showinfo("Message",f"No such files : {file_path}")
        return None

    treeview["column"] = list(df.columns)
    treeview["show"] = "headings"
    for column in treeview["column"]:
        treeview.heading(column, text=column)
    
    DataFrameRows = df.to_numpy().tolist()
    for row in DataFrameRows:
        treeview.insert("","end",values=row)

def browsing():
    selectedItem = treeview.selection()[0]
    link = treeview.item(selectedItem)['values'][1]
    driver = webdriver.Chrome(executable_path = '/path/to/geckodriver')
    driver.get(link)


treeview=ttk.Treeview(myframe)
treeview.place(relheight=1,relwidth=1)

btnBrowse=Button(myframebtn,text="Browse",bg="#1289A7", width=10,fg="white", font=("times",16,"bold"), command=File_dialogue)
btnBrowse.grid(row=1,column=0,padx=10,pady=20)

btnimport=Button(myframebtn,text="IMPORT",bg="#10ac84", width=10,fg="white", font=("times",16,"bold"), command=Load_data)
btnimport.grid(row=1,column=1,padx=10,pady=20)

btnopen=Button(myframebtn,text="Open Browser",bg="#10ac84", width=10,fg="white", font=("times",16,"bold"), command=browsing)
btnopen.grid(row=1,column=2,padx=10,pady=20)

TkinterFile(1000, 500, "Import csv file")


