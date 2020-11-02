
#Простой калькулятор на Питоне 

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from tkinter import messagebox
def proces():
    try:
        number1=Entry.get(E1)
        number2=Entry.get(E2)
        operator=Entry.get(E3)
        number1=int(number1)
        number2=int(number2)
        if operator =="+":
            answer=number1+number2
        if operator =="-":
            answer=number1-number2
        if operator=="*":
            answer=number1*number2
        if operator=="/":
            answer=number1/number2
        Entry.insert(E4,0,answer)
        print(answer)
    except ValueError:
        messagebox.showinfo("Warning","Please enter the value in integer")
top = Tk()
top.title("Калькулятор")
L1 = Label(top, text="Простой калькулятор",).grid(row=0,column=1)
L2 = Label(top, text="Значение 1",).grid(row=1,column=0)
L3 = Label(top, text="Значение 2",).grid(row=2,column=0)
L4 = Label(top, text="Символ",).grid(row=3,column=0)
L4 = Label(top, text="Ответ",).grid(row=4,column=0)
E1 = Entry(top, bd =5)
E1.grid(row=1,column=1)
E2 = Entry(top, bd =5)
E2.grid(row=2,column=1)
E3 = Entry(top, bd =5)
E3.grid(row=3,column=1)
E4 = Entry(top, bd =5)
E4.grid(row=4,column=1)
B=Button(top, text ="Выполнить",command = proces).grid(row=5,column=1,)
top.mainloop()





