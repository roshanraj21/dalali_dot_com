from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as mysql

root2 = Tk()
root2.title('Office Login Page')
root2.geometry('1166x718-150-80')
root2.resizable(False, False)


bg_home = PhotoImage(file='2.png')
Label(root2, image=bg_home).place(x=0, y=0)


def signin():
    username = user.get()
    passw = password.get()

    if username == 'Shreya' and passw == '1234':
        root11 = Toplevel(root2)
        root11.title('Office Login Page')
        root11.geometry('1166x718-150-80')
        root11.resizable(False, False)

        bg_home = PhotoImage(file='11.png')
        Label(root11, image=bg_home).place(x=0, y=0)
        
        try:
            conn = mysql.connect(host= 'localhost', password='MySQL123',user ='root', database='project')
            mycursor=conn.cursor()
            
            tree = ttk.Treeview(root11, columns = ("column1", "column2"), show = "headings")
            tree.column("column1", width = 400, anchor = "center")
            tree.column("column2", width = 400, anchor = "center")
            tree.heading("column1", text = "Agent ID")
            tree.heading("column2", text = "Commission Rate")
            tree.pack(padx = 10, pady = 10)
            tree.place(x = 250, y = 200)
                        
            mycursor.execute("SELECT a_id, c_rate FROM agent")
            result = mycursor.fetchall()

            for row in result:
                tree.insert("", "end", values = row)
    
            tree.tag_configure('evenrow',background='white')
            tree.tag_configure('oddrow',background='#ECEADA')
                
            aid = Entry(root11, width = 20, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 15))
            aid.place(x = 450, y = 610)

            buttonA = Button(root11, text='Submit', width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 18, 'bold'),      border=0).place(x=765, y=605)

        except:
            messagebox.showerror('error','connection is not established! Try Again')

            
        root11.mainloop()

    elif username == '' or passw == '':
        messagebox.showerror('Error', 'Enter valid Id or Password!')
    elif username != 'Shreya':
        messagebox.showerror('Error', 'Enter valid Id or Password!')
    elif passw != '1234':
        messagebox.showerror('Error', 'Enter valid Id or Password!')


user = Entry(root2, width=15, fg='black', border=0, bg='#E7E2D9', font=('Microsoft YaHei UI Light', 15))
user.place(x=645, y=273)

password = Entry(root2, width=15, fg='black', border=0, bg='#E7E2D9', show='*', font=('Microsoft YaHei UI Light', 15))
password.place(x=645, y=380)


def password_command():
    if password.cget('show') == '*':
        password.config(show='')
    else:
        password.config(show='*')


checkButton = Checkbutton(root2, bg='white', command=password_command)
checkButton.place(x=635, y=425)


buttonA = Button(root2, text='Sign In', width=19, background='#735E59', foreground='white', activebackground='#735E59',
                 activeforeground='black', font=('yu gothic ui', 15, 'bold'), border=0, command=signin).place(x=642, y=512)


root2.mainloop()
