from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import *


root5 = Tk()
root5.title('Agent Login Page')
root5.geometry('1166x718-150-80')
root5.resizable(False, False)

bg_home = PhotoImage(file='5.png')
Label(root5, image=bg_home).place(x=0, y=0)

pname = Entry(root5, width = 30, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 20))
pname.place(x = 285, y = 146)

# pid = Entry(root5, width = 10, fg = 'black', border = 0, bg = 'white', font = ('Microsoft YaHei UI Light', 18))
# pid.place(x = 142, y = 136)

# pname = Entry(root5, width = 15, fg = 'black', border = 0, bg = 'white', font = ('Microsoft YaHei UI Light', 18))
# pname.place(x = 640, y = 146)

# ptype = Entry(root5, width = 15, fg = 'black', border = 0, bg = 'white', font = ('Microsoft YaHei UI Light', 18))
# ptype.place(x = 950, y = 146)

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

price = Entry(root5, width = 5, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
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
num.place(x = 590, y = 492)

vid = Entry(root5, width = 15, fg = 'black', border = 0, bg = '#ECEADA', font = ('Microsoft YaHei UI Light', 18))
vid.place(x = 280, y = 594)

buttonA = Button(root5, text='Submit', width=9, background='white', foreground='#735E59', activebackground='white', activeforeground='black', font=('Arial', 15, 'bold'), border=0).place(x=1000, y=642)
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
sex['values'] = ('--Select--','Male', 'Female')
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

root5.mainloop()