from tkinter import *
import tkinter

root9 = Tk()
root9.title('Agent Login Page')
root9.geometry('1166x718-150-80')
root9.resizable(False, False)

bg_home = PhotoImage(file='9.png')
Label(root9, image=bg_home).place(x=0, y=0)

selectp= Entry(root9, width = 8, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
selectp.place(x = 547, y = 480)

buttonA = Button(root9, text='Submit', width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 15, 'bold'), border=0).place(x=710, y=477)
# buttonA = Button(root4, text='Buy', width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 28, 'bold'), border=0).place(x=755, y=475)


root9.mainloop()