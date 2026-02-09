from tkinter import *
from tkinter import ttk
import mysql.connector
import random

from tkinter import messagebox
from database_details import DatabaseDetails


class details_win:
    def __init__(self,root):
        self.root=root
        self.root.title("APNA HOTEL")
        self.root.geometry("1111x528+243+160")
        Dataframe=Frame(self.root,relief=RIDGE,bg="#091E42")
        Dataframe.place(x=0,y=0,width=1111,height=528)
        self.db=DatabaseDetails()
        #==============================variable+++++++++++++++++++++++++++++++++++++++++
        self.floor=StringVar()
        self.room=StringVar()
        self.roomtype=StringVar()

        L1title=Button(Dataframe,text="Customer Details",bg="#091E42",fg="#fff",font=("Arial bold",15))
        L1title.place(x=120,y=6,width=815,height=30)

        label_frame_left=LabelFrame(Dataframe,text="adding new room",font=("Arial bold",10),relief=RIDGE,bg="#091E42",fg="white")
        label_frame_left.place(x=5,y=36,width=535,height=300)
        frame_mid=Frame(label_frame_left,relief=RIDGE,bg="#091E42",bd=2)
        frame_mid.place(x=63,y=60,width=400,height=150)

        l1=Label(label_frame_left,text="Floor Number",font=("Arial bold",12),bg="#091E42",fg="white")
        l1.place(x=125,y=77)
        l2=Label(label_frame_left,text="Room  Number",font=("Arial bold",12),bg="#091E42",fg="white")
        l2.place(x=125,y=112)
        l3=Label(label_frame_left,text="Select Room",font=("Arial bold",12),bg="#091E42",fg="white")
        l3.place(x=125,y=147)

        Floor=Entry(label_frame_left,textvariable=self.floor,font=("Arial bold",10),bg="white",)
        Floor.place(x=250,y=78,width=130)
        
        Room=Entry(label_frame_left,textvariable=self.room,font=("Arial bold",10),bg="white")
        Room.place(x=250,y=113,width=130)
        
        select=Entry(label_frame_left,font=("Arial bold",10),bg="white")
        select.place(x=250,y=148,width=130)
        select_c=ttk.Combobox(label_frame_left,textvariable=self.roomtype,font=("Arial bold",10),state="readonly")
        select_c["values"]=("","single","double","laxury")
        select_c.current(0)
        select_c.place(x=250,y=148,width=130)

        #++++++++++++++++++++++++buttons++++++++++++++++++++++++++++++++++

        Addb=Button(label_frame_left,text="Add",font=("Arial Bold",10),bg="#091E42",fg="white",command=self.add_button)
        Addb.place(x=70,y=195,width=85,height=30)

        Updb=Button(label_frame_left,text="Update",font=("Arial Bold",10),bg="#091E42",fg="white",command=self.Update)
        Updb.place(x=170,y=195,width=85,height=30)

        Delb=Button(label_frame_left,text="Delete",font=("Arial Bold",10),bg="#091E42",fg="white",command=self.Delete)
        Delb.place(x=270,y=195,width=85,height=30)

        Resb=Button(label_frame_left,text="Reset",font=("Arial Bold",10),bg="#091E42",fg="white",command=self.Reset)
        Resb.place(x=370,y=195,width=85,height=30)

        #=======================table frame==============
        Table_frame_right=LabelFrame(Dataframe,text="room details",font=("Arial bold",10),relief=RIDGE,bg="#091E42",fg="white")
        Table_frame_right.place(x=530,y=36,width=535,height=300)

        scroll_x=ttk.Scrollbar(Table_frame_right,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame_right,orient=VERTICAL)

        self.rooms_Details_table=ttk.Treeview(Table_frame_right,column=("Floor","Roomnum","type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)



        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.rooms_Details_table.xview)
        scroll_y.config(command=self.rooms_Details_table.yview)

        self.rooms_Details_table.heading("Floor",text="Floor")
        self.rooms_Details_table.heading("Roomnum",text="Room Number")
        self.rooms_Details_table.heading("type",text="Room type")
        
        self.rooms_Details_table["show"]="headings"
        
        self.rooms_Details_table.column("Floor",width=60)
        self.rooms_Details_table.column("Roomnum",width=100)
        self.rooms_Details_table.column("type",width=100)
        

        self.rooms_Details_table["show"]="headings"
        self.rooms_Details_table.pack(fill=BOTH,expand=1)
        self.rooms_Details_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    def fetch_data(self):
        connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
        mycur=connection.cursor()
        mycur.execute("select * from room_data")
        fetch_data=mycur.fetchall()
        if fetch_data!=0:
            self.rooms_Details_table.delete(*self.rooms_Details_table.get_children())
            for i in fetch_data:
                self.rooms_Details_table.insert("",END,values=i)
                connection.commit()
            connection.close()

    def get_cursor(self,event=""):
        cursor=self.rooms_Details_table.focus()
        i_stor=self.rooms_Details_table.item(cursor)
        row=i_stor["values"]

        self.floor.set(row[0])
        self.room.set(row[1])
        self.roomtype.set(row[2])
        


    def add_button(self):
        if self.floor.get()=="" or self.room.get()=="":
            messagebox.showerror("Erroe","all fild are required,\nso fill all blanks carefully",parent=self.root)
        else:
            try:
                connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
                mycur=connection.cursor()
                mycur.execute("insert into room_data values(%s,%s,%s)",(self.floor.get(),self.room.get(),self.roomtype.get()))
            
                
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("success","room has been added",parent=self.root)

            except Exception as es:
                messagebox.showwarning("warning",f"Something went wrong:{str(es)}",parent=self.root)

    def Update(self):
        if self.roomtype.get()=="":
            messagebox.showerror("Error","please select type of room",parent=self.root)
        else:
            connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
            mycur=connection.cursor()
            mycur.execute("Update room_data set Floor=%s,Roomno=%s,Roomtype=%s",(self.floor.get(),self.room.get(),self.roomtype.get()))
                                                                                                
                                                                                              
        connection.commit()
        self.fetch_data()
        connection.close()
        messagebox.showinfo("Cngratulations","Your data successfully update",parent=self.root)

    def Delete(self):
        Delete=messagebox.askyesno("Apna Hotel","Do you want delete this customer",parent=self.root)
        if Delete>0:
            connection=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
            mycur=connection.cursor()
            query="delete from room_data where Roomno=%s"
            value=(self.room.get(),)
            mycur.execute(query,value)
        else:
            if not Delete:
                return
        connection.commit()
        self.fetch_data()
        connection.close()
        messagebox.showinfo("Cngratulations","Your data Has been deleted",parent=self.root)

    def Reset(self):
        self.floor.set("")
        self.room.set("")
        self.roomtype.set("")
        



            
if __name__== "__main__":
    root=Tk()
    obj=details_win(root)
    root.mainloop()
