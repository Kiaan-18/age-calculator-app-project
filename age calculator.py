from tkinter import*
from tkinter import messagebox
from datetime import date
def calculate_age():
    try:
        day=int(day_entry.get())
        month=int(month_entry.get())
        year=int(year_entry.get())
        birth_date=date(year,month,day)
        today=date.today()
        age=today.year-birth_date.year-((today.month,today.day)<(birth_date.month,birth_date.day))
        messagebox.showinfo("Age Calculator",f"Your age is:{age}years")
    except ValueError:
        messagebox.showerror("invalid Input","Please enter valid numbers for day,month and year")
    except Exception as e:
        messagebox.showerror("Error",str(e))
root=Tk()
root.title("Age Calculator")
Label(root,text="Day:").grid(row=0,column=0,padx=10,pady=5)
Label(root,text="Month:").grid(row=1,column=0,padx=10,pady=5)
Label(root,text="Year:").grid(row=2,column=0,padx=10,pady=5)
day_entry=Entry(root)
month_entry=Entry(root)
year_entry=Entry(root)
day_entry.grid(row=0,column=1,padx=10,pady=5)
month_entry.grid(row=1,column=1,padx=10,pady=5)
year_entry.grid(row=2,column=1,padx=10,pady=5)
Button(root,text="Calculate Age",command=calculate_age).grid(row=3,column=0,columnspan=2,pady=10)
root.mainloop()