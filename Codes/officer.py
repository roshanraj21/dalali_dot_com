from tkinter import *
import tkinter

root11 = Tk()
root11.title('Agent Login Page')
root11.geometry('1166x718-150-80')
root11.resizable(False, False)

bg_home = PhotoImage(file='11.png')
Label(root11, image=bg_home).place(x=0, y=0)

selectp= Entry(root11, width = 8, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
selectp.place(x = 445, y = 608)

buttonA = Button(root11, text='Submit', width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 18, 'bold'), border=0).place(x=765, y=605)
# buttonA = Button(root4, text='Buy', width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 28, 'bold'), border=0).place(x=755, y=475)


root11.mainloop()