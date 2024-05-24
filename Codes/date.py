import tkinter as tk
import tkcalendar as calendar

def show_selected_date():
    selected_date = cal.get_date()
    print("Selected date:", selected_date)

root = tk.Tk()

# Create first calendar widget
cal1 = calendar.Calendar(root)
cal1.grid(row=0, column=0, padx=10, pady=10)

# Create second calendar widget
cal2 = calendar.Calendar(root)
cal2.grid(row=0, column=1, padx=10, pady=10)

# Create a button to get selected date from first calendar
btn1 = tk.Button(root, text="Get Selected Date (Calendar 1)", command=show_selected_date)
btn1.grid(row=1, column=0, padx=10, pady=10)

# Create a button to get selected date from second calendar
btn2 = tk.Button(root, text="Get Selected Date (Calendar 2)", command=show_selected_date)
btn2.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
