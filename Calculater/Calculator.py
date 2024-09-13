import tkinter
from tkinter import *

root = Tk()
root.title("CALCULATOR")
root.geometry("570x600+300+50")
root.resizable(False,False)
root.configure(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation += value
    display.config(text=equation)

def clear():
    global equation
    equation = ""
    display.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    display.config(text=result)


display = Label(root, width=25, height=2, text="", font=("arial",30), bg="#5C5470", fg="#DDE6ED")
display.pack(padx=15, pady=15)

Button(root, text="7", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("7")).place(x=10, y=125) 
Button(root, text="8", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("8")).place(x=150, y=125) 
Button(root, text="9", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("9")).place(x=290, y=125) 
Button(root, text="*", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("*")).place(x=430, y=125) 

Button(root, text="4", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("4")).place(x=10, y=220) 
Button(root, text="5", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("5")).place(x=150, y=220) 
Button(root, text="6", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("6")).place(x=290, y=220) 
Button(root, text="/", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("/")).place(x=430, y=220) 

Button(root, text="1", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("1")).place(x=10, y=320) 
Button(root, text="2", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("2")).place(x=150, y=320) 
Button(root, text="3", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3")).place(x=290, y=320) 
Button(root, text="-", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("-")).place(x=430, y=320) 

Button(root, text="C", width=11, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#3695f5", command=clear).place(x=10, y=510) 
Button(root, text="0", width=11, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0")).place(x=10, y=415) 
Button(root, text=".", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(".")).place(x=290, y=415) 
Button(root, text="+", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("+")).place(x=430, y=415) 
Button(root, text="=", width=11, height=1, font=("arial",30,"bold"), bd=1, fg="#fff", bg="#fe9037", command=calculate).place(x=290, y=510) 


root.mainloop()