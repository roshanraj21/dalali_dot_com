from tkinter import *
import tkinter
from tkinter import messagebox
import mysql.connector as mysql 
from tkinter import ttk 
from tkcalendar import *

#------------------main root page ---------------------------------
root4 = Tk()
root4.title('Agent Login Page')
root4.geometry('1166x718-150-80')
root4.resizable(False, False)


#-------------------------------------------------on clicking sell button---------------------------------------
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
    # bedroom = Entry(root6, width=15, fg='black', border=0,   bg='#ECEADA', font=('Microsoft YaHei UI Light', 15)).place(x=210, y=245)
    # bathroom = Entry(root6, width=15, fg='black', border=0,  bg='#ECEADA', font=('Microsoft YaHei UI Light', 15)).place(x=564, y=245)
    # parking = Entry(root6, width=15, fg='black', border=0, bg='#ECEADA', font=('Microsoft YaHei UI Light', 15)).place(x=965, y=245)
    # sellRent = Entry(root6, width=15, fg='black', border=0, bg='#ECEADA', font=('Microsoft YaHei UI Light', 15)).place(x=225, y=295)
    # pType = Entry(root6, width=15, fg='black', border=0, bg='#ECEADA', font=('Microsoft YaHei UI Light', 15)).place(x=618, y=295)

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
    bathroom['values'] = ('--select--', '1', '2', '3')
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

    #--------------------------------for navigating from sell page to match result page-------------------------------------
    def submit_buyreq():
        
        global street, city
        global bg_match
        root7 = Toplevel(root6)
        root7.title('Matched Results')
        root7.geometry('1166x718-150-80')
        root7.resizable(False, False)
        
        bg_match = PhotoImage(file='7.png')
        Label(root7, image=bg_match).place(x=0, y=0)
        
        
        
        fName = Entry(root7, width=15, fg='black', border=0,  bg='#ECEADA', font=('Microsoft YaHei UI Light', 15))
        fName.place(x=225, y=450)
        # dob = Entry(root7, width=15, fg='black', border=0,  bg='#ECEADA', font=('Microsoft YaHei UI Light', 15))
        # dob.place(x=633, y=448)
        lName = Entry(root7, width=15, fg='black', border=0, bg='#ECEADA', font=('Microsoft YaHei UI Light', 15))
        lName.place(x=225, y=494)

        cnum = Entry(root7, width=15, fg='black', border=0, bg='#ECEADA', font=('Microsoft YaHei UI Light', 15))
        cnum.place(x=235, y=540)
        email = Entry(root7, width=30, fg='black', border=0, bg='#ECEADA', font=('Microsoft YaHei UI Light', 15))
        email.place(x=160, y=587)
        pid = Entry(root7, width=15, fg='black', border=0, bg='#ECEADA', font=('Microsoft YaHei UI Light', 15))
        pid.place(x=630, y=540)
        
        # DATE CALENDER
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
        
        dos = Entry(root7, width = 13, fg = 'black', border = 1, highlightbackground = 'black', bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))  
        dos.place(x=620, y=585)
        dos.insert(0, "yyyy-mm-dd")
        dos.bind("<1>", pick_date)
        
        doe = Entry(root7, width = 13, fg = 'black', border = 1, highlightbackground = 'black', bg = '#E5E5E5', font = ('Microsoft YaHei UI Light', 15))  
        doe.place(x=680, y=630)
        doe.insert(0, "yyyy-mm-dd")
        doe.bind("<1>", pick_date)


        sex = ttk.Combobox(root7, state="readonly")
        sex['values'] = ('--select--', 'M', 'F')
        sex.current(0)
        sex.bind("<<ComboboxSelected>>")
        sex.place(x=620, y=496, width=120)
        sex.config(font=("yu gothic ui", 11))
        
        #---------------------table of match--------------------------------
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
        
        
        #----------------------------mysql connection and query------------------------------------------
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
            

                
                
                
        else:
            query1 = "select *  from property inner join rent_details on property.p_id=sale_details.p_id where Street = %s, City= %s, Bedroom = %s, Bathroom = %s, Parking_Lot = %s, Available ='Yes', Property_Type=%s"
            value=(e1,e2,e3,e4,e5,e6,e7)
            mycursor.execute(query1,value)
            
        
        
        #------------------------tree select--------------------------------------------
        def on_tree_select(e):
                selected_row = listbox.focus()
                values = listbox.item(selected_row, 'values')

                pid.delete(0, END)
                pid.insert(0, values[0])

        listbox.bind("<<TreeviewSelect>>", on_tree_select)
           
        def msubmit():
            m1= fName.get()
            m2= lName.get()
            m3= dob.get()
            m4= cnum.get()
            m5= email.get()
            m6= pid.get()
            m7= sex.get()
            
            query1 = "INSERT INTO buyers (Fname, Lname, Contact_Number , Email, DOB, Sex, a_id) values (%s, %s, %s, %s, %s, %s, %s)"
            value=(m1,m2,m4,m5,m3,m7,)
            mycursor.execute(query1,value)
            
            
            
           
        # button for the matched page 
        buttonA = Button(root7, text='Submit', width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 15, 'bold'), border=0).place(x=1000, y=642)
 
            
    buttonA = Button(root6, text='Submit', command= submit_buyreq, width=9, background='white', foreground='#735E59', activebackground='white',activeforeground='black', font=('Arial', 15, 'bold'), border=0).place(x=1000, y=642)
    
        
        
#------------------------------------------------on clicking buy button-----------------------------------
def buy():
    global bg_buy
    root5 = Toplevel(root4)
    root5.title('Buy from Owners')
    root5.geometry('1166x718-150-80')
    root5.resizable(False, False)
    
    bg_buy = PhotoImage(file='5.png')
    Label(root5, image=bg_buy).place(x=0, y=0)
    
    pid = Entry(root5, width = 50, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
    pid.place(x = 142, y = 131)

    pname = Entry(root5, width = 20, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
    pname.place(x = 275, y = 183)

    pstreet = Entry(root5, width = 10, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
    pstreet.place(x = 152, y = 234)

    pcity = Entry(root5, width = 10, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
    pcity.place(x = 400, y = 231)

    ppin = Entry(root5, width = 8, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
    ppin.place(x = 695, y = 235)

    pla = Entry(root5, width = 10, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
    pla.place(x = 985, y = 233)

    #-----------------owner details---------------------
    fname = Entry(root5, width = 15, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
    fname.place(x = 193, y = 435)

    lname = Entry(root5, width = 15, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
    lname.place(x = 543, y = 435)

    email = Entry(root5, width = 25, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
    email.place(x = 170, y = 535)

    num = Entry(root5, width = 15, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
    num.place(x = 590, y = 488)

    vid = Entry(root5, width = 15, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
    vid.place(x = 280, y = 585)

    # buttonA = Button(root4, text='Buy', width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 28, 'bold'), border=0).place(x=755, y=475)
    
    


    #----------------------------dropdown----------------------
    plot = ttk.Combobox(root5, state = "readonly") 
    plot['values'] = ('-select-','Yes', 'No')
    plot.current(0)
    plot.bind("<<ComboboxSelected>>")
    plot.place(x = 743, y = 292, width = 75)
    plot.config(font = ("yu gothic ui", 11))

    pbed = ttk.Combobox(root5, state = "readonly") 
    pbed['values'] = ('--Select--', 1, 2, 3, 4, 5, 6, 7)
    pbed.current(0)
    pbed.bind("<<ComboboxSelected>>")
    pbed.place(x = 195, y = 292, width = 75)
    pbed.config(font = ("yu gothic ui", 11))

    pbath = ttk.Combobox(root5, state = "readonly") 
    pbath['values'] = ('--Select--', 1, 2, 3, 4, 5, 6, 7)
    pbath.current(0)
    pbath.bind("<<ComboboxSelected>>")
    pbath.place(x = 475, y = 292, width = 75)
    pbath.config(font = ("yu gothic ui", 11))

    sex = ttk.Combobox(root5, state = "readonly") 
    sex['values'] = ('--Select--','Male', 'Female')
    sex.current(0)
    sex.bind("<<ComboboxSelected>>")
    sex.place(x = 132, y = 488, width = 75)
    sex.config(font = ("yu gothic ui", 11))

    ptype = ttk.Combobox(root5, state = "readonly") 
    ptype['values'] = ('--Select--','Apartment', 'House','Plot')
    ptype.current(0)
    ptype.bind("<<ComboboxSelected>>")
    ptype.place(x = 775, y = 183, width = 77)
    ptype.config(font = ("yu gothic ui", 11))
    
    def submit_pdetails():
        try:
            conn = mysql.connect(host = 'localhost', user = 'root', password = 'MySQL123', database = "project")
            mycursor = conn.cursor()
            
            b1=pid.get()
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
            
            
        
                
        except:
            messagebox.showerror('Error', 'Connection is not established! Try Again')
            
        
    
    
    buttonA = Button(root5, text='Submit', command=submit_pdetails,width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 15, 'bold'), border=0).place(x=1000, y=642)
    
    
bg_home = PhotoImage(file='4.png')
Label(root4, image=bg_home).place(x=0, y=0)

        

buttonA = Button(root4, text='Sell', command = sell, width=9, background='white', foreground='#735E59', activebackground='white',activeforeground='black', font=('Arial', 28, 'bold'),     border=0).place(x=200, y=475)
buttonA = Button(root4, text='Buy', command = buy ,width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 28, 'bold'),  border=0).place(x=755, y=475)

root4.mainloop()
