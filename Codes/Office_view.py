from tkinter import *
import tkinter

root12 = Tk()
root12.title('Agent Login Page')
root12.geometry('1166x718-150-80')
root12.resizable(False, False)

bg_home = PhotoImage(file='12.png')
Label(root12, image=bg_home).place(x=0, y=0)

buttonA = Button(root12, text='Available', width=12, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('yu gothic ui', 15, 'bold'), border=0).place(x=510, y=570)
buttonA = Button(root12, text='Sold', width=12, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('yu gothic ui', 15, 'bold'), border=0).place(x=140, y=570)
buttonA = Button(root12, text='Rented', width=12, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('yu gothic ui', 15, 'bold'), border=0).place(x=910, y=565)

fname = Entry(root12, width=15, fg='black', border=0, bg='#ECEADA', font=('Microsoft YaHei UI Light', 15)).place(x=239, y=233)
lname = Entry(root12, width=15, fg='black', border=0, bg='#ECEADA', font=('Microsoft YaHei UI Light', 15)).place(x=752, y=233)
contact = Entry(root12, width=15, fg='black', border=0, bg='#ECEADA', font=('Microsoft YaHei UI Light', 15)).place(x=252, y=283)
email = Entry(root12, width=15, fg='black', border=0,  bg='#ECEADA', font=('Microsoft YaHei UI Light', 15)).place(x=682, y=283)
aid = Entry(root12, width=15, fg='black', border=0, bg='#ECEADA', font=('Microsoft YaHei UI Light', 15)).place(x=150, y=178)

root12.mainloop()
