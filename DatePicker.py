# Import Required Library 
from tkinter import *
from tkcalendar import Calendar 
import tkinter as tk
def start():
    # Create Object 
    root = Tk() 
    root.title("Started Date Picker")
    # Set geometry 
    root.geometry("1920x1080") 
    introduction = tk.Label(root,text=("\n\n\n\nPick a date and click 'Get Date' \n After confirming, click'Continue after Getting Date'"),font=("Arial",16))
    introduction.pack()
    # Add Calender 
    cal = Calendar(root, selectmode = 'day', 
                year = 2022, month = 1, 
                day = 1) 
    
    cal.pack(pady = 20) 
    date = Label(root, text = "") 
    date.pack(pady = 20)
    def grad_date(): 
        date.config(text = "Selected Started Date is: " + cal.get_date(), font=24)
        global final_result
        final_result=cal.get_date()
        
    # Add Button and Label 
    Button(root, text = "Get Date",height=5,width=20, font=48,
        command = grad_date).pack(pady = 20) 
    
    #Exit Button
    def quit():
        root.destroy()
    Button(root, text = "Continue after Getting Date", font=24,
        command = quit).pack(pady = 20) 
 
    # Excecute Tkinter 
    root.mainloop()
    return final_result