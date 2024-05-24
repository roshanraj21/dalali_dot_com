from tkinter import *
from tkinter import ttk
import tkinter as tk
import mysql.connector as mysql
from tkinter import messagebox

global bg_home_sold, bg_home_rent, bg_home_all

root3 = Tk()
root3.title('Available/Sold/Rented')
root3.geometry('1166x718-150-80')
root3.resizable(False, False)

bg_home = PhotoImage(file='3.png')
Label(root3, image=bg_home).place(x=0, y=0)

def Sold():
    global root8

    root8 = Toplevel(root3)
    root8.title('Sold Properties')
    root8.geometry('1166x718-150-80')
    root8.resizable(False, False)
    
    global bg_home_sold
    bg_home_sold = PhotoImage(file='8.png')
    Label(root8, image=bg_home_sold).place(x=0, y=0)

    #connection to database
    try:
        conn=mysql.connect(host='localhost',user='root',password='MySQL123',database='project')
        mycursor=conn.cursor()
    except:
       messagebox.showerror('Error,Connection not established,Try Again!')
    
    #creating property table
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

    #placing the table
    tree.place(x=60,y=124)
    
    #query
    query='select property.P_id,Property_Name,Property_Type,Street,City,Landmark,Pincode,Bedroom,Bathroom,Parking_Lot,Year from property,sale_details where property.  P_id=Sale_Details.p_id and Available="No" and property.A_id="103"'
    mycursor.execute(query)

    # query='select property.P_id,Property_Name,Property_Type,Street,City,Landmark,Pincode,Bedroom,Bathroom,Parking_Lot,Year from property,sale_details where property.  P_id=Sale_Details.p_id and Available="No" and property.A_id=%s'
    # mycursor.execute(query,(user.get(),))
    
    #fetch all data
    records=mycursor.fetchall()
    
    #colouring alternate rows
    tree.pack(pady=100)
    tree.tag_configure('evenrow',background='white')
    tree.tag_configure('oddrow',background='#735E59')

    count=0
    for i in records:
       if count%2!=0:
           tree.insert(parent='',index='end',text="",values=i,tags='evenrow')
       else:
           tree.insert(parent='',index='end',text="",values=i,tags='oddrow')
       count+=1   
    
    #selecting pid on clicking
    def on_tree_select(event):
       # Get the selected row
       selected_row = tree.focus()
       # Get the values from the selected row
       values = tree.item(selected_row, 'values')
       # Update the input field
       Pid.delete(0, END)
       Pid.insert(0, values[0])

       # Bind the <<TreeviewSelect>> event to the on_tree_selectfunction
    tree.bind("<<TreeviewSelect>>", on_tree_select)


    def buyer():

        #creating table for buyer details
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
        
        #placing table of buyer details of height 2
        tree1.config(height=2)
        tree1.place(x=150,y=590)

        #taking p_id input from user
        value = (Pid.get(),)

        #query for sold properties
        query='select B_id,Fname,Lname,Contact_Number,Email,Sex from Buyers where B_id in (select distinct B_id from property inner join sale_details on property.  p_id=sale_details.p_id where Available="No" and property.p_id = %s)'
        mycursor.execute(query, value)

        #fetch all data
        records=mycursor.fetchall()

        #insert into tree
        for row in records:
            tree1.insert("","end",values=row)

    #creating entry for pid
    Pid = Entry(root8, width=9,border=1 ,foreground='#735E59', font=('Arial', 20,))
    Pid.place(x=550, y=510)

    #creating buttons
    buttonA = Button(root8, text='Submit', command = buyer, width=9, background='#735E59', foreground='white', activebackground='white', activeforeground='black', font=    ('Arial', 15, 'bold'), border=0).place(x=770, y=510)    

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

    #connection to database
    try:
        conn=mysql.connect(host='localhost',user='root',password='MySQL123',database='project')
        mycursor=conn.cursor()
    except:
        messagebox.showerror('Error,Connection not established,Try Again!')

    #creating property table
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
    
    #placing the property table
    tree.place(x=60,y=124)

    #query
    query='select property.P_id,Property_Name,Property_Type,Street,City,Landmark,Pincode,Bedroom,Bathroom,Parking_Lot,Year from property,Rent_Details where property.   P_id=Rent_Details.p_id and Available="No" and property.A_id="108"'
    mycursor.execute(query)

    #fetch all data
    records=mycursor.fetchall()

    #colouring alternate rows
    tree.pack(pady=100)
    tree.tag_configure('evenrow',background='white')
    tree.tag_configure('oddrow',background='#735E59')

    count=0
    for i in records:
        if count%2!=0:
            tree.insert(parent='',index='end',text="",values=i,tags='evenrow')
        else:
            tree.insert(parent='',index='end',text="",values=i,tags='oddrow')
        count+=1 

    #selecting pid on clicking
    def on_tree_select(event):
        # Get the selected row
        selected_row = tree.focus()
        # Get the values from the selected row
        values = tree.item(selected_row, 'values')
        # Update the input field
        Pid.delete(0, END)
        Pid.insert(0, values[0])

    # Bind the <<TreeviewSelect>> event to the on_tree_selectfunction
    tree.bind("<<TreeviewSelect>>", on_tree_select)

    def buyer():
        #creating table for buyer details
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
        
        #placing table of buyer details of height 2
        tree1.config(height=2)
        tree1.place(x=150,y=590)

        #taking p_id input from user
        value = (Pid.get(),)
        
        #query
        query='select B_id,Fname,Lname,Contact_Number,Email,Sex from Buyers where B_id in (select distinct B_id from property inner join rent_details on property.  p_id=rent_details.p_id where Available="No" and property.p_id = %s)'
        mycursor.execute(query, value)

        #fetch all data
        records=mycursor.fetchall()

        #insert into tree
        for row in records:
            tree1.insert("","end",values=row)
    
    #creating entry for pid
    Pid = Entry(root9, width=9,border=1 ,foreground='#735E59', font=('Arial', 20))
    Pid.place(x=555, y=475)

    #creating buttons
    buttonA = Button(root9, text='Submit', command=buyer,width=9, background='#735E59', foreground='white', activebackground='white', activeforeground='black', font=   ('Arial', 15, 'bold'), border=0).place(x=730, y=475)

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
    
    #connection to database
    try:
        conn=mysql.connect(host='localhost',user='root',password='MySQL123',database='project')
        mycursor=conn.cursor()
    except:
        messagebox.showerror('Error,Connection not established,Try Again!')

    #creating property table
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

    #placing the property table
    tree.config(height=24)
    tree.place(x=60,y=270)

    #query
    query='select * from property'
    mycursor.execute(query)

    #fetch all data
    records=mycursor.fetchall()

    tree.pack(pady=100)

    #colouring alternate rows
    tree.tag_configure('evenrow',background='white')
    tree.tag_configure('oddrow',background='#ECEADA')

    count=0
    for i in records:
        if count%2!=0:
            tree.insert(parent='',index='end',text="",values=i,tags='evenrow')
        else:
            tree.insert(parent='',index='end',text="",values=i,tags='oddrow')
        count+=1   

    root10.mainloop()

#creating buttons
buttonA = Button(root3, text='Available', width=12, background='white', foreground='#735E59', activebackground='white',
                 activeforeground='black', font=('yu gothic ui', 18, 'bold'), border=0).place(x=500, y=320)
buttonA = Button(root3, text='Sold', width=12, background='white', foreground='#735E59', activebackground='white',
                 activeforeground='black', font=('yu gothic ui', 18, 'bold'), command=Sold, border=0).place(x=190, y=575)
buttonA = Button(root3, text='Rented', width=12, background='white', foreground='#735E59', activebackground='white',
                 activeforeground='black', font=('yu gothic ui', 18, 'bold'), command=Rent, border=0).place(x=850, y=576)
buttonA = Button(root3, text='Show All \n Properties', width=12, background='white', foreground='#735E59', activebackground='white',
                 activeforeground='black', font=('yu gothic ui', 10, 'bold'),  command=All, border=0).place(x=1030, y=666)


root3.mainloop()