
# first install tkinter library if you don't have yet
from tkinter import *

gui2=Tk()

def clear_entry():
    employee_name2.delete(0,END)
    salary2.delete(0,END)
    allowance2.delete(0,END)
    tax_deduction2.delete(0,END)
    net_salary2.delete(0,END)
    

def calculate_salary():
    global tax_deduction2
    global salary2
    global allowance2
    salary_allow = int(salary2.get())+int(allowance2.get())
    tax=''
    if salary_allow <= 25000:
        tax=0
    elif salary_allow >= 25000 or salary_allow <= 50000:
        tax = (salary_allow - 25000) * 0.25
    elif salary_allow >= 50000 or salary_allow <= 100000:
        tax = (salary_allow - 50000) * 0.5 + 5000
    elif salary_allow >= 100000 or salary_allow <= 1000000:
        tax = (salary_allow - 100000) * 1 + 10000
    else:
        tax="wrong value"
    tax_deduction2.insert(0,tax)
    calcu=salary_allow-tax
    net_salary2.insert(0,calcu)
def save_data():
    fatch='1.) Employee Name \t'+str(employee_name2.get()),'\n','2.) Salary \t'+str(salary2.get())+'\n'+'3.) Allowance \t'+str(allowance2.get())+'\n'+'4.) Tax Deduction \t'+str(tax_deduction2.get())+'\n'+'5.) Net Salary \t'+str(net_salary2.get()),'\n\n\n'
    with open('employeinfo.txt','a') as file:
        file.writelines(fatch)
        
gui2.title('Employee Salary Calculator')
gui2.geometry('500x444')
gui2.minsize(500,444)
gui2.maxsize(500,444)
gui2.configure(bg='#C39BD3')

# makibng name labels and grid
heading2=Label(gui2,text="Employee Salary Calculator \n",font=('Times 30 italic underline'),bg='#C39BD3')
employee_name=Label(gui2,text="Empoyee Name",font=('Times 18'),bg='#C39BD3')
salary=Label(gui2,text="Salary",font=('Times 18'),bg='#C39BD3')
allownance=Label(gui2,text="Allownace",font=('Times 18'),bg='#C39BD3')
tax_deduction=Label(gui2,text="Tax Deduction",font=('Times 18'),bg='#C39BD3')
net_salary=Label(gui2,text="Net Salary",font=('Times 18'),bg='#C39BD3')
bln=Label(gui2,text='\n',bg='#C39BD3').grid(row=6)
# all labels grids
heading2.grid(row=0,columnspan=5)
employee_name.grid(row=1,column=0)
salary.grid(row=2,column=0)
allownance.grid(row=3,column=0)
tax_deduction.grid(row=4,column=0)
net_salary.grid(row=5,column=0)

# making entry widget for user input
employee_name2=Entry(gui2,width=20,font=('Times 19 bold'),relief=SUNKEN,bd=6)
salary2=Entry(gui2,width=20,font=('Times 19 bold'),relief=SUNKEN,bd=6)
allowance2=Entry(gui2,width=20,font=('Times 19 bold'),relief=SUNKEN,bd=6)
tax_deduction2=Entry(gui2,width=20,font=('Times 19 bold'),relief=SUNKEN,bd=6)
net_salary2=Entry(gui2,width=20,font=('Times 19 bold'),relief=SUNKEN,bd=6)
# all entry grid
employee_name2.grid(row=1,column=1)
salary2.grid(row=2,column=1)
allowance2.grid(row=3,column=1)
tax_deduction2.grid(row=4,column=1)
net_salary2.grid(row=5,column=1)

# making button for perfoming task
save_button=Button(gui2,text='Save',width=15,font=('Arial 11 bold'),bg='#58D68D',activebackground='#58D68D',relief=FLAT,bd=8,command=save_data)
calculate_button=Button(gui2,text='Calculate Salary',width=15,font=('Arial 11 bold'),bg='#85C1E9',activebackground='#3498DB',relief=FLAT,bd=8,comman=calculate_salary)
clear_button=Button(gui2,text='Clear Entry',width=15,font=('Arial 11 bold'),bg="#F1C40F",activebackground='#F4D03F',relief=FLAT,bd=8,command=clear_entry)
exit_button=Button(gui2,text='Exit',width=15,font=('Arial 11 bold'),bg='#E74C3C',activebackground='#F5B7B1',relief=FLAT,bd=8,comman=gui2.destroy)
# all button grid
save_button.grid(row=7,column=0)
calculate_button.grid(row=7,column=1)
clear_button.grid(row=8,column=0)
exit_button.grid(row=8,column=1)

gui2.mainloop()
