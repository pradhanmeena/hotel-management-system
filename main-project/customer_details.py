from tkinter import *
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from database_details import DatabaseDetails

class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("APNA HOTEL")
        self.root.geometry("1111x528+243+160")
        Dataframe=Frame(self.root,relief=RIDGE,bg="#091E42")
        Dataframe.place(x=0,y=0,width=1111,height=528)
        self.db=DatabaseDetails()
        #____________________________variables___________________

        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
             #++++++++++++++++++++
        self.var_cust_name=StringVar()
        self.var_mother_name=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_Address=StringVar()
        

        #_____________________lables___________________

        L1title=Button(Dataframe,text="Customer Details",bg="#091E42",fg="#fff",font=("Arial bold",15))
        L1title.place(x=120,y=6,width=815,height=30)

        label_frame_left=LabelFrame(Dataframe,text="Customber Details",font=("Arial bold",10),relief=RIDGE,bg="#091E42",fg="white")
        label_frame_left.place(x=5,y=51,width=415,height=467)

        l1=Label(Dataframe,text="Customer Ref",font=("Arial bold",12),bg="#091E42",fg="white")
        l1.place(x=15,y=80)
        l2=Label(Dataframe,text="Customer Name",font=("Arial bold",12),bg="#091E42",fg="white")
        l2.place(x=15,y=115)
        l3=Label(Dataframe,text="Mother Name",font=("Arial bold",12),bg="#091E42",fg="white")
        l3.place(x=15,y=150)
        l4=Label(Dataframe,text="Gender",font=("Arial bold",12),bg="#091E42",fg="white")
        l4.place(x=15,y=185)
        l5=Label(Dataframe,text="Post Code",font=("Arial bold",12),bg="#091E42",fg="white")
        l5.place(x=15,y=220)
        l6=Label(Dataframe,text="Mobile No.",font=("Arial bold",12),bg="#091E42",fg="white")
        l6.place(x=15,y=255)
        l7=Label(Dataframe,text="Email",font=("Arial bold",12),bg="#091E42",fg="white")
        l7.place(x=15,y=290)
        l8=Label(Dataframe,text="Nationality",font=("Arial bold",12),bg="#091E42",fg="white")
        l8.place(x=15,y=325)
        l9=Label(Dataframe,text="Id proof",font=("Arial bold",12),bg="#091E42",fg="white")
        l9.place(x=15,y=360)
        l10=Label(Dataframe,text="Id Number",font=("Arial bold",12),bg="#091E42",fg="white")
        l10.place(x=15,y=395)
        l11=Label(Dataframe,text="Address",font=("Arial bold",12),bg="#091E42",fg="white")
        l11.place(x=15,y=430)

        #Enteris_____________________________________________________

        Ref=Entry(Dataframe,textvariable=self.var_ref,font=("Arial bold",10),bg="white",state="readonly")
        Ref.place(x=180,y=80,width=215)
        
        Name=Entry(Dataframe,textvariable=self.var_cust_name,font=("Arial bold",10),bg="white",)
        Name.place(x=180,y=115,width=215)
        
        Mother=Entry(Dataframe,textvariable=self.var_mother_name,font=("Arial bold",10),bg="white")
        Mother.place(x=180,y=150,width=215)
        
        Gender=Entry(Dataframe,font=("Arial bold",10),bg="white")
        Gender.place(x=180,y=185,width=215)
        Gender_c=ttk.Combobox(Dataframe,textvariable=self.var_gender,font=("Arial bold",10),state="readonly")
        Gender_c["values"]=("","male","Female","other")
        Gender_c.current(0)
        Gender_c.place(x=180,y=185,width=215)
        
        Post=Entry(Dataframe,textvariable=self.var_post,font=("Arial bold",10),bg="white")
        Post.place(x=180,y=220,width=215)
        
        Mobile=Entry(Dataframe,textvariable=self.var_mobile,font=("Arial bold",10),bg="white")
        Mobile.place(x=180,y=255,width=215)
        
        Email=Entry(Dataframe,textvariable=self.var_email,font=("Arial bold",10),bg="white")
        Email.place(x=180,y=290,width=215)
        
        Nationality=Entry(Dataframe,font=("Arial bold",10),bg="white")
        Nationality.place(x=180,y=325,width=215)
        Nationality_c=ttk.Combobox(Dataframe,textvariable=self.var_nationality,font=("Arial bold",10),state="readonly")
        Nationality_c["values"]=("","Afganisthan","Bangladesh","Bhutan","China","India","Myamar","Nepal","Pakisthan","Sri lanka","other")
        Nationality_c.current(0)
        Nationality_c.place(x=180,y=325,width=215)

        
        proof=Entry(Dataframe,font=("Arial bold",10),bg="white")
        proof.place(x=180,y=360,width=215)
        proof_c=ttk.Combobox(Dataframe,textvariable=self.var_id_proof,font=("Arial bold",10),state="readonly")
        proof_c["values"]=("","Aadhar Card","Pan card","Voter id","Debit card","Driving licence","other")
        proof_c.current(0)
        proof_c.place(x=180,y=360,width=215)
        
        
        
        Id=Entry(Dataframe,textvariable=self.var_id_number,font=("Arial bold",10),bg="white")
        Id.place(x=180,y=395,width=215)
        
        Address=Entry(Dataframe,textvariable=self.var_Address,font=("Arial bold",10),bg="white")
        Address.place(x=180,y=430,width=215)

        #_______________________________4 Button________________________

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

        #________________________________Table_______________________________________

        Tableframe=LabelFrame(Dataframe,text="View Details & Search system",font=("Arial bold",10),relief=RIDGE,bg="#091E42",fg="white")
        Tableframe.place(x=425,y=51,width=681,height=467)

        Searchb=Button(Tableframe,text="Search",font=("Arial Bold",10),bg="#091E42",fg="white",command=self.search)
        Searchb.place(x=20,y=20,width=100,height=26)

        self.search_var=StringVar()

        Search_c=ttk.Combobox(Tableframe,textvariable=self.search_var,font=("Arial bold",10),state="readonly")
        Search_c["values"]=("","ref ","name","mobile ","Email ")
        Search_c.current(0)
        Search_c.place(x=135,y=20,width=140,height=25)

        self.txt_var=StringVar()

        Id=Entry(Tableframe,textvariable=self.txt_var,font=("Arial bold",10),bg="white")
        Id.place(x=293,y=20,width=140,height=25)

        Showb=Button(Tableframe,text="Show all",font=("Arial Bold",10),bg="#091E42",fg="white",command=self.fetch_data)
        Showb.place(x=450,y=20,width=100,height=26)



        #___________________Dtail_______________________________________________


        Dframe=LabelFrame(Dataframe,text="",font=("Arial bold",10),relief=RIDGE,bg="#091E42",fg="white")
        Dframe.place(x=431,y=122,width=670,height=390)

        scroll_x=ttk.Scrollbar(Dframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Dframe,orient=VERTICAL)

        self.cust_Details_table=ttk.Treeview(Dframe,column=("ref","Name","Mother","gender","post","mobile",

                                                            "Email","Nationality","ID","number","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_Details_table.xview)
        scroll_y.config(command=self.cust_Details_table.yview)

        self.cust_Details_table.heading("ref",text="Refer No")
        self.cust_Details_table.heading("Name",text="Name")
        self.cust_Details_table.heading("Mother",text="Mother Name")
        self.cust_Details_table.heading("gender",text="Gender")
        self.cust_Details_table.heading("post",text="Postcode")
        self.cust_Details_table.heading("mobile",text="Mobile")

        self.cust_Details_table.heading("Email",text="Email")
        self.cust_Details_table.heading("Nationality",text="Nationality")
        self.cust_Details_table.heading("ID",text="Id proof")
        self.cust_Details_table.heading("gender",text="Gender")
        self.cust_Details_table.heading("number",text="Id Number")
        self.cust_Details_table.heading("Address",text="Address")

        self.cust_Details_table.column("ref",width=60)
        self.cust_Details_table.column("Name",width=100)
        self.cust_Details_table.column("Mother",width=100)
        self.cust_Details_table.column("gender",width=60)
        self.cust_Details_table.column("post",width=60)
        self.cust_Details_table.column("mobile",width=75)
        self.cust_Details_table.column("Email",width=200)
        self.cust_Details_table.column("Nationality",width=90)
        self.cust_Details_table.column("ID",width=75)
        self.cust_Details_table.column("number",width=90)
        self.cust_Details_table.column("Address",width=300)




        
        self.cust_Details_table["show"]="headings"
        self.cust_Details_table.pack(fill=BOTH,expand=1)
        self.cust_Details_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()
        


    def add_button(self):
        if self.var_mobile.get()=="" or self.var_mother_name.get()=="" or self.var_id_number.get()=="":
            messagebox.showerror("Erroe","all fild are required,\nso fill all blanks carefully",parent=self.root)
        else:
            try:
                connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
                mycur=connection.cursor()
                mycur.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),self.var_cust_name.get(),self.var_mother_name.get(),self.var_gender.get()
                                                                                               ,self.var_post.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get()
                                                                                               ,self.var_id_proof.get(),self.var_id_number.get(),self.var_Address.get()))
            
                
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("success","Customer has been added",parent=self.root)

            except Exception as es:
                messagebox.showwarning("warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
        mycur=connection.cursor()
        mycur.execute("select * from customer")
        fetch_data=mycur.fetchall()
        if fetch_data!=0:
            self.cust_Details_table.delete(*self.cust_Details_table.get_children())
            for i in fetch_data:
                self.cust_Details_table.insert("",END,values=i)
                connection.commit()
            connection.close()

    def get_cursor(self,event=""):
        cursor=self.cust_Details_table.focus()
        i_stor=self.cust_Details_table.item(cursor)
        row=i_stor["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother_name.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_Address.set(row[10])

    def Update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","please enter mobile number",parent=self.root)
        else:
            connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
            mycur=connection.cursor()
            mycur.execute("Update customer set Name=%s,Mother=%s,Gender=%s,Postcode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                                                                                                self.var_cust_name.get(),self.var_mother_name.get(),self.var_gender.get()
                                                                                               ,self.var_post.get(),self.var_mobile.get(),self.var_email.get(),self.var_nationality.get()
                                                                                               ,self.var_id_proof.get(),self.var_id_number.get(),self.var_Address.get(),self.var_ref.get()))
        connection.commit()
        self.fetch_data()
        connection.close()
        messagebox.showinfo("Cngratulations","Your data successfully update",parent=self.root)

    def Delete(self):
        Delete=messagebox.askyesno("Apna Hotel","Do you want delete this customer",parent=self.root)
        if Delete>0:
            connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
            mycur=connection.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            mycur.execute(query,value)
        else:
            if not Delete:
                return
        connection.commit()
        self.fetch_data()
        connection.close()
        messagebox.showinfo("Cngratulations","Your data Has been deleted",parent=self.root)

    def Reset(self):
        self.var_ref.set("")
        self.var_cust_name.set("")
        self.var_mother_name.set("")
        #self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        #self.var_nationality.set("")
        #self.var_id_proof.set("")
        self.var_id_number.set("")
        self.var_Address.set("")
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        if self.search_var.get()=="" or self.txt_var.get()=="":
            messagebox.showerror("Error","please select option frist",parent=self.root)
        else:
            
            try:
                connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
                mycur=connection.cursor()
                mycur.execute("SELECT * FROM customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_var.get())+"%'")
                row=mycur.fetchall()
                if len(row)!=0:
                    self.cust_Details_table.delete(*self.cust_Details_table.get_children())
                    for i in row:
                        self.cust_Details_table.insert("",END,values=i)
                    connection.commit()
        
                connection.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
            
if __name__== "__main__":
    root=Tk()
    obj=cust_win(root)
    root.mainloop()
    
