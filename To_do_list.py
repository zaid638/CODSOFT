from cProfile import label
from logging import root
import tkinter
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+30")
root.resizable(False, False)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    f2 = open('tasklist.txt','a')
    f2.write(f"{task}\n")
    task_list.append(f"{task}\n")
    listbox.insert(END, task)  
    f2.close()


def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)

    f3 = open('tasklist.txt','w')
    for tsk in task_list:
        f3.write(f"{tsk}")
    f3.close()
    listbox.delete(ANCHOR)


def openTaskFile():

    global task_list
    f1 = open('tasklist.txt','r')
    tasks = f1.readlines()

    for task in tasks:
        task_list.append(task)
        listbox.insert(END, task)    
    f1.close()  


#icon
image_icon = PhotoImage(file="design3.png")
root.iconphoto(False, image_icon)

#top bar
TopImage = PhotoImage(file="design1.png")
Label(root, image=TopImage).pack()


heading = Label(root, text='ALL TASK', font='arial 20 bold', fg='white', bg='#32405b')
heading.place(x=130, y=30)

#main
frame = Frame(root, width=400, height=50, bg='white')
frame.place(x=0, y=150)

task = StringVar()
task_entry = Entry(frame, width=18, font='arial 20', bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text='ADD', font='arial 20 bold', width=6, bg='#5a95ff', fg='#fff', bd=0, command=addTask)
button.place(x=300, y=0)

#listbox
frame1 = Frame(root, bd=3, width=700, height=280, bg='#32405b')
frame1.pack(pady=(50,0))

listbox = Listbox(frame1, font=('arial',12), width=40, height=16, bg='#32405b', fg='white', cursor='hand2', selectbackground='#5a95ff')
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)

scrollbar2 = Scrollbar(root, orient=HORIZONTAL)
scrollbar2.pack(side=BOTTOM, fill=X)

listbox.config(yscrollcommand=scrollbar.set, xscrollcommand=scrollbar2.set)
scrollbar.config(command=listbox.yview)
scrollbar2.config(command=listbox.xview)

#delete
Delete_icon = PhotoImage(file="design5.png")
Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=TOP, pady=30) 

openTaskFile()

root.mainloop()
