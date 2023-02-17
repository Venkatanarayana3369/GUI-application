from tkinter import *
from tkinter import Tk
from tkinter import ttk
import pymysql

class studentsdata:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1500x800')
        title1=Label(self.root,text='Welcome To NTH Students Data',
                     font=('Rockwell Extra Bold',40),bg='teal',fg='white',bd=5,relief=RAISED)
        title1.pack(fill='x')
        self.rollnoVar=StringVar()
        self.fnameVar=StringVar()
        self.lnameVar=StringVar()
        self.courseVar=StringVar()
        self.contactVar=StringVar()
        self.emailVar=StringVar()
        self.locationVar=StringVar()
        self.instituteVar=StringVar()
#creating frames
        dataentryframe=Frame(self.root,bg='teal')
        dataentryframe.place(x=10,y=80,width=600,height=900)
        datadisplayframe=Frame(self.root,bg='teal')
        datadisplayframe.place(x=620,y=80,width=1290,height=900)
        #working with dataentry frame
        title2=Label(dataentryframe,text='studentsdataentry',font=('Rockwell',20),
                                                                   bg='black',fg='white',bd=3,relief=RAISED)
        title2.grid(row=0,columnspan=2,padx=120,pady=20)

        #roll no
        rollnoL=Label(dataentryframe,text='Roll NO:',font=('rockwell',20),
                                                                   bg='teal',fg='black')
        rollnoL.grid(row=1,column=0,sticky='W',padx=10)
        

        rollnoE=Entry(dataentryframe,textvariable=self.rollnoVar,font=('castellar',15))                                                               
        rollnoE.grid(row=1,column=1,sticky='E')
        #first name
        firstE=Label(dataentryframe,text='First Name:',font=('rockwell',20),bg='teal',fg='black')
        firstE.grid(row=2,column=0,sticky='W',padx=10)
        
        firstE=Entry(dataentryframe,textvariable=self.fnameVar,font=('castellar',15))                                                               
        firstE  .grid(row=2,column=1,sticky='E')
        #last name
        lastE=Label(dataentryframe,text='Last Name:',font=('rockwell',20),bg='teal',fg='black')
        lastE.grid(row=3,column=0,sticky='W',padx=10)
        
        lastE=Entry(dataentryframe,textvariable=self.lnameVar,font=('castellar',15))                                                               
        lastE.grid(row=3,column=1,sticky='E')
        #course
        courseL=Label(dataentryframe,text='Course Name:',font=('rockwell',20),bg='teal',fg='black')
        courseL.grid(row=4,column=0,sticky='W',padx=10)
        
        courseE=Entry(dataentryframe,textvariable=self.courseVar,font=('castellar',15))                                                               
        courseE.grid(row=4,column=1,sticky='E')
        #email id
        emailL=Label(dataentryframe,text='Email ID:',font=('rockwell',20),bg='teal',fg='black')
        emailL.grid(row=5,column=0,sticky='W',padx=10)
        
        emailE=Entry(dataentryframe,textvariable=self.emailVar,font=('castellar',15))                                                               
        emailE.grid(row=5,column=1,sticky='E')
        #contact
        contactL=Label(dataentryframe,text='Contact:',font=('rockwell',20),bg='teal',fg='black')
        contactL.grid(row=6,column=0,sticky='W',padx=10)
        
        contactE=Entry(dataentryframe,textvariable=self.contactVar,font=('castellar',15))                                                               
        contactE.grid(row=6,column=1,sticky='E')
        #location
        locationL=Label(dataentryframe,text='Location:',font=('rockwell',20),bg='teal',fg='black')
        locationL.grid(row=7,column=0,sticky='W',padx=10)
        
        locationE=Entry(dataentryframe,textvariable=self.locationVar,font=('castellar',15))                                                               
        locationE.grid(row=7,column=1,sticky='E')
        #institute
        instituteL=Label(dataentryframe,text='Institute:',font=('rockwell',20),bg='teal',fg='black')
        instituteL.grid(row=8,column=0,sticky='W',padx=10)
        
        instituteE=Entry(dataentryframe,textvariable=self.instituteVar,font=('castellar',15))                                                               
        instituteE.grid(row=8,column=1,sticky='E')
        #creating button frame
        buttonframe=Frame(dataentryframe,bg='teal',bd=3,relief=RAISED)
        buttonframe.place(x=10,y=520,width=550,height=130)
        #creating  buttons
        add=Button(buttonframe,text='Add',command=self.addingdata,font=('rockwell',20),bg='lavender',fg='red',bd=5,relief=RAISED)
        add.grid(row=0,column=0,padx=10,pady=20)

        update=Button(buttonframe,text='Update',command=self.updatingdata,font=('rockwell',20),bg='lavender',fg='red',bd=5,relief=RAISED)
        update.grid(row=0,column=1,padx=17,pady=20)

        delete=Button(buttonframe,text='Delete',command=self.deletingdata,font=('rockwell',20),bg='lavender',fg='red',bd=5,relief=RAISED)
        delete.grid(row=0,column=2,padx=17,pady=20)

        clear=Button(buttonframe,text='Clear',command=self.clearingdata,font=('rockwell',20),bg='lavender',fg='red',bd=5,relief=RAISED)
        clear.grid(row=0,column=3,padx=17,pady=20)
        #working with data display frame
        title3=Label(datadisplayframe,text='student data display',font=('Rockwell',20),
                                                                   bg='black',fg='white',bd=3,relief=RAISED)
        title3.place(x=500,y=20)


        tblframe=Frame(datadisplayframe,bg='teal',bd=5,relief=RAISED)
        tblframe.place(x=10,y=80,width=1230,height=800)


        self.studentinfo=ttk.Treeview(tblframe,columns=('rollno','fname','lname','course','contact','email','location','institute'))
        self.studentinfo.heading('rollno',text='Roll NO')
        self.studentinfo.heading('fname',text='First Name')
        self.studentinfo.heading('lname',text='Last Name')
        self.studentinfo.heading('course',text='Course')
        self.studentinfo.heading('contact',text='Contact')
        self.studentinfo.heading('email',text='Email ID')
        self.studentinfo.heading('location',text='Location')
        self.studentinfo.heading('institute',text='Institute')

        
        self.studentinfo.column('rollno',width=150,anchor='center')
        self.studentinfo.column('fname',width=150,anchor='center')
        self.studentinfo.column('lname',width=150,anchor='center')
        self.studentinfo.column('course',width=150,anchor='center')
        self.studentinfo.column('contact',width=150,anchor='center')
        self.studentinfo.column('email',width=150,anchor='center')
        self.studentinfo.column('location',width=150,anchor='center')
        self.studentinfo.column('institute',width=150,anchor='center')


        self.studentinfo['show']='headings'
        self.fetchingdata()
        
        self.studentinfo.pack()
        self.studentinfo.bind('<ButtonRelease-1>',self.cursor_row)
    
    def addingdata(self):
        connection=pymysql.connect(host='localhost',user='root',password='abab1212',db='studentdb')
        c=connection.cursor()
        c.execute('insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s)',
                  (
                       self.rollnoVar.get(),
                       self.fnameVar.get(),
                       self.lnameVar.get(),
                       self.courseVar.get(),
                       self.contactVar.get(),
                       self.emailVar.get(),
                       self.locationVar.get(),
                       self.instituteVar.get()
                       ))
        connection.commit()
        self.fetchingdata()
        self.clearingdata()
        connection.close()
    def clearingdata(self):
        self.rollnoVar.set('')
        self.fnameVar.set('')
        self.lnameVar.set('')
        self.courseVar.set('')
        self.contactVar.set('')
        self.emailVar.set('')
        self.locationVar.set('')
        self.instituteVar.set('')
    def fetchingdata(self):
        connection=pymysql.connect(host='localhost',user='root',password='abab1212',db='studentdb')
        c=connection.cursor()
        c.execute('select* from studentdata')
        data=c.fetchall()
        self.studentinfo.delete(*self.studentinfo.get_children())
        for i in data:
            self.studentinfo.insert('',END,value=i)
        connection.commit()
        connection.close()

    def cursor_row(self,a):
        cursor_row=self.studentinfo.focus()
        content=self.studentinfo.item(cursor_row)
        row=content['values']
        self.rollnoVar.set(row[0])
        self.fnameVar.set(row[1])
        self.lnameVar.set(row[2])
        self.courseVar.set(row[3])
        self.contactVar.set(row[4])
        self.emailVar.set(row[5])
        self.locationVar.set(row[6])
        self.instituteVar.set(row[7])
    def updatingdata(self):
        connection=pymysql.connect(host='localhost',user='root',password='abab1212',db='studentdb')
        c=connection.cursor()
        c.execute('update studentdata set fname=%s,lname=%s,course=%s,contact=%s,email=%s,location=%s,institute=%s where rollno=%s',
                   (
                    self.fnameVar.get(),
                    self.lnameVar.get(),
                    self.courseVar.get(),
                    self.contactVar.get(),
                    self.emailVar.get(),
                    self.locationVar.get(),
                    self.instituteVar.get(),
                    self.rollnoVar.get()
                       ))
        connection.commit()
        self.fetchingdata()
        self.clearingdata()
        connection.close()

    def deletingdata(self):
        connection=pymysql.connect(host='localhost',user='root',password='abab1212',db='studentdb')
        c=connection.cursor()
        c.execute('delete from studentdata where rollno=%s',self.rollnoVar.get()) 
        connection.commit()
        self.fetchingdata()
        self.clearingdata()
        connection.close()
        
        
root=Tk()        
s=studentsdata(root)

