from tkinter import *
import tkinter
from tkinter import messagebox
import mysql.connector as mysql
from tkinter import ttk 
from tkcalendar import *

root1 = Tk()
root1.title('Agent Login')
root1.geometry('1166x718-150-80')
root1.resizable(False, False)

bg_home = PhotoImage(file='2.png')
Label(root1, image=bg_home).place(x=0, y=0)

def signin():
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
        
        # DATABASE selected
        query = 'use project'
        mycursor.execute(query)
        
        # QUERY for agent validation
        query = 'select a_id, Password from agent where a_id = %s and Password = %s'
        mycursor.execute(query, (username, passw))
    
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid username or password!')
        else:
            messagebox.showinfo('Success', 'Login is Successful')
                
            root4 = Toplevel(root1)
            root4.title('Agent Login Page')
            root4.geometry('1166x718-150-80')
            root4.resizable(False, False)


            # ----------------------Toplevel---------------------------
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


                            doe = Label(root7, text="Not required",width = 13, fg = 'black', border = 1, highlightbackground = 'black', bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 15))  
                            doe.place(x=680, y=630)


                    elif (e6=='Rent'):
                        query1 = "select  property.p_id, Property_Name, Property_Type, Street, City, Landmark, Pincode, Bedroom, Bathroom, Rent, Parking_Lot, Year from property inner join rent_details on property.p_id=rent_details.p_id where Street = %s, City= %s, Bedroom = %s, Bathroom = %s, Parking_Lot = %s, Available ='Yes', Property_Type=%s"
                        value=(e1,e2,e3,e4,e5,e6,e7)
                        mycursor.execute(query1,value)
                        records = mycursor.fetchall()
                        print(records)

                        for i, (p_id, Property_Name, Property_Type, Street, City, Landmark, Pincode, Bedroom, Bathroom, Price, Parking_Lot, Year) in enumerate(records, start = 1):
                             listbox.insert("", "end", values = (p_id, Property_Name, Property_Type, Street, City, Landmark, Pincode, Bedroom, Bathroom, Price, Parking_Lot, Year))




                    #------------------------tree select--------------------------------------------
                    def on_tree_select(e):
                            selected_row = listbox.focus()
                            values = listbox.item(selected_row, 'values')

                            pid.delete(0, END)
                            pid.insert(0, values[0])

                    listbox.bind("<<TreeviewSelect>>", on_tree_select)

                    def msubmit():
                        global doe
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
                            
                        

                        


                    # button for the matched page 
                    buttonA = Button(root7, text='Submit',command=msubmit, width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 15, 'bold'), border=0).place(x=1000, y=642)


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

                # pid = Entry(root5, width = 10, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                # pid.place(x = 145, y = 146)

                # pid = Entry(root5, width = 10, fg = 'black', border = 0, bg = 'white', font = ('Microsoft YaHei UI Light', 18))
                # pid.place(x = 142, y = 136)

                pname = Entry(root5, width = 30, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 20))
                pname.place(x = 285, y = 146)

                # ptype = Entry(root5, width = 18, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                # ptype.place(x = 775, y = 180)

                pstreet = Entry(root5, width = 10, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                pstreet.place(x = 155, y = 255)

                pcity = Entry(root5, width = 10, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                pcity.place(x = 400, y = 254)

                ppin = Entry(root5, width = 8, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                ppin.place(x = 184, y = 310)

                pla = Entry(root5, width = 25, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 20))
                pla.place(x = 735, y = 253)

                # pbed = Entry(root5, width = 5, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                # pbed.place(x = 195, y = 288)

                # pbath = Entry(root5, width = 5, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                # pbath.place(x = 475, y = 288)

                price = Entry(root5, width = 10, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                price.place(x = 955, y = 202)

                #-----------------owner details---------------------
                fname = Entry(root5, width = 15, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                fname.place(x = 193, y = 444)

                lname = Entry(root5, width = 15, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                lname.place(x = 543, y = 444)

                # sex = Entry(root5, width = 15, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                # sex.place(x = 132, y = 484)

                email = Entry(root5, width = 15, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                email.place(x = 170, y = 544)

                num = Entry(root5, width = 15, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                num.place(x = 590, y = 497)

                vid = Entry(root5, width = 15, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
                vid.place(x = 280, y = 594)

                # buttonA = Button(root4, text='Buy', width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 28, 'bold'), border=0).place(x=755, y=475)



                #----------------------------dropdown----------------------
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
                    try:
                        conn = mysql.connect(host = 'localhost', user = 'root', password = 'MySQL123', database = "project")
                        mycursor = conn.cursor()
                        
                    except:
                        messagebox.showerror('Error', 'Connection is not established! Try Again')

                    # b1=pid.get()
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
                
                    
                        
                buttonA = Button(root5, text='Submit', command=submit_pdetails,width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 15, 'bold'), border=0).place(x=1000, y=642)
    
                
            bg_home = PhotoImage(file='4.png')
            Label(root4, image=bg_home).place(x=0, y=0)
            
            buttonA = Button(root4, text='Sell', command = sell, width=9, background='white', foreground='#735E59', activebackground='white',activeforeground='black', font=('Arial', 28, 'bold'),     border=0).place(x=200, y=475)
            buttonA = Button(root4, text='Buy', command = buy ,width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 28, 'bold'),  border=0).place(x=755, y=475)
            
            root4.mainloop()


            # bg_home = PhotoImage(file='4.png')
            # Label(root4, image=bg_home).place(x=0, y=0)

            # buttonA = Button(root4, text='Sell', width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 28, 'bold'),     border=0).place(x=200, y=475)
            # buttonA = Button(root4, text='Buy', width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 28, 'bold'),  border=0).place(x=755, y=475)


            # root4.mainloop()

        
        
     
user = Entry(root1, width = 15, fg = 'black', border = 0, bg = '#E7E2D9', font = ('Microsoft YaHei UI Light', 15))
user.place(x = 645, y = 273)

password = Entry(root1, width = 15, fg = 'black', border = 0, show = '*',bg = '#E7E2D9', font = ('Microsoft YaHei UI Light', 15))
password.place(x = 645, y = 380)

def password_command():
    if password.cget('show') == '*':
        password.config(show='')
    else:
        password.config(show='*')

checkButton=Checkbutton(root1, bg='white',command=password_command)
checkButton.place(x=635, y=425)    


buttonA = Button(root1, text='Sign In', width=19, background='#735E59', foreground='white', activebackground='#735E59',activeforeground='black', font=('yu gothic ui', 15, 'bold'), border=0, command = signin).place(x=642, y=512)




root1.mainloop()







 