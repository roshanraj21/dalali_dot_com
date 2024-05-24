from tkinter import *
from tkinter import ttk
import tkinter as tk
import mysql.connector as mysql
from tkinter import messagebox
from tkcalendar import *

global bg_home_agent_main, username

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
    
    global bg_home_agent_main

    bg_home_agent_main = PhotoImage(file='2.png')
    Label(root1, image=bg_home_agent_main).place(x=0, y=0)

    def signin():
        global username
        username = user.get()
        passw = password.get()

        if username == '' or password == '':
                messagebox.showerror('Error', 'All fields are required!')

        else:
            try:
                conn = mysql.connect(host = 'localhost', user = 'root', password = 'MySQL123')
                mycursor = conn.cursor()
            except:
                messagebox.showerror('Error', 'Connection is not established! Try Again')
                return

            query = 'use project'
            mycursor.execute(query)

            
            query = 'select a_id, Password from agent where a_id = %s and Password = %s'
            mycursor.execute(query, (username, passw))

            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Invalid username or password!')
            else:
                messagebox.showinfo('Success', 'Login is Successful')

                global bg_home_sold, bg_home_rent, bg_home_all

                root3 = Toplevel(root1)
                root3.title('Available/Sold/Rented')
                root3.geometry('1166x718-150-80')
                root3.resizable(False, False)

                bg_home = PhotoImage(file='3.png')
                Label(root3, image=bg_home).place(x=0, y=0)

                def Sold():
                    global root8, username

                    root8 = Toplevel(root3)
                    root8.title('Sold Properties')
                    root8.geometry('1166x718-150-80')
                    root8.resizable(False, False)

                    global bg_home_sold
                    bg_home_sold = PhotoImage(file='8.png')
                    Label(root8, image=bg_home_sold).place(x=0, y=0)

                   
                    try:
                        conn=mysql.connect(host='localhost',user='root',password='MySQL123',database='project')
                        mycursor=conn.cursor()
                    except:
                       messagebox.showerror('Error,Connection not established,Try Again!')

                    tree = ttk.Treeview(root8, columns = ("column1", "column2", "column3", "column4", "column5","column6", "column7", "column8", "column9", "column10", "column11"), show ="headings")
                    tree.column("column1", width = 70, anchor = "center")
                    tree.column("column2", width = 110, anchor = "center")
                    tree.column("column3", width = 110, anchor = "center")
                    tree.column("column4", width = 100, anchor = "center")
                    tree.column("column5", width = 70, anchor = "center")
                    tree.column("column6", width = 180, anchor = "center")
                    tree.column("column7", width = 90, anchor = "center")
                    tree.column("column8", width = 70, anchor = "center")
                    tree.column("column9", width = 70, anchor = "center")
                    tree.column("column10", width = 100, anchor = "center")
                    tree.column("column11", width = 70, anchor = "center")

                    tree.heading("column1", text = "P_id")
                    tree.heading("column2", text = "Property_Name")
                    tree.heading("column3", text = "Property_Type")
                    tree.heading("column4", text = "Street")
                    tree.heading("column5", text = "City")
                    tree.heading("column6", text = "Landmark")
                    tree.heading("column7", text = "Pincode")
                    tree.heading("column8", text = "Bedroom")
                    tree.heading("column9", text = "Bathroom")
                    tree.heading("column10", text = "Parking_Lot")
                    tree.heading("column11", text = "Year")

                    tree.place(x=60,y=124)

                    
                    query='select property.P_id,Property_Name,Property_Type,Street,City,Landmark,Pincode,Bedroom,Bathroom,Parking_Lot,Year from property,sale_details where property.P_id=Sale_Details.p_id and Available="No" and property.A_id=%s'
                    mycursor.execute(query,(username,))

                   
                    records=mycursor.fetchall()

                    
                    tree.pack(pady=100)
                    tree.tag_configure('evenrow',background='white')
                    tree.tag_configure('oddrow',background='#CFC5B3')

                    count=0
                    for i in records:
                       if count%2!=0:
                           tree.insert(parent='',index='end',text="",values=i,tags='evenrow')
                       else:
                           tree.insert(parent='',index='end',text="",values=i,tags='oddrow')
                       count+=1   

                    
                    def on_tree_select(event):
                       
                       selected_row = tree.focus()
                       
                       values = tree.item(selected_row, 'values')
                       
                       Pid.delete(0, END)
                       Pid.insert(0, values[0])

                       
                    tree.bind("<<TreeviewSelect>>", on_tree_select)


                    def buyer():
                    
                        
                        tree1 = ttk.Treeview(root8, columns = ("column1", "column2", "column3", "column4", "column5","column6"), show = "headings")
                        tree1.column("column1", width = 80, anchor = "center")
                        tree1.column("column2", width = 110, anchor = "center")
                        tree1.column("column3", width = 110, anchor = "center")
                        tree1.column("column4", width = 120, anchor = "center")
                        tree1.column("column5", width = 180, anchor = "center")
                        tree1.column("column6", width = 100, anchor = "center")

                        tree1.heading("column1", text = "B_id")
                        tree1.heading("column2", text = "FName")
                        tree1.heading("column3", text = "LName")
                        tree1.heading("column4", text = "Contact_Number")
                        tree1.heading("column5", text = "Email")
                        tree1.heading("column6", text = "Sex")

                        tree1.config(height=2)
                        tree1.place(x=150,y=590)

                        
                        value = (Pid.get(),)

                       
                        query='select B_id,Fname,Lname,Contact_Number,Email,Sex from Buyers where B_id in (select distinct B_id from property inner join sale_details on property.p_id=sale_details.p_id where Available="No" and property.p_id = %s)'
                        mycursor.execute(query, value)

                        
                        records=mycursor.fetchall()

                        
                        for row in records:
                            tree1.insert("","end",values=row)

                    Pid = Entry(root8, width=9,border=1 ,foreground='#735E59', font=('Arial', 20,))
                    Pid.place(x=550, y=510)

                    buttonA = Button(root8, text='Submit', command = buyer, width=9, background='#735E59', foreground='white',        activebackground='white', activeforeground='black', font=('Arial', 18, 'bold'), border=0).place(x=770, y=510)    

                    root8.mainloop()

                def Rent():
                    global root9

                    root9 = Toplevel(root3)
                    root9.title('Rented Properties')
                    root9.geometry('1166x718-150-80')
                    root9.resizable(False, False)

                    global bg_home_rent
                    bg_home_rent = PhotoImage(file='9.png')
                    Label(root9, image=bg_home_rent).place(x=0, y=0)

                  
                    try:
                        conn=mysql.connect(host='localhost',user='root',password='MySQL123',database='project')
                        mycursor=conn.cursor()
                    except:
                        messagebox.showerror('Error,Connection not established,Try Again!')

                
                    tree = ttk.Treeview(root9, columns = ("column1", "column2", "column3", "column4", "column5","column6", "column7", "column8", "column9", "column10", "column11"), show ="headings")
                    tree.column("column1", width = 70, anchor = "center")
                    tree.column("column2", width = 110, anchor = "center")
                    tree.column("column3", width = 110, anchor = "center")
                    tree.column("column4", width = 100, anchor = "center")
                    tree.column("column5", width = 70, anchor = "center")
                    tree.column("column6", width = 190, anchor = "center")
                    tree.column("column7", width = 90, anchor = "center")
                    tree.column("column8", width = 70, anchor = "center")
                    tree.column("column9", width = 70, anchor = "center")
                    tree.column("column10", width = 100, anchor = "center")
                    tree.column("column11", width = 70, anchor = "center")

                    tree.heading("column1", text = "P_id")
                    tree.heading("column2", text = "Property_Name")
                    tree.heading("column3", text = "Property_Type")
                    tree.heading("column4", text = "Street")
                    tree.heading("column5", text = "City")
                    tree.heading("column6", text = "Landmark")
                    tree.heading("column7", text = "Pincode")
                    tree.heading("column8", text = "Bedroom")
                    tree.heading("column9", text = "Bathroom")
                    tree.heading("column10", text = "Parking_Lot")
                    tree.heading("column11", text = "Year")

                    
                    tree.place(x=60,y=124)

                    
                    query='select property.P_id,Property_Name,Property_Type,Street,City,Landmark,Pincode,Bedroom,Bathroom,Parking_Lot,Year from property,Rent_Details where property.P_id=Rent_Details.p_id and Available="No" and property.A_id=%s'
                    mycursor.execute(query, (username,))

                    
                    records=mycursor.fetchall()

                    
                    tree.pack(pady=100)
                    tree.tag_configure('evenrow',background='white')
                    tree.tag_configure('oddrow',background='#CFC5B3')

                    count=0
                    for i in records:
                        if count%2!=0:
                            tree.insert(parent='',index='end',text="",values=i,tags='evenrow')
                        else:
                            tree.insert(parent='',index='end',text="",values=i,tags='oddrow')
                        count+=1 

                    
                    def on_tree_select(event):
                        
                        selected_row = tree.focus()
                        
                        values = tree.item(selected_row, 'values')
                        
                        Pid.delete(0, END)
                        Pid.insert(0, values[0])

                    
                    tree.bind("<<TreeviewSelect>>", on_tree_select)

                    def buyer():
                       
                        tree1 = ttk.Treeview(root9, columns = ("column1", "column2", "column3", "column4", "column5","column6"), show = "headings")
                        tree1.column("column1", width = 80, anchor = "center")
                        tree1.column("column2", width = 110, anchor = "center")
                        tree1.column("column3", width = 110, anchor = "center")
                        tree1.column("column4", width = 120, anchor = "center")
                        tree1.column("column5", width = 180, anchor = "center")
                        tree1.column("column6", width = 100, anchor = "center")

                        tree1.heading("column1", text = "B_id")
                        tree1.heading("column2", text = "FName")
                        tree1.heading("column3", text = "LName")
                        tree1.heading("column4", text = "Contact_Number")
                        tree1.heading("column5", text = "Email")
                        tree1.heading("column6", text = "Sex")

                        
                        tree1.config(height=2)
                        tree1.place(x=150,y=590)

                        
                        value = (Pid.get(),)

                        
                        query='select B_id,Fname,Lname,Contact_Number,Email,Sex from Buyers where B_id in (select distinct B_id from property inner join rent_details on property.p_id=rent_details.p_id where Available="No" and property.p_id = %s)'
                        mycursor.execute(query, value)

                        
                        records=mycursor.fetchall()

                        
                        for row in records:
                            tree1.insert("","end",values=row)

                   
                    Pid = Entry(root9, width=9,border=1 ,foreground='#735E59', font=('Arial', 20))
                    Pid.place(x=555, y=475)

                    
                    buttonA = Button(root9, text='Submit', command=buyer,width=9, background='#735E59', foreground='white', activebackground='white', activeforeground='black', font=   ('Arial', 18, 'bold'), border=0).place(x=730, y=475)

                    root9.mainloop()

                def All():
                    global root10

                    root10 = Toplevel(root3)
                    root10.title('All Properties')
                    root10.geometry('1166x718-150-80')
                    root10.resizable(False, False)

                    global bg_home_all
                    bg_home_all= PhotoImage(file='10.png')
                    Label(root10, image=bg_home_all).place(x=0, y=0)

                    
                    try:
                        conn=mysql.connect(host='localhost', user='root', password='MySQL123', database='project')
                        mycursor=conn.cursor()
                    except:
                        messagebox.showerror('Error, Connection not established,Try Again!')

                    
                    tree = ttk.Treeview(root10, columns = ("column1", "column2", "column3", "column4", "column5","column6", "column7", "column8", "column9", "column10", "column11"), show  = "headings")
                    tree.column("column1", width = 70, anchor = "center")
                    tree.column("column2", width = 150, anchor = "center")
                    tree.column("column3", width = 110, anchor = "center")
                    tree.column("column4", width = 100, anchor = "center")
                    tree.column("column5", width = 70, anchor = "center")
                    tree.column("column6", width = 190, anchor = "center")
                    tree.column("column7", width = 90, anchor = "center")
                    tree.column("column8", width = 60, anchor = "center")
                    tree.column("column9", width = 60, anchor = "center")
                    tree.column("column10", width = 100, anchor = "center")
                    tree.column("column11", width = 70, anchor = "center")

                    tree.heading("column1", text = "P_id")
                    tree.heading("column2", text = "Property_Name")
                    tree.heading("column3", text = "Property_Type")
                    tree.heading("column4", text = "Street")
                    tree.heading("column5", text = "City")
                    tree.heading("column6", text = "Landmark")
                    tree.heading("column7", text = "Pincode")
                    tree.heading("column8", text = "Bedroom")
                    tree.heading("column9", text = "Bathroom")
                    tree.heading("column10", text = "Parking_Lot")
                    tree.heading("column11", text = "Year")

                    
                    tree.config(height=24)
                    tree.place(x=60,y=270)

                    
                    query='select * from property where a_id = %s'
                    mycursor.execute(query, (username,))

                    
                    records=mycursor.fetchall()

                    tree.pack(pady=100)

                    
                    tree.tag_configure('evenrow',background='white')
                    tree.tag_configure('oddrow',background='#CFC5B3')

                    count=0
                    for i in records:
                        if count%2!=0:
                            tree.insert(parent='',index='end',text="",values=i,tags='evenrow')
                        else:
                            tree.insert(parent='',index='end',text="",values=i,tags='oddrow')
                        count+=1   

                    root10.mainloop()
                    
                 
                 
                def Available():   
                    root4 = Toplevel(root3)
                    root4.title('Available Properties')
                    root4.geometry('1166x718-150-80')
                    root4.resizable(False, False)


                    def sell():
                        global street,city
                        global bg_sell
                        root6 = Toplevel(root4)
                        root6.title('Sell to Buyers')
                        root6.geometry('1166x718-150-80')
                        root6.resizable(False, False)

                        bg_sell = PhotoImage(file='6.png')
                        Label(root6, image=bg_sell).place(x=0, y=0)


                        street = Entry(root6, width=15, fg='black', border=0,   bg='#ECEADA', font=('Microsoft YaHei UI Light', 15))
                        street.place(x=170, y=148)
                        city = Entry(root6, width=15, fg='black', border=0,bg='#ECEADA', font=('Microsoft YaHei UI Light', 15))
                        city.place(x=145, y=195)
                       

                        sellRent = ttk.Combobox(root6, state="readonly")
                        sellRent['values'] = ('--select--', 'Sell', 'Rent')
                        sellRent.current(0)
                        sellRent.bind("<<ComboboxSelected>>")
                        sellRent.place(x=230, y=298, width=120)
                        sellRent.config(font=("yu gothic ui", 11))

                        pType = ttk.Combobox(root6, state="readonly")
                        pType['values'] = ('--select--', 'Plot', 'House', 'Appartment')
                        pType.current(0)
                        pType.bind("<<ComboboxSelected>>")
                        pType.place(x=620, y=298, width=120)
                        pType.config(font=("yu gothic ui", 11))

                        bedroom = ttk.Combobox(root6, state="readonly")
                        bedroom['values'] = ('--select--', '1', '2', '3', '4', '5', '6', '7')
                        bedroom.current(0)
                        bedroom.bind("<<ComboboxSelected>>")
                        bedroom.place(x=210, y=247, width=120)
                        bedroom.config(font=("yu gothic ui", 11))

                        bathroom = ttk.Combobox(root6, state="readonly")
                        bathroom['values'] = ('--select--', '1', '2', '3','4','5')
                        bathroom.current(0)
                        bathroom.bind("<<ComboboxSelected>>")
                        bathroom.place(x=565, y=247, width=120)
                        bathroom.config(font=("yu gothic ui", 11))

                        parking = ttk.Combobox(root6, state="readonly")
                        parking['values'] = ('--select--', 'Yes', 'No')
                        parking.current(0)
                        parking.bind("<<ComboboxSelected>>")
                        parking.place(x=968, y=247, width=120)
                        parking.config(font=("yu gothic ui", 11))

                        def submit_buyreq():
                            global street, city
                            global bg_match
                        
                            if(street.get()!='' and city.get()!='' and bedroom.get()!='' and bathroom.get()!='' and parking.get()!='' and sellRent.get()!='' and pType.get()!=''):
                                
                                root7 = Toplevel(root6)
                                root7.title('Matched Results')
                                root7.geometry('1166x718-150-80')
                                root7.resizable(False, False)

                                bg_match = PhotoImage(file='7.png')
                                Label(root7, image=bg_match).place(x=0, y=0)



                                fName = Entry(root7, width=15, fg='black', border=0,  bg='#ECEADA', font=('Microsoft YaHei UI Light', 15))
                                fName.place(x=225, y=450)
                                lName = Entry(root7, width=15, fg='black', border=0, bg='#ECEADA', font=('Microsoft YaHei UI Light', 15))
                                lName.place(x=225, y=494)

                                cnum = Entry(root7, width=15, fg='black', border=0, bg='#ECEADA', font=('Microsoft YaHei UI Light', 15))
                                cnum.place(x=235, y=540)
                                email = Entry(root7, width=30, fg='black', border=0, bg='#ECEADA', font=('Microsoft YaHei UI Light', 15))
                                email.place(x=160, y=587)
                                pid = Entry(root7, width=15, fg='black', border=0, bg='#ECEADA', font=('Microsoft YaHei UI Light', 15))
                                pid.place(x=630, y=540)

                                def pick_date(e):
                                    global cal, date_window
                                    date_window = Toplevel()
                                    date_window.grab_set()
                                    date_window.title('Select date of buying: ')
                                    date_window.geometry('250x220+590+370')
                                    cal = Calendar(date_window, selectmode = "day", date_pattern = "y-mm-dd")
                                    cal.place(x = 0, y = 0)
                                    submit_btn = Button(date_window, text = "Submit", command = grab_date)
                                    submit_btn.place(x = 80, y = 190)

                                def grab_date():
                                    dob.delete(0, END)
                                    dob.insert(0, cal.get_date())
                                    date_window.destroy()





                                dob = Entry(root7, width = 13, fg = 'black', border = 1, highlightbackground = 'black', bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))  
                                dob.place(x=633, y=448)
                                dob.insert(0, "yyyy-mm-dd")
                                dob.bind("<1>", pick_date)
                                global doe
                                dos = Entry(root7, width = 13, fg = 'black', border = 1, highlightbackground = 'black', bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))  
                                dos.place(x=620, y=585)


                                doe = Entry(root7, width = 13, fg = 'black', border = 1, highlightbackground = 'black', bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))  
                                doe.place(x=680, y=630)


                                sex = ttk.Combobox(root7, state="readonly")
                                sex['values'] = ('--select--', 'Male', 'Female')
                                sex.current(0)
                                sex.bind("<<ComboboxSelected>>")
                                sex.place(x=620, y=496, width=120)
                                sex.config(font=("yu gothic ui", 11))


                                column1 = ('Property_id', 'Property_Name', 'Property_Type', 'Street', 'City', 'Landmark', 'Pincode', 'Bedrooms', 'Bathrooms', 'Price', 'Parking', 'YOC')
                                listbox = ttk.Treeview(root7, columns = column1, show = 'headings')
                                listbox.column("#1", anchor = CENTER, width = 80)
                                listbox.column("#2", anchor = CENTER, width = 140)
                                listbox.column("#3", anchor = CENTER, width = 100)
                                listbox.column("#4", anchor = CENTER, width = 120)
                                listbox.column("#5", anchor = CENTER, width = 120)
                                listbox.column("#6", anchor = CENTER, width = 120)
                                listbox.column("#7", anchor = CENTER, width = 80)  
                                listbox.column("#8", anchor = CENTER, width = 70) 
                                listbox.column("#9", anchor = CENTER, width = 70) 
                                listbox.column("#10", anchor = CENTER, width = 60) 
                                listbox.column("#11", anchor = CENTER, width = 60) 
                                listbox.column("#12", anchor = CENTER, width = 80) 

                                for col in column1:
                                    listbox.heading(col, text = col)
                                    listbox.grid(row = 1, column = 0, columnspan = 1)
                                    listbox.place(x = 33, y = 120)  


                                e1=street.get()
                                e2=city.get()
                                e3=bedroom.get()
                                e4=bathroom.get()
                                e5=parking.get()
                                e6=sellRent.get()
                                e7=pType.get()
                                print(e1,e2,e3,e4,e5,e6,e7)


                                try:
                                    conn = mysql.connect(host = 'localhost', user = 'root', password = 'MySQL123', database = "project")
                                    mycursor = conn.cursor()



                                except:
                                    messagebox.showerror('Error', 'Connection is not established! Try Again')

                                if(e6=='Sell'):
                                        query1 = "select property.p_id, Property_Name, Property_Type, Street, City, Landmark, Pincode, Bedroom, Bathroom, Selling_Price, Parking_Lot, Year  from property inner join sale_details on property.p_id=sale_details.p_id where Street = %s and City= %s and Bedroom = %s and  Bathroom = %s and  Parking_Lot = %s and Available ='Yes' and Property_Type=%s"
                                        value=(e1,e2,e3,e4,e5,e7)
                                        mycursor.execute(query1,value)
                                        records = mycursor.fetchall()
                                        print(records)

                                        for i, (p_id, Property_Name, Property_Type, Street, City, Landmark, Pincode, Bedroom, Bathroom, Price, Parking_Lot, Year) in enumerate(records, start = 1):
                                             listbox.insert("", "end", values = (p_id, Property_Name, Property_Type, Street, City, Landmark, Pincode, Bedroom, Bathroom, Price, Parking_Lot, Year))


                                        doe = Label(root7, text="Not required",width = 13, fg = 'black', border = 1, highlightbackground = 'black', bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 15))  
                                        doe.place(x=680, y=630)


                                elif (e6=='Rent'):
                                    query1 = "select  property.p_id, Property_Name, Property_Type, Street, City, Landmark, Pincode, Bedroom, Bathroom, Rent, Parking_Lot, Year from property inner join rent_details on property.p_id=rent_details.p_id where Street = %s and City= %s and Bedroom = %s and Bathroom = %s and Parking_Lot = %s and Available ='Yes'and Property_Type=%s"
                                    value=(e1,e2,e3,e4,e5,e7)
                                    mycursor.execute(query1,value)
                                    records = mycursor.fetchall()
                                    print(records)

                                    for i, (p_id, Property_Name, Property_Type, Street, City, Landmark, Pincode, Bedroom, Bathroom, Price, Parking_Lot, Year) in enumerate(records, start = 1):
                                         listbox.insert("", "end", values = (p_id, Property_Name, Property_Type, Street, City, Landmark, Pincode, Bedroom, Bathroom, Price, Parking_Lot, Year))




                                def on_tree_select(e):
                                        selected_row = listbox.focus()
                                        values = listbox.item(selected_row, 'values')

                                        pid.delete(0, END)
                                        pid.insert(0, values[0])

                                listbox.bind("<<TreeviewSelect>>", on_tree_select)

                                def msubmit():
                                    global doe
                                    if(  fName.get()!='' and lName.get()!='' and dob.get()!='' and cnum.get()!='' and email.get()!='' and pid.get()!='' and sex.get()!='' and dos.get()!=''):
                                    
                                    
                                        m1= fName.get()
                                        m2= lName.get()
                                        m3= dob.get()
                                        m4= cnum.get()
                                        m5= email.get()
                                        m6= pid.get()
                                        m7= sex.get()
                                        m9=dos.get()


                                        query1 = "INSERT INTO buyers (Fname, Lname, Contact_Number , Email, DOB, Sex) values (%s, %s, %s, %s, %s, %s)"
                                        value=(m1,m2,m4,m5,m3,m7)
                                        mycursor.execute(query1,value)
                                        conn.commit()

                                        query1 = "select b_id from buyers where Fname=%s"
                                        value=(m1,)
                                        mycursor.execute(query1,value)
                                        records1 = mycursor.fetchone()


                                        if(e6=="Sell"):
                                            query2 = "update sale_details set b_id=%s , Available='No', Selling_Date=%s where p_id=%s"
                                            value=(records1[0],m9,m6,)
                                            mycursor.execute(query2,value)
                                            conn.commit()



                                        elif (e6=="Rent"):
                                            m10=doe.get()
                                            query2 = "update rent_details set b_id=%s, Available='No', Start_Date=%s, End_Date=%s where p_id=%s"
                                            value=(records1[0],m9,m10,m6)
                                            mycursor.execute(query2,value)
                                            conn.commit()



                                        messagebox.showinfo('Success', 'Property is sold successfully')
                                    
                                    else:
                                        messagebox.showerror('error', " ALL Fields are Required ")




 
                                buttonA = Button(root7, text='Submit',command=msubmit, width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 15, 'bold'), border=0).place(x=1000, y=642)
                            
                            else:
                                messagebox.showerror('error','ALL Fields are required!')

                        buttonA = Button(root6, text='Submit', command= submit_buyreq, width=9, background='white', foreground='#735E59', activebackground='white',activeforeground='black', font=('Arial', 15, 'bold'), border=0).place(x=1000, y=642)



                    def buy():
                        
                        global bg_buy
                        root5 = Toplevel(root4)
                        root5.title('Buy from Owners')
                        root5.geometry('1166x718-150-80')
                        root5.resizable(False, False)


                        bg_buy = PhotoImage(file='5.png')
                        Label(root5, image=bg_buy).place(x=0, y=0)

                        

                        pname = Entry(root5, width = 30, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 20))
                        pname.place(x = 285, y = 146)

                        

                        pstreet = Entry(root5, width = 10, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                        pstreet.place(x = 155, y = 255)

                        pcity = Entry(root5, width = 10, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                        pcity.place(x = 400, y = 254)

                        ppin = Entry(root5, width = 8, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                        ppin.place(x = 184, y = 310)

                        pla = Entry(root5, width = 25, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 20))
                        pla.place(x = 735, y = 253)

                        

                        price = Entry(root5, width = 10, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                        price.place(x = 955, y = 202)

                        fname = Entry(root5, width = 15, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                        fname.place(x = 193, y = 444)

                        lname = Entry(root5, width = 15, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                        lname.place(x = 543, y = 444)

                       

                        email = Entry(root5, width = 15, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                        email.place(x = 170, y = 544)

                        num = Entry(root5, width = 15, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                        num.place(x = 590, y = 497)

                        vid = Entry(root5, width = 15, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                        vid.place(x = 280, y = 594)

                        


                        
                        plot = ttk.Combobox(root5, state = "readonly") 
                        plot['values'] = ('-select-','Yes', 'No')
                        plot.current(0)
                        plot.bind("<<ComboboxSelected>>")
                        plot.place(x = 1055, y = 316, width = 87)
                        plot.config(font = ("yu gothic ui", 11))

                        pbed = ttk.Combobox(root5, state = "readonly") 
                        pbed['values'] = ('--Select--', 1, 2, 3, 4, 5, 6, 7)
                        pbed.current(0)
                        pbed.bind("<<ComboboxSelected>>")
                        pbed.place(x = 475, y = 316, width = 87)
                        pbed.config(font = ("yu gothic ui", 11))

                        pbath = ttk.Combobox(root5, state = "readonly") 
                        pbath['values'] = ('--Select--', 1, 2, 3, 4, 5, 6, 7)
                        pbath.current(0)
                        pbath.bind("<<ComboboxSelected>>")
                        pbath.place(x = 770, y = 316, width = 87)
                        pbath.config(font = ("yu gothic ui", 11))

                        sex = ttk.Combobox(root5, state = "readonly") 
                        sex['values'] = ('--Select--','M', 'F')
                        sex.current(0)
                        sex.bind("<<ComboboxSelected>>")
                        sex.place(x = 132, y = 497, width = 87)
                        sex.config(font = ("yu gothic ui", 11))

                        ptype = ttk.Combobox(root5, state = "readonly") 
                        ptype['values'] = ('--Select--','Apartment', 'House','Plot')
                        ptype.current(0)
                        ptype.bind("<<ComboboxSelected>>")
                        ptype.place(x = 270, y = 208, width = 87)
                        ptype.config(font = ("yu gothic ui", 11))

                        year = ttk.Combobox(root5, state = "readonly") 
                        year['values'] = ('--Select--',1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959,1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969,1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979,1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,2020, 2021, 2022, 2023)
                        year.current(0)
                        year.bind("<<ComboboxSelected>>")
                        year.place(x = 715, y = 206, width = 90)
                        year.config(font = ("yu gothic ui", 11))

                        purpose = ttk.Combobox(root5, state = "readonly") 
                        purpose['values'] = ('--Select--','Sell','Rent')
                        purpose.current(0)
                        purpose.bind("<<ComboboxSelected>>")
                        purpose.place(x = 950, y = 152, width = 100)
                        purpose.config(font = ("yu gothic ui", 11))

                        def pick_date(e):
                            global cal, date_window
                            date_window = Toplevel()
                            date_window.grab_set()
                            date_window.title('Select date of buying: ')
                            date_window.geometry('250x220+590+370')
                            cal = Calendar(date_window, selectmode = "day", date_pattern = "y-mm-dd")
                            cal.place(x = 0, y = 0)
                            submit_btn = Button(date_window, text = "Submit", command = grab_date)
                            submit_btn.place(x = 80, y = 190)

                        def grab_date():
                            d.delete(0, END)
                            d.insert(0, cal.get_date())
                            date_window.destroy()

                        d = Entry(root5, width = 13, fg = 'black', border = 1, highlightbackground = 'black', bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))  
                        d.place(x=493, y=544)
                        d.insert(0, "yyyy-mm-dd")
                        d.bind("<1>", pick_date)

                        def submit_pdetails():
                            if(pname.get()!='' and pstreet.get()!='' and pcity.get()!='' and ppin.get()!='' and pla.get()!='' and fname.get()!='' and lname.get()!='' and email.get()!='' and num.get()!='' and vid.get()!='' and plot.get()!='' and pbed.get()!='' and pbath.get()!='' and sex.get()!='' and ptype.get()!='' and year.get()!='' and d.get()!='' and purpose.get()!='' and price.get()!=''): 
                        
                                try:
                                    conn = mysql.connect(host = 'localhost', user = 'root', password = 'MySQL123', database = "project")
                                    mycursor = conn.cursor()

                                except:
                                    messagebox.showerror('Error', 'Connection is not established! Try Again')

                                
                                b2=pname.get()
                                b3=pstreet.get()
                                b4=pcity.get()
                                b5=ppin.get()
                                b6=pla.get()
                                b7=fname.get()
                                b8=lname.get()
                                b9=email.get()
                                b10=num.get()
                                b11=vid.get()
                                b12=plot.get()
                                b13=pbed.get()
                                b14=pbath.get()
                                b15=sex.get()
                                b16=ptype.get()
                                b17=year.get()
                                b18=d.get()
                                b19=purpose.get()
                                b20=price.get()

                                query5="insert into owner(Fname,Lname,Email,Sex,Verification_id,Contact_Number) values (%s, %s, %s, %s, %s, %s)"
                                value =(b7,b8,b9,b15,b11,b10)
                                mycursor.execute(query5,value)
                                conn.commit()

                                query6="Select o_id from owner where Fname=%s"
                                value=(b7,)
                                mycursor.execute(query6,value)
                                records2 = mycursor.fetchone()

                                query7="insert into property(Property_Name,Property_Type,Street,City,Landmark,Pincode,Bedroom,Bathroom,Parking_Lot,Year,o_id,a_id) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                value =(b2,b16,b3,b4,b6,b5,b13,b14,b12,b17,records2[0],username, )
                                mycursor.execute(query7,value)
                                conn.commit

                                query10 = "select p_id from property where Property_Name=%s"
                                value=(b2, )
                                mycursor.execute(query10,value)
                                records3 = mycursor.fetchone()


                                if(b19 == 'Sell'):
                                    query8 = "insert into sale_details(Selling_Price,Registeration_Date,Selling_Date,Available,a_id,b_id,p_id) values (%s, %s, NULL, 'Yes', %s, NULL, %s)"
                                    value = (b20,b18,username,records3[0])
                                    mycursor.execute(query8,value)
                                    conn.commit()

                                elif(b19 == 'Rent'):
                                     query8 = "insert into rent_details(Rent,Start_Date,End_Date,Available,a_id,b_id,p_id) values (%s, NULL, NULL, 'Yes', %s, NULL, %s)"
                                     value = (b20,username,records3[0])
                                     mycursor.execute(query8,value)
                                     conn.commit()

                                messagebox.showinfo('Success','New Property Added')

                            else:
                                messagebox.showerror('error','All Fields are Required')

                        buttonA = Button(root5, text='Submit', command=submit_pdetails,width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 15, 'bold'), border=0).place(x=1000, y=642)


                    bg_home = PhotoImage(file='4.png')
                    Label(root4, image=bg_home).place(x=0, y=0)

                    buttonA = Button(root4, text='Sell', command = sell, width=9, background='white', foreground='#735E59', activebackground='white',activeforeground='black', font=('Arial', 28, 'bold'),     border=0).place(x=200, y=475)
                    buttonA = Button(root4, text='Buy', command = buy ,width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 28, 'bold'),  border=0).place(x=755, y=475)

                    root4.mainloop()

                buttonA = Button(root3, text='Available', command = Available, width=12, background='white', foreground='#735E59', activebackground='white',
                                 activeforeground='black', font=('yu gothic ui', 18, 'bold'), border=0).place(x=500, y=320)
                buttonA = Button(root3, text='Sold', width=12, background='white', foreground='#735E59', activebackground='white',
                                 activeforeground='black', font=('yu gothic ui', 18, 'bold'), command=Sold, border=0).place(x=190, y=575)
                buttonA = Button(root3, text='Rented', width=12, background='white', foreground='#735E59', activebackground='white',
                                 activeforeground='black', font=('yu gothic ui', 18, 'bold'), command=Rent, border=0).place(x=850, y=576)
                buttonA = Button(root3, text='Show All \n Properties', width=12, background='white', foreground='#735E59', activebackground='white',
                                 activeforeground='black', font=('yu gothic ui', 10, 'bold'),  command=All, border=0).place(x=1030, y=666)


                root3.mainloop()
        root1.mainloop()

    user = Entry(root1, width = 15, fg = 'black', border = 0, bg = '#E7E2D9', font = ('Microsoft YaHei UI Light', 15))
    user.place(x = 645, y = 273)

    password = Entry(root1, width = 15, fg = 'black', show = '*', border = 0, bg = '#E7E2D9', font = ('Microsoft YaHei UI Light', 15))
    password.place(x = 645, y = 380)

    def password_command():
        if password.cget('show') == '*':
            password.config(show='')
        else:
            password.config(show='*')

    checkButton=Checkbutton(root1, bg='white',command=password_command)
    checkButton.place(x=635, y=425) 

    buttonA = Button(root1, text='Sign In', command=signin, width=19, background='#735E59', foreground='white', activebackground='#735E59',activeforeground='black', font=('yu gothic ui', 15, 'bold'), border=0).place(x=642, y=512)

def office_signin():
    root2 = Toplevel(root)
    root2.title('Office Login Page')
    root2.geometry('1166x718-150-80')
    root2.resizable(False, False)

    global Aid
    bg_home = PhotoImage(file='2.png')
    Label(root2, image=bg_home).place(x=0, y=0)

    def signin():
        username = user.get()
        passw = password.get()
        global Aid

        if username == 'Shreya' and passw == '1234':
            root11 = Toplevel(root2)
            root11.title('Officer Details')
            root11.geometry('1166x718-150-80')
            root11.resizable(False, False)

            bg_home = PhotoImage(file='11.png')
            Label(root11, image=bg_home).place(x=0, y=0)

            db = mysql.connect(host='localhost', user='root',
                               password='MySQL123', database='project')
            mycursor = db.cursor()

            s = ttk.Style()

            tree = ttk.Treeview(root11, columns=(
                "column1", "column2"), show="headings")

            tree.column("column1", width=510, anchor="center")
            tree.column("column2", width=510, anchor="center")
            tree.heading("column1", text="Agent ID")
            tree.heading("column2", text="Commission Rate")

            mycursor.execute("SELECT a_id, c_rate FROM agent")

            result = mycursor.fetchall()

            tree.pack(pady=100)
            
            tree.tag_configure('evenrow', background='white')
            tree.tag_configure('oddrow', background='#CFC5B3')

            def on_tree_select(event):
                
                selected_row = tree.focus()

                values = tree.item(selected_row, 'values')


                Aid.delete(0, END)
                Aid.insert(0, values[0])

            tree.bind("<<TreeviewSelect>>", on_tree_select)

            tree.place(x=70, y=140)
            
            count = 0
            for i in result:
                if count % 2 != 0:
                    tree.insert(parent='', index='end', text="",
                                values=i, tags='evenrow')
                else:
                    tree.insert(parent='', index='end', text="",
                                values=i, tags='oddrow')
                count += 1

            Aid = Entry(root11, width=19, fg='black', border=1,
                        background='#ECEADA', font=('Microsoft YaHei UI Light', 15))
            Aid.place(x=443, y=610)

            def agent_det():
                root12 = Toplevel(root11)

                root12.title('Agent Details')
                root12.geometry('1166x718-150-80')
                root12.resizable(False, False)

                bg_home = PhotoImage(file='12.png')
                Label(root12, image=bg_home).place(x=0, y=0)

                db = mysql.connect(host='localhost', user='root',
                                   password='MySQL123', database='project')
                mycursor = db.cursor()

                global Aid

                value = (int(Aid.get()),)
                query = "SELECT a_id, Fname, Lname, Contact_Number, Email FROM agent where A_id = %s"
                mycursor.execute(query, value)

                result = mycursor.fetchone()

                aid = Label(root12, text=result[0], width=15, fg='black', border=0,
                            bg='#ECEADA', font=('Microsoft YaHei UI Light', 15)).place(x=150, y=178)
                fname = Label(root12, text=result[1], width=15, fg='black', border=0,
                              bg='#ECEADA', font=('Microsoft YaHei UI Light', 15,)).place(x=239, y=233)
                lname = Label(root12, text=result[2], width=15, fg='black', border=0,
                              bg='#ECEADA', font=('Microsoft YaHei UI Light', 15)).place(x=752, y=233)
                contact = Label(root12, text=result[3], width=15, fg='black', border=0,
                                bg='#ECEADA', font=('Microsoft YaHei UI Light', 15)).place(x=252, y=283)
                email = Label(root12, text=result[4], width=25, fg='black', border=0,
                              bg='#ECEADA', font=('Microsoft YaHei UI Light', 15)).place(x=682, y=283)

                def sold():
                    global Aid
                    value = (int(Aid.get()),)

                    root8 = Toplevel(root12)
                    root8.title('Sold Properties')
                    root8.geometry('1166x718-150-80')
                    root8.resizable(False, False)

                    bg_home = PhotoImage(file='8.png')
                    Label(root8, image=bg_home).place(x=0, y=0)

                    try:
                        conn = mysql.connect(host='localhost', user='root',
                                             password='MySQL123', database='project')
                        mycursor = conn.cursor()
                    except:
                        messagebox.showerror(
                            'Error,Connection not established,Try Again!')

                    tree = ttk.Treeview(root8, columns=("column1", "column2", "column3", "column4", "column5","column6", "column7", "column8", "column9", "column10", "column11"), show="headings")
                    tree.column("column1", width=70, anchor="center")
                    tree.column("column2", width=110, anchor="center")
                    tree.column("column3", width=110, anchor="center")
                    tree.column("column4", width=100, anchor="center")
                    tree.column("column5", width=70, anchor="center")
                    tree.column("column6", width=180, anchor="center")
                    tree.column("column7", width=90, anchor="center")
                    tree.column("column8", width=70, anchor="center")
                    tree.column("column9", width=70, anchor="center")
                    tree.column("column10", width=100, anchor="center")
                    tree.column("column11", width=70, anchor="center")

                    tree.heading("column1", text="P_id")
                    tree.heading("column2", text="Property_Name")
                    tree.heading("column3", text="Property_Type")
                    tree.heading("column4", text="Street")
                    tree.heading("column5", text="City")
                    tree.heading("column6", text="Landmark")
                    tree.heading("column7", text="Pincode")
                    tree.heading("column8", text="Bedroom")
                    tree.heading("column9", text="Bathroom")
                    tree.heading("column10", text="Parking_Lot")
                    tree.heading("column11", text="Year")

                    tree.place(x=60, y=124)

                    query = 'select property.P_id,Property_Name,Property_Type,Street,City,Landmark,Pincode,Bedroom,Bathroom,Parking_Lot,Year from property,sale_details where property.P_id=Sale_Details.p_id and Available="No" and property.A_id=%s'
                    mycursor.execute(query, value)

                    records = mycursor.fetchall()

                    tree.pack(pady=100)
                    tree.tag_configure('evenrow', background='white')
                    tree.tag_configure('oddrow', background='#CFC5B3')

                    count = 0
                    for i in records:
                        if count % 2 != 0:
                            tree.insert(parent='', index='end',
                                        text="", values=i, tags='evenrow')
                        else:
                            tree.insert(parent='', index='end',
                                        text="", values=i, tags='oddrow')
                        count += 1

                    
                    def on_tree_select(event):
                      
                        selected_row = tree.focus()
                        
                        values = tree.item(selected_row, 'values')
                        
                        Pid.delete(0, END)
                        Pid.insert(0, values[0])

                    tree.bind("<<TreeviewSelect>>", on_tree_select)
                    
                    def buyer():

                        tree1 = ttk.Treeview(root8, columns=("column1", "column2", "column3", "column4", "column5", "column6"), show="headings")
                        tree1.column("column1", width=100, anchor="center")
                        tree1.column("column2", width=110, anchor="center")
                        tree1.column("column3", width=110, anchor="center")
                        tree1.column("column4", width=100, anchor="center")
                        tree1.column("column5", width=180, anchor="center")
                        tree1.column("column6", width=100, anchor="center")

                        tree1.heading("column1", text="B_id")
                        tree1.heading("column2", text="FName")
                        tree1.heading("column3", text="LName")
                        tree1.heading("column4", text="Contact_Number")
                        tree1.heading("column5", text="Email")
                        tree1.heading("column6", text="Sex")

                        tree1.config(height=2)
                        tree1.place(x=150, y=590)

                        value = (Pid.get(),)

                        query = 'select B_id,Fname,Lname,Contact_Number,Email,Sex from Buyers where B_id in (select distinct B_id from property inner join sale_details on property.p_id=sale_details.p_id where Available="No" and property.p_id = %s)'
                        mycursor.execute(query, value)

                        records = mycursor.fetchall()

                        for row in records:
                            tree1.insert("", "end", values=row)

                    Pid = Entry(root8, width=9, border=1,
                                foreground='#735E59', font=('Arial', 20,))
                    Pid.place(x=550, y=510)

                    buttonA = Button(root8, text='Submit', command=buyer, width=9, background='#735E59', foreground='white',
                                     activebackground='white', activeforeground='black', font=('Arial', 18, 'bold'), border=0).place(x=770, y=510)
                    root8.mainloop()

                def rent():
                    global Aid

                    value = (int(Aid.get()),)

                    root9 = Toplevel(root12)
                    root9.title('Rented Properties')
                    root9.geometry('1166x718-150-80')
                    root9.resizable(False, False)

                    bg_home = PhotoImage(file='9.png')
                    Label(root9, image=bg_home).place(x=0, y=0)

                    try:
                        conn = mysql.connect(host='localhost', user='root',
                                             password='MySQL123', database='project')
                        mycursor = conn.cursor()
                    except:
                        messagebox.showerror(
                            'Error,Connection not established,Try Again!')
 
                    tree = ttk.Treeview(root9, columns=("column1", "column2", "column3", "column4", "column5", "column6", "column7", "column8", "column9", "column10", "column11"), show="headings")
                    tree.column("column1", width=70, anchor="center")
                    tree.column("column2", width=110, anchor="center")
                    tree.column("column3", width=110, anchor="center")
                    tree.column("column4", width=100, anchor="center")
                    tree.column("column5", width=70, anchor="center")
                    tree.column("column6", width=180, anchor="center")
                    tree.column("column7", width=90, anchor="center")
                    tree.column("column8", width=70, anchor="center")
                    tree.column("column9", width=70, anchor="center")
                    tree.column("column10", width=100, anchor="center")
                    tree.column("column11", width=70, anchor="center")

                    tree.heading("column1", text="P_id")
                    tree.heading("column2", text="Property_Name")
                    tree.heading("column3", text="Property_Type")
                    tree.heading("column4", text="Street")
                    tree.heading("column5", text="City")
                    tree.heading("column6", text="Landmark")
                    tree.heading("column7", text="Pincode")
                    tree.heading("column8", text="Bedroom")
                    tree.heading("column9", text="Bathroom")
                    tree.heading("column10", text="Parking_Lot")
                    tree.heading("column11", text="Year")

                    tree.place(x=60, y=124)

                    query = 'select property.P_id,Property_Name,Property_Type,Street,City,Landmark,Pincode,Bedroom,Bathroom,Parking_Lot,Year from property,Rent_Details where property.P_id=Rent_Details.p_id and Available="No" and property.A_id=%s'
                    mycursor.execute(query, value)

                    records = mycursor.fetchall()

                    tree.pack(pady=100)
                    tree.tag_configure('evenrow', background='white')
                    tree.tag_configure('oddrow', background='#CFC5B3')

                    count = 0
                    for i in records:
                        if count % 2 != 0:
                            tree.insert(parent='', index='end',
                                        text="", values=i, tags='evenrow')
                        else:
                            tree.insert(parent='', index='end',
                                        text="", values=i, tags='oddrow')
                        count += 1

                    def on_tree_select(event):
                        
                        selected_row = tree.focus()
                        
                        values = tree.item(selected_row, 'values')
                        
                        Pid.delete(0, END)
                        Pid.insert(0, values[0])

                    tree.bind("<<TreeviewSelect>>", on_tree_select)

                    def buyer():

                        tree1 = ttk.Treeview(root9, columns=("column1", "column2", "column3", "column4", "column5", "column6"), show="headings")
                        tree1.column("column1", width=100, anchor="center")
                        tree1.column("column2", width=110, anchor="center")
                        tree1.column("column3", width=110, anchor="center")
                        tree1.column("column4", width=100, anchor="center")
                        tree1.column("column5", width=180, anchor="center")
                        tree1.column("column6", width=100, anchor="center")

                        tree1.heading("column1", text="B_id")
                        tree1.heading("column2", text="FName")
                        tree1.heading("column3", text="LName")
                        tree1.heading("column4", text="Contact_Number")
                        tree1.heading("column5", text="Email")
                        tree1.heading("column6", text="Sex")

                        tree1.config(height=2)
                        tree1.place(x=150, y=590)

                        value = (Pid.get(),)

                        query = 'select B_id,Fname,Lname,Contact_Number,Email,Sex from Buyers where B_id in (select distinct B_id from property inner join rent_details on property.p_id=rent_details.p_id where Available="No" and property.p_id = %s)'
                        mycursor.execute(query, value)

                        records = mycursor.fetchall()

                        for row in records:
                            tree1.insert("", "end", values=row)

                    Pid = Entry(root9, width=9, border=1, foreground='#735E59',
                                font=('Arial', 20))
                    Pid.place(x=555, y=475)

                    buttonA = Button(root9, text='Submit', command=buyer, width=9, background='#735E59', foreground='white',
                                     activebackground='white', activeforeground='black', font=('Arial', 18,'bold'), border=0).place(x=730, y=475)
                   
                    root9.mainloop()

                def avai():
                    global Aid
                    value = (int(Aid.get()),)

                    global bg_home_avai
                    root15 = Toplevel(root12)

                    root15.title('Available Properties')
                    root15.geometry('1166x718-150-80')
                    root15.resizable(False, False)

                    bg_home_avai = PhotoImage(file='14.png')
                    Label(root15, image=bg_home_avai).place(x=0, y=0)

                    try:
                        conn = mysql.connect(host='localhost', user='root',password='MySQL123', database='project')
                        mycursor = conn.cursor()
                    except:
                        messagebox.showerror(
                            'Error,Connection not established,Try Again!')
                    tree = ttk.Treeview(root15, columns=("column1", "column2", "column3", "column4", "column5","column6", "column7", "column8", "column9", "column10", "column11"), show="headings")
                    tree.column("column1", width=70, anchor="center")
                    tree.column("column2", width=110, anchor="center")
                    tree.column("column3", width=110, anchor="center")
                    tree.column("column4", width=100, anchor="center")
                    tree.column("column5", width=70, anchor="center")
                    tree.column("column6", width=180, anchor="center")
                    tree.column("column7", width=90, anchor="center")
                    tree.column("column8", width=70, anchor="center")
                    tree.column("column9", width=70, anchor="center")
                    tree.column("column10", width=100, anchor="center")
                    tree.column("column11", width=70, anchor="center")

                    tree.heading("column1", text="P_id")
                    tree.heading("column2", text="Property_Name")
                    tree.heading("column3", text="Property_Type")
                    tree.heading("column4", text="Street")
                    tree.heading("column5", text="City")
                    tree.heading("column6", text="Landmark")
                    tree.heading("column7", text="Pincode")
                    tree.heading("column8", text="Bedroom")
                    tree.heading("column9", text="Bathroom")
                    tree.heading("column10", text="Parking_Lot")
                    tree.heading("column11", text="Year")

                    tree.config(height=10)
                    tree.place(x=60, y=124)

                    query = 'select property.P_id,Property_Name,Property_Type,Street,City,Landmark,Pincode,Bedroom,Bathroom,Parking_Lot,Year from property,Sale_Details where   property.P_id=Sale_Details.P_id and Available="Yes" and property.A_id=%s'
                    mycursor.execute(query, value)

                    records = mycursor.fetchall()

                    tree.pack(pady=110)
                    tree.tag_configure('evenrow', background='white')
                    tree.tag_configure('oddrow', background='#CFC5B3')

                    count = 0
                    for i in records:
                        if count % 2 != 0:
                            tree.insert(parent='', index='end',
                                        text="", values=i, tags='evenrow')
                        else:
                            tree.insert(parent='', index='end',
                                        text="", values=i, tags='oddrow')
                        count += 1

                    tree1 = ttk.Treeview(root15, columns=("column1", "column2", "column3", "column4", "column5", "column6", "column7", "column8", "column9", "column10", "column11"), show= "headings")
                    tree1.column("column1", width=70, anchor="center")
                    tree1.column("column2", width=110, anchor="center")
                    tree1.column("column3", width=110, anchor="center")
                    tree1.column("column4", width=100, anchor="center")
                    tree1.column("column5", width=70, anchor="center")
                    tree1.column("column6", width=180, anchor="center")
                    tree1.column("column7", width=90, anchor="center")
                    tree1.column("column8", width=70, anchor="center")
                    tree1.column("column9", width=70, anchor="center")
                    tree1.column("column10", width=100, anchor="center")
                    tree1.column("column11", width=70, anchor="center")

                    tree1.heading("column1", text="P_id")
                    tree1.heading("column2", text="Property_Name")
                    tree1.heading("column3", text="Property_Type")
                    tree1.heading("column4", text="Street")
                    tree1.heading("column5", text="City")
                    tree1.heading("column6", text="Landmark")
                    tree1.heading("column7", text="Pincode")
                    tree1.heading("column8", text="Bedroom")
                    tree1.heading("column9", text="Bathroom")
                    tree1.heading("column10", text="Parking_Lot")
                    tree1.heading("column11", text="Year")

                    tree1.config(height=10)
                    tree1.place(x=60, y=100)

                    query1 = 'select property.P_id,Property_Name,Property_Type,Street,City,Landmark,Pincode,Bedroom,Bathroom,Parking_Lot,Year from property,Rent_Details where  property.P_id=Rent_Details.p_id and Available="Yes" and property.A_id=%s'
                    mycursor.execute(query1, value)

                    records1 = mycursor.fetchall()

                    tree1.pack(pady=20)
                    tree1.tag_configure('evenrow', background='white')
                    tree1.tag_configure('oddrow', background='#CFC5B3')

                    count1 = 0
                    for i in records1:
                        if count1 % 2 != 0:
                            tree1.insert(parent='', index='end',
                                         text="", values=i, tags='evenrow')
                        else:
                            tree1.insert(parent='', index='end',
                                         text="", values=i, tags='oddrow')
                        count1 += 1

                    root15.mainloop()

                buttonA = Button(root12, text='Available', width=12, background='white', foreground='#735E59', activebackground='white',
                                 activeforeground='black', font=('yu gothic ui', 15, 'bold'), command=avai, border=0).place(x=510, y=570)

                buttonB = Button(root12, text='Sold', width=12, background='white', foreground='#735E59', activebackground='white',
                                 activeforeground='black', font=('yu gothic ui', 15, 'bold'), border=0, command=sold).place(x=140, y=570)

                buttonC = Button(root12, text='Rented', width=12, background='white', foreground='#735E59', activebackground='white',
                                 activeforeground='black', font=('yu gothic ui', 15, 'bold'), border=0, command=rent).place(x=910, y=565)

                root12.mainloop()

            buttonA = Button(root11, text='Submit', width=9, background='#735E59', foreground='white', activebackground='#735E59',
                             activeforeground='black', font=('Arial', 18, 'bold'), border=0, command=agent_det).place(x=765, y=605)

            root11.mainloop()

        elif username == '' or passw == '':
            messagebox.showerror('Error', 'Enter valid Id or Password!')
        elif username != 'Shreya':
            messagebox.showerror('Error', 'Enter valid Id or Password!')
        elif passw != '1234':
            messagebox.showerror('Error', 'Enter valid Id or Password!')

    user = Entry(root2, width=15, fg='black', border=0,
                 bg='#E7E2D9', font=('Microsoft YaHei UI Light', 15))
    user.place(x=645, y=273)

    password = Entry(root2, width=15, fg='black', border=0,
                     bg='#E7E2D9', show='*', font=('Microsoft YaHei UI Light', 15))
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

buttonA = Button(root, text='Agent', width=9, background='white', foreground='black', activebackground='white',activeforeground='#735E59', font=('yu gothic ui', 28, 'bold'), border=0,command =agent_signin).place(x=200, y=539)
buttonO = Button(root, text='Office', command = office_signin, width=9, background='white', foreground='black', activebackground='white',activeforeground='#735E59', font=('yu gothic ui', 30, 'bold'), border=0).place(x=770, y=540)

root.mainloop()