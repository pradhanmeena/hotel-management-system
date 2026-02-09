from tkinter import *

from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from customer_details import cust_win
from Room import Room_win
from details import details_win
from report import Report
from database_details import DatabaseDetails
import mysql.connector

def main():
    win=Tk()
    app=Login_win(win)
    win.mainloop()

class Login_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768")
        self.db=DatabaseDetails()
        frame2=Frame(bg="#091E42")
        frame2.place(x=0,y=0,width=1366,height=768)

        img2=Image.open(r"D:\python projects\Hotel pro\Main Project\Images\l3.png")
        img2=img2.resize((1366,768),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lbimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbimg.place(x=0,y=0,width=1366,height=768)

    

        self.Username=StringVar()
        self.Cnpass=StringVar()
        

       

        fram=Frame(lbimg,bd=3,relief=RIDGE,bg="#483c32")
        fram.place(x=488,y=115,width=350,height=370)

        title=Button(lbimg,text="Login your id",font=("Arial bold",13),bg="#483c32",fg="white")
        title.place(x=605,y=100)
        title1=Label(lbimg,text="~APNA HOTEL~",font=("Arial bold",20),bg="#483c32",fg="#E69D10")
        title1.place(x=550,y=170)

        
        u1=Label(lbimg,text="Username",font=("Arial bold",12),bg="#483c32",fg="white")
        u1.place(x=540,y=249)
        self.U=Entry(lbimg,font=("Arial bold",13),bg="#fff")
        self.U.place(x=645,y=250,width=150)

        u2=Label(lbimg,text="Password",font=("Arial bold",12),bg="#483c32",fg="white")
        u2.place(x=540,y=299)
        self.U2=Entry(lbimg,font=("Arial bold",13),bg="#fff",fg="black")
        self.U2.place(x=645,y=300,width=150)

        Forgetpass=Button(lbimg,text="Forget password",font=("Arial bold",8),bg="#483c32",fg="white",borderwidth=0,activebackground="#483c32",activeforeground="white")
        Forgetpass.place(x=540,y=430)

        title=Button(lbimg,text="Create a new account",font=("Arial bold",8),bg="#483c32",fg="white",borderwidth=0,activebackground="#483c32",activeforeground="white",command=self.Register_window)
        title.place(x=540,y=410)

        

        
        b=Button(lbimg,text="Back",font=("Arial bold",10),bg="#FFECD1",fg="#141413",command=self.root.destroy)
        b.place(x=550,y=360,width=90,height=25)
        b1=Button(lbimg,text="login",font=("Arial bold",10),bg="#FFECD1",fg="#141413",command=self.login)
        b1.place(x=685,y=360,width=90,height=25)

    def login(self):
        if self.U.get()=="" or self.U2.get()=="":
            messagebox.showerror("Error","all field required",parent=self.root)

        else:
            connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
            mycur=connection.cursor()
            mycur.execute("select * from Login where Username=%s and Password=%s",(self.U.get(),self.U2.get()))
            raw=mycur.fetchone()
            if raw==None:
                messagebox.showerror("Error","Invalid Username or password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Hotel(self.new_window)
                else:
                    if not open_main:
                        return
            connection.commit()
            connection.close()

    def Register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register_win(self.new_window)

class Register_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768")

        
        
        self.db=DatabaseDetails()

        img2=Image.open(r"D:\python projects\Hotel pro\Main Project\Images\l3.png")
        img2=img2.resize((1366,768),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lbimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbimg.place(x=0,y=0,width=1366,height=768)

        fram=Frame(lbimg,bd=3,relief=RIDGE,bg="#483c32")
        fram.place(x=320,y=115,width=650,height=370)

        

        #========================variables==============
        self.FName=StringVar()
        self.LName=StringVar()
        self.Cpass=StringVar()
        self.Cnpass=StringVar()
        self.Gender=StringVar()
        self.Contact=StringVar()
        self.Quetion=StringVar()
        self.Answer=StringVar()
        self.Country=StringVar()
        self.Username=StringVar()
        
        
        
        
        title=Button(lbimg,text="CREATE A NEW ACCOUNT",font=("Arial bold",13),bg="#483c32",fg="white")
        title.place(x=550,y=100)

        #=================Enterys left side
        
        self.E=Entry(lbimg,textvariable=self.FName,font=("Arial bold",10),bg="#fff")
        self.E.place(x=485,y=160,width=120)
        self.e2=Entry(lbimg,textvariable=self.Cpass,font=("Arial bold",10),bg="#fff")
        self.e2.place(x=485,y=210,width=120)
        self.e3=Entry(lbimg,textvariable=self.Contact,font=("Arial bold",10),bg="#fff")
        self.e3.place(x=485,y=260,width=120)
        self.e4=ttk.Combobox(lbimg,textvariable=self.Gender,font=("Arial bold",10),state="readonly")
        self.e4["values"]=("Select","male","Female","other")
        self.e4.place(x=485,y=310,width=120)
        self.e4.current(0)
        self.e5=ttk.Combobox(lbimg,textvariable=self.Quetion,font=("Arial bold",10),state="readonly")
        self.e5["values"]=("Select","Best friend Name?","Mother Name?","school Name?")
        self.e5.place(x=485,y=360,width=120)
        self.e5.current(0)
        
        

        #++++++++++++++++++++++++lABELS left side+++++++++++++++++++++++++++++++++
        l1=Label(lbimg,text="Enter First Name",font=("Arial bold",12),bg="#483c32",fg="white")
        l1.place(x=335,y=157)
        l2=Label(lbimg,text="Create Password",font=("Arial bold",12),bg="#483c32",fg="white")
        l2.place(x=335,y=207)
        l3=Label(lbimg,text="Enter Contact",font=("Arial bold",12),bg="#483c32",fg="white")
        l3.place(x=335,y=257)
        l4=Label(lbimg,text="Select Gender",font=("Arial bold",12),bg="#483c32",fg="white")
        l4.place(x=335,y=307)
        l5=Label(lbimg,text="select A Quetion",font=("Arial bold",12),bg="#483c32",fg="white")
        l5.place(x=335,y=357)

        

        #======================Enterys Right side

        self.En=Entry(lbimg,textvariable=self.LName,font=("Arial bold",10),bg="#fff")
        self.En.place(x=815,y=160,width=120)
        self.en2=Entry(lbimg,textvariable=self.Cnpass,font=("Arial bold",10),bg="#fff")
        self.en2.place(x=815,y=210,width=120)
        self.en3=Entry(lbimg,textvariable=self.Username,font=("Arial bold",10),bg="#fff")
        self.en3.place(x=815,y=260,width=120)
        self.en4=ttk.Combobox(lbimg,textvariable=self.Country,font=("Arial bold",10),state="readonly")
        self.en4["values"]=("Select","Afganisthan","Bangladesh","Bhutan","China","India","Myamar","Nepal","Pakisthan","Sri lanka","other")
        self.en4.place(x=815,y=310,width=120)
        self.en4.current(0)
        self.en5=Entry(lbimg,textvariable=self.Answer,font=("Arial bold",10),bg="#fff")
        self.en5.place(x=815,y=360,width=120)
       

        #++++++++++++++++++++++++lABELS Right side+++++++++++++++++++++++++++++++++
        l1=Label(lbimg,text="Enter Last Name",font=("Arial bold",12),bg="#483c32",fg="white")
        l1.place(x=650,y=157)
        l2=Label(lbimg,text="Conform Password",font=("Arial bold",12),bg="#483c32",fg="white")
        l2.place(x=650,y=207)
        l3=Label(lbimg,text="Create Username",font=("Arial bold",12),bg="#483c32",fg="white")
        l3.place(x=650,y=257)
        l4=Label(lbimg,text="Select Country",font=("Arial bold",12),bg="#483c32",fg="white")
        l4.place(x=650,y=307)
        l5=Label(lbimg,text="Enter Answer",font=("Arial bold",12),bg="#483c32",fg="white")
        l5.place(x=650,y=357)

        self.check=IntVar()

        checkbtn=Checkbutton(lbimg,variable=self.check,text="I Agree The Terms & Conditions",font=("Arial bold",8),
                             bg="#483c32",activebackground="#483c32",activeforeground="#483c32",onvalue=1,offvalue=0,fg="#FFECD1")
        checkbtn.place(x=335,y=400)

         #==========================Buttons =========
        self.b=Button(lbimg,text="BACK",font=("Arial bold",10),bg="#FFECD1",fg="#141413",command=self.root.destroy)
        self.b.place(x=487,y=440,width=130,height=30)
        self.b1=Button(lbimg,text="CREATE",font=("Arial bold",10),bg="#FFECD1",fg="#141413",command=self.Register_data)
        self.b1.place(x=665,y=440,width=130,height=30)

    

                
                
    #===============================================Function ++++++++++++++++++++++++++++++++++++++
    def Register_data(self):
        if self.FName.get()=="" or self.Quetion=="Select" or self.Username.get()=="":
            messagebox.showerror("ERROR","All fills are Required",parent=self.root)
        elif self.Cpass.get()!=self.Cnpass.get():
            messagebox.showerror("ERROR","Password are Not same",parent=self.root)
        elif self.check.get()==0:
            messagebox.showerror("ERROR","Agree term & Conditions",parent=self.root)
        else:
            connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
            mycur=connection.cursor()
            Q=("select * from Login where Contact=%s")
            value=(self.Contact.get(),)
            mycur.execute(Q,value)
            row=mycur.fetchone()
            if row!=None:
                messagebox.showerror("ERROR","This user Already exist\n try another contact ",parent=self.root)

            else:
                mycur.execute("insert into Login values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.FName.get(),self.LName.get() ,self.Cnpass.get(),
                                                                                          self.Contact.get(),self.Username.get(),self.Gender.get()  ,self.Country.get(),
                                                                                          self.Quetion.get(),self.Answer.get()
                                                                                          ))
                connection.commit()
                connection.close()
                messagebox.showinfo("Congratulations","Your Account Create successfully ",parent=self.root)

class Hotel:
    def __init__(self,root):
        self.root=root
        self.root.title("APNA HOTEL")
        self.root.geometry("1366x717")
        Dataframe=Frame(self.root,relief=RIDGE,bg="#091E42")
        Dataframe.place(x=0,y=0,width=1366,height=768)
        Dataframe2=Frame(self.root,relief=RIDGE,bg="#E69D10",bd=2)
        Dataframe2.place(x=0,y=0,width=1366,height=161)
        #_________________________________For image___________________________
        img2=Image.open(r"D:\python projects\Hotel pro\Main Project\Images\I2.png")
        img2=img2.resize((1366,562),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lbimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbimg.place(x=0,y=153,width=1366,height=562)
        img1=Image.open(r"D:\python projects\Hotel pro\Main Project\Images\Image.png")
        img1=img1.resize((1366,161),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lbimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbimg.place(x=0,y=0,width=1366,height=161)
        #_________________________________title & frame___________________________
        #L1title=Label(Dataframe2,text="APNA HOTEL",bg="#091E42",fg="#E69D10",font=("Arial bold",20))
        #L1title.place(x=0,y=15)
        main_frame=Frame(Dataframe,bd=3,relief=RIDGE,bg="#091E42")
        main_frame.place(x=0,y=125,width=1360,height=690)
        #________________________________buttons_____________________________________
        #Menu=Button(main_frame,text="MENU",bg="#091E42",fg="#E69D10",font=("Arial bold",15))
        #Menu.place(x=0,y=0,width=115,height=30)
        CUST=Button(lbimg,text="CUSTOMER",bg="#d4a97f",fg="#044d72",font=("Arial bold",15),command=self.cust_details)
        CUST.place(x=24,y=128,width=145,height=25)

        ROOM=Button(lbimg,text="ROOM",bg="#d4a97f",fg="#044d72",font=("Arial bold",15),command=self.Roombooking)
        ROOM.place(x=185,y=128,width=145,height=25)

        DETAILS=Button(lbimg,text="DETAILS",bg="#d4a97f",fg="#044d72",font=("Arial bold",15),command=self.details_add)
        DETAILS.place(x=347,y=128,width=145,height=25)

        REPORT=Button(lbimg,text="REPORT",bg="#d4a97f",fg="#044d72",font=("Arial bold",15),command=self.report2)
        REPORT.place(x=514,y=128,width=145,height=25)

        LOGOUT=Button(lbimg,text="LOGOUT",bg="#d4a97f",fg="#044d72",font=("Arial bold",15),command=self.logout)
        LOGOUT.place(x=680,y=128,width=145,height=25)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)
    def Roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Room_win(self.new_window)
    def details_add(self):
        self.new_window=Toplevel(self.root)
        self.app=details_win(self.new_window)
    def report2(self):
        self.new_window=Toplevel(self.root)
        self.app=Report(self.new_window)
    def logout(self):
        confirm=messagebox.askyesno("Confirmation","are you sure??",parent=self.root)
        if confirm>0:
            self.root.destroy()
        
            
    
        
if __name__=="__main__":
    root=Tk()
    app=Login_win(root)
    root.mainloop()
