from tkinter import *
import tkinter

root = Tk()
root.title('Home Page')
root.geometry('1166x718-150-80')
root.resizable(False, False)

bg_home = PhotoImage(file='1.png')
Label(root, image=bg_home).place(x=0, y=0)


def agent_signin():
    root1 = Toplevel(root)
    root1.title('Agent Login Page')
    root1.geometry('1166x718-150-80')
    root1.resizable(False, False)

    bg_home = PhotoImage(file='2.png')
    Label(root1, image=bg_home).place(x=0, y=0)

    user = Entry(root1, width = 15, fg = 'black', border = 0, bg = '#E7E2D9', font = ('Microsoft YaHei UI Light', 15))
    user.place(x = 645, y = 273)

    password = Entry(root1, width = 15, fg = 'black', border = 0, bg = '#E7E2D9', font = ('Microsoft YaHei UI Light', 15))
    password.place(x = 645, y = 380)

    buttonA = Button(root1, text='Sign In', width=19, background='#735E59', foreground='white', activebackground='#735E59',activeforeground='black', font=('yu gothic ui', 15, 'bold'), border=0).place(x=642, y=512)

    root1.mainloop()


buttonA = Button(root, text='Agent', width=9, background='white', foreground='black', activebackground='white',activeforeground='#735E59', font=('yu gothic ui', 28, 'bold'), border=0,command =agent_signin).place(x=200, y=539)
buttonO = Button(root, text='Office', width=9, background='white', foreground='black', activebackground='white',activeforeground='#735E59', font=('yu gothic ui', 30, 'bold'), border=0).place(x=770, y=540)

root.mainloop()
