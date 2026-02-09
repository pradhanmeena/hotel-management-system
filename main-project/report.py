from tkinter import *
class Report:
    def __init__(self,root):
        self.root=root
        
        
        self.root.geometry("1366x783")
        self.root.configure(background="#091E42")
        frame=Frame(self.root,bg="#091E42",relief=RIDGE,bd=1)
        frame.place(x=200,y=120,width=900,height=500)

        frame=Frame(self.root,bg="#091E42",relief=RIDGE,bd=1)
        frame.place(x=185,y=113,width=60,height=60)
        frame=Frame(self.root,bg="#091E42",relief=RIDGE,bd=1)
        frame.place(x=1085,y=113,width=60,height=60)

        frame=Frame(self.root,bg="#091E42",relief=RIDGE,bd=1)
        frame.place(x=185,y=600,width=60,height=60)
        frame=Frame(self.root,bg="#091E42",relief=RIDGE,bd=1)
        frame.place(x=1085,y=600,width=60,height=60)

        #frame2
        frame2=Frame(self.root,bg="#091E42",relief=RIDGE,bd=1)
        frame2.place(x=225,y=146,width=850,height=450)

        frame=Frame(self.root,bg="#091E42",relief=RIDGE,bd=1)
        frame.place(x=185,y=113,width=30,height=30)
        frame=Frame(self.root,bg="#091E42",relief=RIDGE,bd=1)
        frame.place(x=1085,y=113,width=30,height=30)

        frame=Frame(self.root,bg="#091E42",relief=RIDGE,bd=1)
        frame.place(x=185,y=600,width=30,height=30)
        frame=Frame(self.root,bg="#091E42",relief=RIDGE,bd=1)
        frame.place(x=1085,y=600,width=30,height=30)

        #labes
        label=Label(frame2,text="Devloper Details",font=("Arial bold",17,"bold"),bg="#091E42",fg="#fff")
        label.place(x=270,y=20,width=330,height=30)

        label=Label(frame2,text="Qualification of devloper :-",font=("Arial bold",10,"bold"),bg="#091E42",fg="#fff")
        label.place(x=150,y=120)

        label=Label(frame2,text="Name of The Project :-",font=("Arial bold",10,"bold"),bg="#091E42",fg="#fff")
        label.place(x=150,y=150)

        label=Label(frame2,text="Technologies Used :-",font=("Arial bold",10,"bold"),bg="#091E42",fg="#fff")
        label.place(x=150,y=180)

        label=Label(frame2,text="Project Category:-",font=("Arial bold",10,"bold"),bg="#091E42",fg="#fff")
        label.place(x=150,y=210)

        label=Label(frame2,text="Date of Deployement",font=("Arial bold",10,"bold"),bg="#091E42",fg="#fff")
        label.place(x=150,y=240)

        label=Label(frame2,text="Email contact :-",font=("Arial bold",10,"bold"),bg="#091E42",fg="#fff")
        label.place(x=150,y=270)

        label=Label(frame2,text="Address :-",font=("Arial bold",10,"bold"),bg="#091E42",fg="#fff")
        label.place(x=150,y=300)


        label=Label(frame2,text="Diploma in CSE",font=("Arial bold",10,"bold"),bg="#091E42",fg="#fff")
        label.place(x=450,y=120)

        label=Label(frame2,text="Hotel Menegment System",font=("Arial bold",10,"bold"),bg="#091E42",fg="#fff")
        label.place(x=450,y=150)

        label=Label(frame2,text="Python & MySQL",font=("Arial bold",10,"bold"),bg="#091E42",fg="#fff")
        label.place(x=450,y=180)

        label=Label(frame2,text="Desktop Software",font=("Arial bold",10,"bold"),bg="#091E42",fg="#fff")
        label.place(x=450,y=210)

        label=Label(frame2,text="22 January 2024 ",font=("Arial bold",10,"bold"),bg="#091E42",fg="#fff")
        label.place(x=450,y=240)

        label=Label(frame2,text="Pradhanmeena7778@gmail.com ",font=("Arial bold",10,"bold"),bg="#091E42",fg="#fff")
        label.place(x=450,y=270)

        label=Label(frame2,text="Nandgaon,Bundi Rajsthan(323024) ",font=("Arial bold",10,"bold"),bg="#091E42",fg="#fff")
        label.place(x=450,y=300)

if __name__== "__main__":

    root=Tk()
    ob=Report(root)
    root.mainloop()
    
