from tkinter import *
import os
from tkinter import ttk
from tkinter import messagebox
import tkinter
import random
import datetime

counter=None
with open('count.txt', 'r') as f:
    counter = f.readlines()[0]


def submit(*args):
    global counter
    try:
        file = open('4digitcodes.txt', 'r') #sold codes file
        lines = file.readlines()
        new_lines=[]
        for x in lines:
            new_lines.append(x.strip())
        cde = code.get().lower().replace(" ", "") #get what they entered
        file.close()
        if cde=="":
            pass
        elif str(cde) in new_lines:
            fileout= open('4digitcodes.txt', 'a') #codes file
            code.set("")
            for x in new_lines:
                if x == cde:
                    new_lines.remove(cde)
            for x in new_lines:
                fileout.write(x+'\n')
            fileout.close()
            now = datetime.datetime.now()
            data=cde+ " was used to access door at "+ str(now)
            fileout = open('4digitcodes.txt', 'a')# codes file
            fileout.write(data+'\n')

    except ValueError:
        pass



root = Tk()
root.title("Security Door")
code=StringVar()
style = ttk.Style()

mainframe = tkinter.Frame(root,width=1024,height=600)
mainframe.grid(column=0, row=0, sticky=(N, W))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
content = ttk.Frame(root, padding=(1,1,1,1))
frame = tkinter.Frame(content, borderwidth=5, relief="sunken", bg="firebrick3",width=1300, height=800)
code_entrylbl = Label(content, text="ENTER CODE HERE", bg="firebrick3")
code_entry = ttk.Entry(content, width=30, textvariable=code,font=("Courier", 22))
code_entrylbl.config(width=20)
code_entrylbl.config(font=("Courier", 32))


content.grid(column=0, row=0, sticky=(W))
enter_button=tkinter.Button(content,font=("Courier", 22), text="ENTER",bg="light blue",width=20,command=submit).grid(column=0,row=2,sticky=(N))
frame.grid(column=0, row=0, rowspan=3, sticky=(W))
code_entrylbl.grid(column=0, row=0, sticky=(S), padx=1)
code_entry.grid(column=0, row=1, sticky=(N), pady=1, padx=1)
def character_limit(entry_text):
    if len(entry_text.get()) > 0:
        code.set(code.get()[:4])
code.trace("w", lambda *args: character_limit(code))

code_entry.focus()
root.bind('<Return>', submit)
root.mainloop()
