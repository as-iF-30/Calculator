#BLL
from tkinter import *
expression=""
def num(n):
    global expression
    expression = expression + str(n)
    equ.set(expression)
def clean():
    global expression
    expression=""
    equ.set("")
def result():
    try:
        global expression
        total = str(eval(expression))
        equ.set(total)
        expression=""
    except:
        equ.set("Error in euation")
        expression = ""
#PLL
if __name__ == "__main__":
    root = Tk()
    root.geometry("330x300")
    root.title('Calculator')
    root.configure(background = 'black')
#Entry text
    equ = StringVar()
    entry_text=Entry(root, textvariable=equ, font=('ariel',15))
    equ.set("Enter your equtaion")
    entry_text.place(x=65, y=20)
    #Button
    bcl=Button(root, text='clear', bg='yellow', height=1, width=3)
    bcl.place(x=295, y=20)
    bcl.config(command=clean)
    b1=Button(root, text='1', bg='grey', height=2, width=4)
    b1.place(x=50, y=60)
    b1.config(command=lambda:num(1))
    b2=Button(root, text='2', bg='grey', height=2, width=4)
    b2.place(x=100, y=60)
    b2.config(command=lambda:num(2))
    b3=Button(root, text='3', bg='grey', height=2, width=4)
    b3.place(x=150, y=60)
    b3.config(command=lambda:num(3))
    b4=Button(root, text='-', bg='red',height=2, width=4)
    b4.place(x=220, y=60)
    b4.config(command=lambda:num('-'))
    b5=Button(root, text='+', bg='red',height=2, width=4)
    b5.place(x=270, y=60)
    b5.config(command=lambda:num('+'))
    b6=Button(root, text='4', bg='grey',height=2, width=4)
    b6.place(x=50, y=120)
    b6.config(command=lambda:num(4))
    b7=Button(root, text='5', bg='grey',height=2, width=4)
    b7.place(x=100, y=120)
    b7.config(command=lambda:num(5))
    b8=Button(root, text='6', bg='grey',height=2, width=4)
    b8.place(x=150, y=120)
    b8.config(command=lambda:num(6))
    b9=Button(root, text='*', bg='red',height=2, width=4)
    b9.place(x=220, y=120)
    b9.config(command=lambda:num('*'))
    b10=Button(root, text='/', bg='red',height=2, width=4)
    b10.place(x=270, y=120)
    b10.config(command=lambda:num('/'))
    b11=Button(root, text='7', bg='grey',height=2, width=4)
    b11.place(x=50, y=180)
    b11.config(command=lambda:num(7))
    b12=Button(root, text='8', bg='grey',height=2, width=4)
    b12.place(x=100, y=180)
    b12.config(command=lambda:num(8))
    b13=Button(root, text='9', bg='grey',height=2, width=4)
    b13.place(x=150, y=180)
    b13.config(command=lambda:num(9))
    b14=Button(root, text='%', bg='red',height=2, width=4)
    b14.place(x=220, y=180)
    b14.config(command=lambda:num('%'))
    b15=Button(root, text='**', bg='red',height=2, width=4)
    b15.place(x=270, y=180)
    b15.config(command=lambda:num('**'))
    b16=Button(root, text='=', bg='white', height=2, width=6)
    b16.place(x=245, y=240)
    b16.config(command=result)
    b17=Button(root, text='0', bg='grey',height=2, width=6)
    b17.place(x=50, y=240)
    b17.config(command=lambda:num(0))
    b18=Button(root, text='.', bg='grey',height=2, width=6)
    b18.place(x=120, y=240)
    b18.config(command=lambda:num('.'))
    root.mainloop()
