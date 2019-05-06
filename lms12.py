from tkinter import *
from tkinter import ttk
import json
import sys
import random
import datetime

class poolLMS(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        self.container=Frame(self)
        self.container.pack(fill=BOTH,expand=True)

        self.ls={}

        for F in [homePage,Manager,Employee,Manager_signup,Employee_signup,Manager_login,Employee_login]:
            fr=F(self.container,self)
            self.ls[F]=fr
            fr.grid(row=0,column=0,sticky="nsew",padx=100,pady=100)

        self.show_frame(homePage)

    def add_frame(self,frame):
        fr=frame(self.container,self)
        self.ls[frame]=fr
        fr.grid(row=0,column=0,sticky="nsew",padx=100,pady=100)

    def show_frame(self,frame):
        self.ls[frame].tkraise()


class homePage(Frame):
    def __init__(self,parent,root):
        Frame.__init__(self,parent)
        l1=Label(self,text="Home Page",font=("Verdana",25)).pack()
        b1=ttk.Button(self,text="Manager",command=lambda:root.show_frame(Manager))
        b1.pack()
        b2=ttk.Button(self,text="Employee",command=lambda:root.show_frame(Employee))
        b2.pack()

class Manager(Frame):
    def __init__(self,parent,root):
        Frame.__init__(self,parent)
        l1=Label(self,text="Manager",font=("Verdana", 25)).pack()
        b1=ttk.Button(self,text="Login",command=lambda:root.show_frame(Manager_login))
        b1.pack()
        b2=ttk.Button(self,text="Sign Up",command=lambda:root.show_frame(Manager_signup))
        b2.pack()
        b3=ttk.Button(self,text="Back",command=lambda:root.show_frame(homePage))
        b3.pack(pady=20)

class Employee(Frame):
    def __init__(self,parent,root):
        Frame.__init__(self,parent)
        l1=Label(self,text="Employee",font=("Verdana", 25)).pack()
        b1=ttk.Button(self,text="Login",command=lambda:root.show_frame(Employee_login))
        b1.pack()
        b2=ttk.Button(self,text="Sign Up",command=lambda:root.show_frame(Employee_signup))
        b2.pack()
        b3=ttk.Button(self,text="Back",command=lambda:root.show_frame(homePage))
        b3.pack(pady=20)

class Manager_signup(Frame):
    def __init__(self,parent,root):
        Frame.__init__(self,parent)
        self.l=Label(self,text="Manager",font=("Verdana", 25))
        self.l.grid(row=0,column=0,columnspan=2)
        self.l1=Label(self,text="First Name:")
        self.l1.grid(row=1,column=0,sticky="e")
        self.e1=Entry(self)
        self.e1.grid(row=1,column=1)
        self.l2=Label(self,text="Last Name:")
        self.l2.grid(row=2,column=0,sticky="e")
        self.e2=Entry(self)
        self.e2.grid(row=2,column=1)
        self.l3=Label(self,text="ID:")
        self.l3.grid(row=3,column=0,sticky="e")
        self.e3=Entry(self)
        self.e3.grid(row=3,column=1)
        self.l4=Label(self,text="Password:")
        self.l4.grid(row=4,column=0,sticky="e")
        self.e4=Entry(self)
        self.e4.grid(row=4,column=1)
        self.b1=ttk.Button(self,text="Submit")
        self.b1.grid(columnspan=2)
        self.b1.bind("<Button-1>",self.get_manager_data)
        self.b2=ttk.Button(self,text="Back",command=lambda:root.show_frame(Manager))
        self.b2.grid(columnspan=2,pady=10)

    def get_manager_data(self,event):
        self.d={}
        self.d["First Name"]=self.e1.get()
        self.d["Last Name"]=self.e2.get()
        self.d["ID"]=self.e3.get()
        self.d["Password"]=self.e4.get()
        manager_data.append(self.d)
        with open('Manager.json','w') as f:
            json.dump(manager_data,f)
        root.show_frame(Manager_login)

class Employee_signup(Frame):
    def __init__(self,parent,root):
        Frame.__init__(self,parent)
        self.l=Label(self,text="Employee",font=("Verdana", 25))
        self.l.grid(row=0,column=0,columnspan=2)
        self.l1=Label(self,text="First Name:")
        self.l1.grid(row=1,column=0,sticky="e")
        self.e1=Entry(self)
        self.e1.grid(row=1,column=1)
        self.l2=Label(self,text="Last Name:")
        self.l2.grid(row=2,column=0,sticky="e")
        self.e2=Entry(self)
        self.e2.grid(row=2,column=1)
        self.l3=Label(self,text="ID:")
        self.l3.grid(row=3,column=0,sticky="e")
        self.e3=Entry(self)
        self.e3.grid(row=3,column=1)
        self.l4=Label(self,text="Password:")
        self.l4.grid(row=4,column=0,sticky="e")
        self.e4=Entry(self)
        self.e4.grid(row=4,column=1)
        self.b1=ttk.Button(self,text="Submit")
        self.b1.grid(columnspan=2)
        self.b1.bind("<Button-1>",self.get_emp_data)
        self.b2=ttk.Button(self,text="Back",command=lambda:root.show_frame(Employee))
        self.b2.grid(columnspan=2,pady=10)

    def get_emp_data(self,event):
        self.d={}
        self.d["First Name"]=self.e1.get()
        self.d["Last Name"]=self.e2.get()
        self.d["ID"]=self.e3.get()
        self.d["Password"]=self.e4.get()
        employee_data.append(self.d)
        with open('Employee.json','w') as f:
            json.dump(employee_data,f)
        root.show_frame(Employee_login)

class Manager_login(Frame):
    def __init__(self,parent,root):
        Frame.__init__(self,parent)
        self.l=Label(self,text="Manager Login",font=("Verdana",25))
        self.l.grid(row=0,columnspan=2)
        self.l1=Label(self,text="ID:")
        self.l1.grid(row=1,column=0,sticky='e')
        self.e1=Entry(self)
        self.e1.grid(row=1,column=1)
        self.l2=Label(self,text="Password:")
        self.l2.grid(row=2,column=0,sticky='e')
        self.e2=Entry(self,show="•")
        self.e2.grid(row=2,column=1)
        self.b1=ttk.Button(self,text="Login")
        self.b1.bind("<Button-1>",self.check_manager)
        self.b1.grid(row=3,columnspan=2)
        self.b2=ttk.Button(self,text="Back",command=lambda:root.show_frame(Manager))
        self.b2.grid(columnspan=2,pady=10)

    def check_manager(self,event):
        id=self.e1.get()
        pw=self.e2.get()
        global logged_manager
        with open('Manager.json','r') as f:
            d=json.load(f)
        for t in d:
            if t['ID']==id and t['Password']==pw:
                logged_manager=t
                root.add_frame(Manager_pageone)
                root.show_frame(Manager_pageone)
                break
        if id != t['ID'] or pw != t['Password']:
            self.l3=Label(self,text="Wrong ID or Password")   
            self.l3.grid(row=5,columnspan=2)     


class Employee_login(Frame):
    def __init__(self,parent,root):
        Frame.__init__(self,parent)
        self.l=Label(self,text="Employee Login",font=("Verdana",25))
        self.l.grid(row=0,columnspan=2)
        self.l1=Label(self,text="ID:")
        self.l1.grid(row=1,column=0,sticky='e')
        self.e1=Entry(self)
        self.e1.grid(row=1,column=1)
        self.l2=Label(self,text="Password:")
        self.l2.grid(row=2,column=0,sticky='e')
        self.e2=Entry(self,show="•")
        self.e2.grid(row=2,column=1)
        self.b1=ttk.Button(self,text="Login")
        self.b1.bind("<Button-1>",self.check_employee)
        self.b1.grid(row=3,columnspan=2)
        self.b2=ttk.Button(self,text="Back",command=lambda:root.show_frame(Employee))
        self.b2.grid(columnspan=2,pady=10)

    def check_employee(self,event):
        id=self.e1.get()
        pw=self.e2.get()
        global logged_employee
        with open('Employee.json','r') as f:
            d=json.load(f)
        for t in d:
            if t['ID']==id and t['Password']==pw:
                logged_employee=t
                root.add_frame(Employee_pageone)
                root.show_frame(Employee_pageone)
                break
        if id != t['ID'] or pw != t['Password']:
            self.l3=Label(self,text="Wrong ID or Password")   
            self.l3.grid(row=5,columnspan=2)  


class Manager_pageone(Frame):
    def __init__(self,parent,root):
        Frame.__init__(self,parent)
        self.l=Label(self,text="Welcome "+logged_manager["First Name"],font=("Verdana",25))
        self.l.grid(row=0,column=0,columnspan=2)
        self.b1=ttk.Button(self,text="Leave Requests",command=self.show_leave_requests)
        self.b1.grid(row=1,column=0,columnspan=2,pady=10)
        self.b2=ttk.Button(self,text="Employees List",command=self.set_employee_list)
        self.b2.grid(row=2,column=0,columnspan=2,pady=10)
        self.b3=ttk.Button(self,text="Log Out",command=lambda:root.show_frame(homePage))
        self.b3.grid(row=3,column=0,columnspan=2,pady=10)

    def set_employee_list(self):
        root.add_frame(Employee_list)
        root.show_frame(Employee_list)

    def show_leave_requests(self):
        root.add_frame(Manager_leave_requests)
        root.show_frame(Manager_leave_requests)

class Manager_leave_requests(Frame):
    def __init__(self,parent,root):
        Frame.__init__(self,parent)
        self.Request_ID=[]
        self.Employee_ID=[]
        self.Employee_Name=[]
        self.From=[]
        self.To=[]
        self.Status=[]
        i=0
        self.Accept=[]
        self.Reject=[]
        j=0
        for key in leave_request[0]:
            l=Label(self,text=key,padx=10,pady=10,font=(15)).grid(row=0,column=j)
            j=j+1
        for t in leave_request:
            self.Request_ID.append(Label(self,text=t["Request ID"]))
            self.Request_ID[i].grid(row=i+1,column=0,padx=10,pady=5)
            self.Employee_ID.append(Label(self,text=t["Employee ID"]))
            self.Employee_ID[i].grid(row=i+1,column=1,padx=10,pady=5)
            self.Employee_Name.append(Label(self,text=t["Employee Name"]))
            self.Employee_Name[i].grid(row=i+1,column=2,padx=10,pady=5)
            self.From.append(Label(self,text=t["From"]))
            self.From[i].grid(row=i+1,column=3,padx=10,pady=5)
            self.To.append(Label(self,text=t["To"]))
            self.To[i].grid(row=i+1,column=4,padx=10,pady=5)
            self.Status.append(Label(self,text=t["Status"]))
            self.Status[i].grid(row=i+1,column=5,padx=10,pady=5)
            self.Accept.append(ttk.Button(self,text="Accept"))
            self.Accept[i].bind("<Button-1>",self.accepted)
            self.Accept[i].grid(row=i+1,column=6,padx=10,pady=5)
            self.Reject.append(ttk.Button(self,text="Reject"))
            self.Reject[i].bind("<Button-1>",self.rejected)
            self.Reject[i].grid(row=i+1,column=7,padx=10,pady=5)
            i=i+1
        self.b=ttk.Button(self,text="Back",command=lambda:root.show_frame(Manager_pageone)).grid(column=0,columnspan=8)
    
    def accepted(self,event):
        global leave_request
        x=event.widget.grid_info()['row'] 
        leave_request[x-1]["Status"]="Accepted"
        with open('Request.json','w') as f:
            json.dump(leave_request,f)
        root.add_frame(Manager_leave_requests)
        root.show_frame(Manager_leave_requests)

    def rejected(self,event):
        global leave_request
        x=event.widget.grid_info()['row'] 
        leave_request[x-1]["Status"]="Rejected"
        with open('Request.json','w') as f:
            json.dump(leave_request,f)
        root.add_frame(Manager_leave_requests)
        root.show_frame(Manager_leave_requests)

        
    
class Employee_list(Frame):
    def __init__(self,parent,root):
        Frame.__init__(self,parent)
        self.la=Label(self,text="Name",font=("Verdana",20))
        self.la.grid(row=0,column=0)
        self.lb=Label(self,text="ID",font=("Verdana",20),padx=20)
        self.lb.grid(row=0,column=1)
        l1={}
        l2={}
        i=1
        with open('Employee.json','r') as f:
            d=json.load(f)
            for t in d:
                l1[t['First Name']]=Label(self,text="{}) ".format(i)+t['First Name']+" "+t['Last Name'],font=(15))
                l1[t['First Name']].grid(row=i,column=0,sticky='w')
                l2[t['ID']]=Label(self,text=t['ID'],font=(15))
                l2[t['ID']].grid(row=i,column=1,padx=20,sticky='w')
                i=i+1
        self.b1=Button(self,text="Back",command=lambda:root.show_frame(Manager_pageone))
        self.b1.grid(columnspan=2,pady=10)


class Employee_pageone(Frame):
    def __init__(self,parent,root):
        Frame.__init__(self,parent)
        self.l=Label(self,text="Welcome "+logged_employee["First Name"],font=("Verdana",25))
        self.l.grid(row=0,column=0,columnspan=2)
        self.b1=ttk.Button(self,text="Request a Leave",command=self.set_leave)
        self.b1.grid(row=1,column=0,columnspan=2,pady=10)
        self.b2=ttk.Button(self,text="Previous Requests",command=self.show_leave)
        self.b2.grid(row=2,column=0,columnspan=2,pady=10)
        self.b3=ttk.Button(self,text="Log Out",command=lambda:root.show_frame(homePage))
        self.b3.grid(row=3,column=0,columnspan=2,pady=10)

    def set_leave(self):
        root.add_frame(Employee_leave_request)
        root.show_frame(Employee_leave_request)

    def show_leave(self):
        root.add_frame(Employee_show_leave)
        root.show_frame(Employee_show_leave)

class Employee_leave_request(Frame):
    def __init__(self,parent,root):
        Frame.__init__(self,parent)
        self.l=Label(self,text="Leave Request",font=("Verdana",25))
        self.l.grid(row=0,column=0,columnspan=3)
        self.l1=Label(self,text="From: ")
        self.l1.grid(row=1,column=0)
        self.e1=Entry(self)
        self.e1.grid(row=1,column=1)
        self.l2=Label(self,text="dd/mm/yyyy")
        self.l2.grid(row=1,column=3)
        self.l3=Label(self,text="To: ")
        self.l3.grid(row=2,column=0)
        self.e2=Entry(self)
        self.e2.grid(row=2,column=1)
        self.l4=Label(self,text="dd/mm/yyyy")
        self.l4.grid(row=2,column=3)
        self.b1=ttk.Button(self,text="Submit")
        self.b1.bind("<Button-1>",self.generate_leave)
        self.b1.grid(row=3,column=0,columnspan=3,pady=10)
        self.b2=Button(self,text="Back",command=lambda:root.show_frame(Employee_pageone))
        self.b2.grid(row=5,column=0,columnspan=3)

    def generate_leave(self,event):
        if self.check() == True:
            data={}
            global logged_employee
            global leave_request
            data["Request ID"]=random.randint(10000,100000)
            data["Employee ID"]=logged_employee["ID"]
            data["Employee Name"]=logged_employee["First Name"]+" "+logged_employee["Last Name"]
            data["From"]=self.e1.get()
            data["To"]=self.e2.get()
            data["Status"]="Pending"
            leave_request.append(data)
            with open('Request.json','w') as f:
                json.dump(leave_request,f)
            root.add_frame(Employee_show_leave)
            root.show_frame(Employee_show_leave)
        else:
            self.l5=Label(self,text="Enter proper dates")
            self.l5.grid(row=4,column=0,columnspan=3)

           

    def check(self):
        t1=self.e1.get().split('/')
        t2=self.e2.get().split('/')
        print(t1)
        print(t2)
        try:
            if datetime.date.today() <= datetime.date(year=int(t1[2]),month=int(t1[1]),day=int(t1[0])) < datetime.date(year=int(t2[2]),month=int(t2[1]),day=int(t2[0])):
                print("if")
                return True
            else:
                print("else")
                return False
        except:
            return False
        
        


class Employee_show_leave(Frame):
    def __init__(self,parent,root):
        Frame.__init__(self,parent)
        global leave_request
        global logged_employee
        self.li=[None]*6
        self.li[0]=Label(self,text="Request ID",font=("Verdana",15)).grid(row=0,column=0)
        self.li[1]=Label(self,text="Employee ID",font=("Verdana",15)).grid(row=0,column=1)
        self.li[2]=Label(self,text="Employee Name",font=("Verdana",15)).grid(row=0,column=2)
        self.li[3]=Label(self,text="From",font=("Verdana",15)).grid(row=0,column=3)
        self.li[4]=Label(self,text="To",font=("Verdana",15)).grid(row=0,column=4)
        self.li[5]=Label(self,text="Status",font=("Verdana",15)).grid(row=0,column=5)
        for i in range(0,len(leave_request)):
            if logged_employee["ID"]==leave_request[i]["Employee ID"]:
                self.l=Label(self,text=leave_request[i]["Request ID"]).grid(row=i+1,column=0)
                self.l=Label(self,text=leave_request[i]["Employee ID"]).grid(row=i+1,column=1)
                self.l=Label(self,text=leave_request[i]["Employee Name"]).grid(row=i+1,column=2)
                self.l=Label(self,text=leave_request[i]["From"]).grid(row=i+1,column=3)
                self.l=Label(self,text=leave_request[i]["To"]).grid(row=i+1,column=4)
                self.l=Label(self,text=leave_request[i]["Status"]).grid(row=i+1,column=5)
        self.b=ttk.Button(self,text="Back",command=lambda:root.show_frame(Employee_pageone))
        self.b.grid(columnspan=6)




logged_manager={}
logged_employee={}
manager_data=[]
employee_data=[]
leave_request=[]

with open('Request.json','r') as f:
    leave_request=json.load(f)
with open('Manager.json','r') as f:
    manager_data=json.load(f)
with open('Employee.json','r') as f:
    employee_data=json.load(f)

root=poolLMS() 
root.wm_title("Leave Management")
#root.geometry("400x400")
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
root.mainloop()