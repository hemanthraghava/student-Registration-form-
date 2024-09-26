from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

win=Tk()
win.title("Student Registration  form")
frame=Frame(win)

#  frame1

user_frame=LabelFrame(frame,text="User Information",font=('arial',11))
user_frame.grid(row=0,column=0,pady=10,padx=20)

#creating all labels in this frame1

firstname_label=Label(user_frame,text='First Name',font=('Arial',10))
firstname_label.grid(row=0,column=0)
lastname_label=Label(user_frame,text='Last Name',font=('arial',10))
lastname_label.grid(row=0,column=1)
titlelabel=Label(user_frame,text='Title',font=('arial',10))
titlelabel.grid(row=0,column=2)
agelabel=Label(user_frame,text='Age',font=('arial',10))
agelabel.grid(row=2,column=0)
nationalitylabel=Label(user_frame,text='Nationality',font=('arial',10))
nationalitylabel.grid(row=2,column=1)

#creating enteries into labels in frame1

firstnameentry=Entry(user_frame)
firstnameentry.grid(row=1,column=0)
lastnameentry=Entry(user_frame)
lastnameentry.grid(row=1,column=1)
titleentry=ttk.Combobox(user_frame,values=["","Mr.",'Ms.',"Dr."])
titleentry.grid(row=1,column=2)
age=Spinbox(user_frame, from_='10',to='150')
age.grid(row=3,column=0)
nationality=ttk.Combobox(user_frame,values=['India','America','China','Japan','Australia','Brasil','Africa','Antartica','Russia'])
nationality.grid(row=3,column=1)

# spacing all the widgets

for i in user_frame.winfo_children():
    i.grid_configure(padx=10,pady=5)

#frame 2

courseframe=LabelFrame(frame)
courseframe.grid(row=1,column=0,sticky='news',pady=10,padx=20)

# Labels in frame2

registration=Label(courseframe,text='# Registration Status',font=('arial',10))
registration.grid(row=0,column=0)
completedcourses=Label(courseframe,text='# completed courses ',font=('arial',10))
completedcourses.grid(row=0,column=1)
semesterlabel=Label(courseframe,text='# current Semester',font=('arial',10))
semesterlabel.grid(row=0,column=2)

# entrys for frame2
registred_var=StringVar(value='Not Registred')
registrationbutton=Checkbutton(courseframe, text='Currently registred',font=('arial',10),variable=registred_var,onvalue='Registred succesfully',offvalue='Not Registred')
registrationbutton.grid(row=1,column=0)
completedcoursesEntry=Spinbox(courseframe,from_=0,to=20)
completedcoursesEntry.grid(row=1,column=1)
semester=ttk.Combobox(courseframe,values=[1,2,3,4,5,6,7,8])
semester.grid(row=1,column=2)

# placing widgets perfectly in frame2

for i in courseframe.winfo_children():
    i.grid_configure(padx=10,pady=10)

# frame 3

termsframe=LabelFrame(frame,text="Terms and conditions",font=('arial',11))
termsframe.grid(row=2,column=0,sticky="news",pady=10,padx=20)
 
# widgets in frame3

accept_var=StringVar(value='Not accepted')
accept=Checkbutton(termsframe,text='I accept the accept the terms and conditions ',variable=accept_var,onvalue='Accepted',offvalue='Not Accepted')
accept.grid(row=0,column=0,pady=10)

# functionn

def operation():
    firstname=firstnameentry.get()
    lastname=lastnameentry.get()
    title=titleentry.get()
    agee=age.get()
    nationalityy=nationality.get()
    registration=registred_var.get()
    courses=completedcoursesEntry.get()
    semseters=semester.get()
    terms=accept_var.get()
    if terms=='Accepted':
        if firstname and lastname:
            if registration=='Registred succesfully':
                if title:
                    if nationalityy:
                        print(firstname,lastname,title,nationalityy,registration,terms)
                        messagebox.showinfo(title='Registration Success',message='THANK YOU')
                        conn = sqlite3.connect('ah.db')
                        c = conn.cursor()
                        createtable="""
                        CREATE TABLE IF NOT EXISTS Student_Form (FirstName TEXT,Lastname TEXT,Title TEXT,Age INTEGER,
                        Nationality TEXT,Registration_Status TEXT, Num_courses INTEGER, Num_semesters INTEGER)
                        """
                        c.execute(createtable)
                        
                        insertion='''
                        INSERT INTO Student_Form (FirstName,Lastname,Title,Age,
                        Nationality,Registration_Status, Num_courses, Num_semesters) VALUES (?,?,?,?,?,?,?,?)
                        '''
                        inserttuple=(firstname,lastname,title,agee,nationalityy,registration,courses,semseters)
                        c.execute(insertion,inserttuple)
                        conn.commit()
                        conn.close()

                    else:
                       messagebox.showwarning(title='Registration failed ',message=' Nationality is required')
                else:
                    messagebox.showwarning(title='Registration failed',message='Title is required')
            else:
                 messagebox.showwarning(title='Registration failed',message='Registration status is required')
        else:
            messagebox.showwarning(title='Registration failed',message='first name and last name both are required')
    else:
        messagebox.showwarning(title='Registration failed',message='you have to accept the terms and conditions')

# Button

button=Button(frame,text='Enter',font=('arial',11),command=operation)
button.grid(row=3,column=0,sticky="news",pady=10,padx=20)

frame.pack()

win.mainloop()