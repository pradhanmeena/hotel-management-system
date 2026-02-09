from tkinter import *
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from datetime import datetime
from database_details import DatabaseDetails

class Room_win:
    def __init__(self,root):
        self.root=root
        self.root.title("APNA HOTEL")
        self.root.geometry("1111x528+243+160")
        #++++++++++++++Variables for database details
        self.db=DatabaseDetails()
        Dataframe=Frame(self.root,relief=RIDGE,bg="#091E42")
        Dataframe.place(x=0,y=0,width=1111,height=528)

        #==========================variables========================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_Availblity=StringVar()
        self.var_Meal=StringVar()
        self.var_numofdays=StringVar()
        self.var_tax=StringVar()
        self.var_subtotal=StringVar()
        self.var_Totalcost=StringVar()
        #_____________________lables___________________

        L1title=Button(Dataframe,text="Rooms Details",bg="#091E42",fg="#fff",font=("Arial bold",15))
        L1title.place(x=120,y=6,width=815,height=30)

        label_frame_left=LabelFrame(Dataframe,text="Rooms Booking Details",font=("Arial bold",10),relief=RIDGE,bg="#091E42",fg="white")
        label_frame_left.place(x=5,y=51,width=415,height=467)

        l1=Label(Dataframe,text="Customer Contact",font=("Arial bold",12),bg="#091E42",fg="white")
        l1.place(x=15,y=80)
        l2=Label(Dataframe,text="Check In Date",font=("Arial bold",12),bg="#091E42",fg="white")
        l2.place(x=15,y=115)
        l3=Label(Dataframe,text="Check Out Date",font=("Arial bold",12),bg="#091E42",fg="white")
        l3.place(x=15,y=150)
        l4=Label(Dataframe,text="Room Type",font=("Arial bold",12),bg="#091E42",fg="white")
        l4.place(x=15,y=185)
        l5=Label(Dataframe,text="Available Rooms",font=("Arial bold",12),bg="#091E42",fg="white")
        l5.place(x=15,y=220)
        l6=Label(Dataframe,text="Meal",font=("Arial bold",12),bg="#091E42",fg="white")
        l6.place(x=15,y=255)
        l7=Label(Dataframe,text="Number Of Days",font=("Arial bold",12),bg="#091E42",fg="white")
        l7.place(x=15,y=290)
        l8=Label(Dataframe,text="Paid Tax",font=("Arial bold",12),bg="#091E42",fg="white")
        l8.place(x=15,y=325)
        l9=Label(Dataframe,text="Sub Total",font=("Arial bold",12),bg="#091E42",fg="white")
        l9.place(x=15,y=360)
        l10=Label(Dataframe,text="Total Cost",font=("Arial bold",12),bg="#091E42",fg="white")
        l10.place(x=15,y=395)

        #==========================4 buttons===============================
        frm=LabelFrame(Dataframe,text="",relief=RIDGE,bg="#fff",fg="black")
        frm.place(x=12,y=464,width=400,height=45)


        Addb=Button(Dataframe,text="Add",font=("Arial Bold",10),bg="#091E42",fg="white",command=self.add_button)
        Addb.place(x=18,y=472,width=85,height=30)

        Updb=Button(Dataframe,text="Update",font=("Arial Bold",10),bg="#091E42",fg="white",command=self.Update)
        Updb.place(x=118,y=472,width=85,height=30)

        Delb=Button(Dataframe,text="Delete",font=("Arial Bold",10),bg="#091E42",fg="white",command=self.Delete)
        Delb.place(x=218,y=472,width=85,height=30)

        Resb=Button(Dataframe,text="Reset",font=("Arial Bold",10),bg="#091E42",fg="white",command=self.Reset)
        Resb.place(x=318,y=472,width=85,height=30)



        #Enteris_____________________________________________________

        Contact=Entry(Dataframe,textvariable=self.var_contact,font=("Arial bold",10),bg="white")
        Contact.place(x=180,y=80,width=130)

        
        Date=Entry(Dataframe,textvariable=self.var_checkin,font=("Arial bold",10),bg="white",)
        Date.place(x=180,y=115,width=215)
        
        Date2=Entry(Dataframe,textvariable=self.var_checkout,font=("Arial bold",10),bg="white")
        Date2.place(x=180,y=150,width=215)

        connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
        mycur=connection.cursor()
        mycur.execute("select Roomtype from room_data;")
        roomtype=mycur.fetchall()

        Room_c=ttk.Combobox(Dataframe,textvariable=self.var_roomtype,font=("Arial bold",10),state="readonly")
        Room_c["values"]=roomtype
        Room_c.current(0)
        Room_c.place(x=180,y=185,width=215)
        
        connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
        mycur=connection.cursor()
        mycur.execute("select Roomno from room_data;")
        rows=mycur.fetchall()

        Available_c=ttk.Combobox(Dataframe,textvariable=self.var_Availblity,font=("Arial bold",10))
        Available_c["values"]=rows
        Available_c.current(0)
        Available_c.place(x=180,y=220,width=215)
        
        Meal=Entry(Dataframe,textvariable=self.var_Meal,font=("Arial bold",10),bg="white")
        Meal.place(x=180,y=255,width=215)
        
        Days=Entry(Dataframe,textvariable=self.var_numofdays,font=("Arial bold",10),bg="white")
        Days.place(x=180,y=290,width=215)
        
        Tax=Entry(Dataframe,textvariable=self.var_tax,font=("Arial bold",10),bg="white")
        Tax.place(x=180,y=325,width=215)

        Sub_Total=Entry(Dataframe,textvariable=self.var_subtotal,font=("Arial bold",10),bg="white")
        Sub_Total.place(x=180,y=360,width=215)

        Total=Entry(Dataframe,textvariable=self.var_Totalcost,font=("Arial bold",10),bg="white")
        Total.place(x=180,y=395,width=215)

              #==============Buttons============
        Fetchb=Button(Dataframe,text="Fetch Data",font=("Arial Bold",10),bg="#091E42",fg="white",command=self.Fetch_contact)
        Fetchb.place(x=316,y=79,width=80,height=22)
        Bill=Button(Dataframe,text="Generat bill ",font=("Arial Bold",10),bg="#091E42",fg="white",command=self.total)
        Bill.place(x=296,y=430,width=100,height=22)

        #=============================dtails frame,button & Table=================

        Tableframe=LabelFrame(Dataframe,text="View Details & Search system",font=("Arial bold",10),relief=RIDGE,bg="#091E42",fg="white")
        Tableframe.place(x=425,y=198,width=681,height=320)

        Searchb=Button(Tableframe,text="Search",font=("Arial Bold",10),bg="#091E42",fg="white",command=self.search)
        Searchb.place(x=20,y=15,width=100,height=26)

        self.search_var=StringVar()

        Search_c=ttk.Combobox(Tableframe,font=("Arial bold",10),state="readonly")
        Search_c["values"]=("","Contact ","roomavailablity")
        Search_c.current(0)
        Search_c.place(x=135,y=15,width=140,height=25)

        self.txt_var=StringVar()
        
        Id=Entry(Tableframe,font=("Arial bold",10),bg="white")
        Id.place(x=293,y=15,width=140,height=25)

        Showb=Button(Tableframe,text="Show all",font=("Arial Bold",10),bg="#091E42",fg="white")
        Showb.place(x=450,y=15,width=100,height=26)

        #=========================================Show Data table=================================================
        Dframe=LabelFrame(Dataframe,text="",font=("Arial bold",10),relief=RIDGE,bg="#091E42",fg="white")
        Dframe.place(x=431,y=258,width=670,height=255)

        scroll_x=ttk.Scrollbar(Dframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Dframe,orient=VERTICAL)

        self.room_table=ttk.Treeview(Dframe,column=("Contact","checkindate","checkOutdate","Roomtype","roomavailablity","meal",

                                                            "NumberofDays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        

        self.room_table.heading("Contact",text="Contact")
        self.room_table.heading("checkindate",text="check in ")
        self.room_table.heading("checkOutdate",text="check Out ")
        self.room_table.heading("Roomtype",text="Room type")
        self.room_table.heading("roomavailablity",text="room No.")
        self.room_table.heading("meal",text="meal")
        self.room_table.heading("NumberofDays",text="Number of Days")

        self.room_table["show"]="headings"
        
        self.room_table.column("Contact",width=100)
        self.room_table.column("checkindate",width=80)
        self.room_table.column("checkOutdate",width=80)
        self.room_table.column("Roomtype",width=60)
        self.room_table.column("roomavailablity",width=60)
        self.room_table.column("meal",width=35)
        self.room_table.column("NumberofDays",width=50)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_button(self):
        
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Erroe","all fild are required,\nso fill all blanks carefully",parent=self.root)
        else:
            
            try:
                
                connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
                mycur=connection.cursor()
                mycur.execute("insert into  room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_contact.get(),self.var_checkin.get()
                                                                                ,self.var_checkout.get()
                                                                                ,self.var_roomtype.get(),self.var_Availblity.get()
                                                                                ,self.var_Meal.get(),self.var_numofdays.get()))
            

                
                
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("success","Room has been Booked",parent=self.root)

            except Exception as es:
                messagebox.showwarning("warning",f"Something went wrong:{str(es)}",parent=self.root)

    def search(self):
        
        connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
        mycur=connection.cursor()
        
        mycur.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_var.get())+"%'")
        row=mycur.fetchall()
        if len(row)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in row:
                self.room_table.insert("",END,values=i)
            connection.commit()
        
        connection.close()
    

    def Update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","please enter availbal room",parent=self.root)
        else:
            connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
            mycur=connection.cursor()
            mycur.execute("Update room set check_in=%s,check_out=%s,Room_type=%s,room_available=%s,Meal=%s,Numberofdays=%s where Contact=%s",(
                                                                                                self.var_checkin.get(),self.var_checkout.get()
                                                                                               ,self.var_roomtype.get(),self.var_Availblity.get(),self.var_Meal.get(),self.var_numofdays.get()
                                                                                               ,self.var_contact.get()))
        connection.commit()
        self.fetch_data()
        connection.close()
        messagebox.showinfo("Cngratulations","Room data successfully update")

    def Delete(self):
        Delete=messagebox.askyesno("Apna Hotel","Do you want delete this customer",parent=self.root)
        if Delete>0:
            connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
            mycur=connection.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            mycur.execute(query,value)
        else:
            if not Delete:
                return
        connection.commit()
        self.fetch_data()
        connection.close()
        messagebox.showinfo("Cngratulations","Your room data Has been deleted",parent=self.root)

    def Reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_Availblity.set("")
        self.var_Meal.set("")
        self.var_numofdays.set("")
        self.var_tax.set("")
        self.var_subtotal.set("")
        self.var_Totalcost.set("")
        


    def get_cursor(self,event=""):
        cursor=self.room_table.focus()
        i_stor=self.room_table.item(cursor)
        row=i_stor["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_Availblity.set(row[4])
        self.var_Meal.set(row[5])
        self.var_numofdays.set(row[6])

    
    def fetch_data(self):
        connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
        mycur=connection.cursor()
        mycur.execute("select * from room")
        fetch_data=mycur.fetchall()
        if fetch_data!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in fetch_data:
                self.room_table.insert("",END,values=i)
                connection.commit()
            connection.close()

    
        
        
        

    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","please enter contact number",parent=self.root)
        else:
            connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
            mycur=connection.cursor()
            query=("select name from customer where mobile=%s")
            value=(self.var_contact.get(),)
            mycur.execute(query,value)
            row=mycur.fetchone()
            if row==None:
                messagebox.showerror("Error","This number Not found",parent=self.root)
            else:
                connection.commit()
          
                connection.close()

                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2,bg="#fff")
                showdataframe.place(x=426,y=59,width=300,height=125)
                
                namelabel=Label(showdataframe,text="Name :",bg="#fff",font=("Arial bold",8))
                namelabel.place(x=10,y=10)
                
                label1=Label(showdataframe,text=row,bg="#fff",font=("Arial bold",8))
                label1.place(x=90,y=10)

                connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
                mycur=connection.cursor()
                query=("select Gender from customer where mobile=%s")
                value=(self.var_contact.get(),)
                mycur.execute(query,value)
                row=mycur.fetchone()

                genderlabel=Label(showdataframe,text="Gender :",bg="#fff",font=("Arial bold",8))
                genderlabel.place(x=10,y=29)
                
                label2=Label(showdataframe,text=row,bg="#fff",font=("Arial bold",8))
                label2.place(x=90,y=29)

                connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
                mycur=connection.cursor()
                query=("select Email from customer where mobile=%s")
                value=(self.var_contact.get(),)
                mycur.execute(query,value)
                row=mycur.fetchone()

                genderlabel=Label(showdataframe,text="Email :",bg="#fff",font=("Arial bold",8))
                genderlabel.place(x=10,y=44)
                
                label2=Label(showdataframe,text=row,bg="#fff",font=("Arial bold",8))
                label2.place(x=90,y=44)

                connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
                mycur=connection.cursor()
                query=("select Nationality from customer where mobile=%s")
                value=(self.var_contact.get(),)
                mycur.execute(query,value)
                row=mycur.fetchone()

                genderlabel=Label(showdataframe,text="Nation :",bg="#fff",font=("Arial bold",8))
                genderlabel.place(x=10,y=61)
                
                label2=Label(showdataframe,text=row,bg="#fff",font=("Arial bold",8))
                label2.place(x=90,y=61)

                connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
                mycur=connection.cursor()
                query=("select Address from customer where mobile=%s")
                value=(self.var_contact.get(),)
                mycur.execute(query,value)
                row=mycur.fetchone()

                genderlabel=Label(showdataframe,text="Address :",bg="#fff",font=("Arial bold",8))
                genderlabel.place(x=10,y=78)
                
                label2=Label(showdataframe,text=row,bg="#fff",font=("Arial bold",8))
                label2.place(x=90,y=78)

    def total(self):
        indate=self.var_checkin.get()
        outdate=self.var_checkout.get()
        indate=datetime.strptime(indate,"%d/%m/%Y")
        outdate=datetime.strptime(outdate,"%d/%m/%Y")
        self.var_numofdays.set(abs(outdate-indate).days)

        if (self.var_Meal.get()=="BreakFast" and self.var_roomtype.get()=="single"):
            q1=float(300.0)
            q2=float(900.0)
            q3=float(self.var_numofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)

            tax="Rs."+str("%.2f"%((q5)*0.9))
            SubTotal="Rs."+str("%.2f"%((q5)))
            TotalTax="Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.var_tax.set(tax)
            self.var_subtotal.set(SubTotal)
            self.var_Totalcost.set(TotalTax)

        elif (self.var_Meal.get()=="Launch" and self.var_roomtype.get()=="Laxury"):
            q1=float(500.0)
            q2=float(1500.0)
            q3=float(self.var_numofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)

            tax="Rs."+str("%.2f"%((q5)*0.11))
            SubTotal="Rs."+str("%.2f"%((q5)))
            TotalTax="Rs."+str("%.2f"%(q5+((q5)*0.11)))
            self.var_tax.set(tax)
            self.var_subtotal.set(SubTotal)
            self.var_Totalcost.set(TotalTax)
            
            
            
            
            

            


                
                

        

        
        

if __name__=="__main__":
    root=Tk()
    obj=Room_win(root)
    root.mainloop()
