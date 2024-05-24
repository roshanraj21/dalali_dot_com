from tkinter import *
import tkinter

root8 = Tk()
root8.title('Agent Login Page')
root8.geometry('1166x718-150-80')
root8.resizable(False, False)

bg_home = PhotoImage(file='8.png')
Label(root8, image=bg_home).place(x=0, y=0)

selectp= Entry(root8, width = 8, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
selectp.place(x = 550, y = 510)

buttonA = Button(root8, text='Submit', width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 15, 'bold'), border=0).place(x=770, y=510)
# buttonA = Button(root4, text='Buy', width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 28, 'bold'), border=0).place(x=755, y=475)


root8.mainloop()