from tkinter import*
from tkinter import ttk # stylish entry field
from PIL import Image,ImageTk  
import mysql.connector
import pymysql
from tkinter import messagebox
 
class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management System")


# creating variables   -->  SQL
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designation=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_doj=StringVar()
        self.var_dob=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()
    
        
# LAbel for setting attribute of title 
        lbl_title=Label(self.root,text="WorkFlowHR",font=("times new roman",37,"bold"),fg='darkblue', bg='white' )
        lbl_title.place(x=0,y=0,width=1530,height=50)

        #adding logo
        img_logo=Image.open("images/demo_logo.png")
        # Resampling.Resampling.LANCZOS - create high quality picture       
        img_logo=img_logo.resize((60,60),Image.Resampling.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo) #saving it
        
        self.logo = Label(self.root, image=self.photo_logo)   # showing it 
        self.logo.place(x=560,y=0,width=50,height=50)   # placing it with c orrect hieght width x,y
    
        # IMAGE FRAME
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160) 
        # making frame for image
        # 1st
        img1=Image.open("images/emp_working.png")
        # Resampling.Resampling.Resampling.LANCZOS - create high quality picture       
        img1=img1.resize((540,160),Image.Resampling.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1) #saving it
        
        self.img_1 = Label(img_frame, image=self.photo1)   # showing it 
        self.img_1.place(x=0,y=0,width=540,height=160) 

        
        # 2nd
        img_2=Image.open("images/emp_talk.png")
        img_2=img_2.resize((540,160),Image.Resampling.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img_2) 
        
        self.img_2 = Label(img_frame, image=self.photo2)  
        self.img_2.place(x=540,y=0,width=540,height=160) 

          # 3
        img_3=Image.open("images/emp_working.png")
        img_3=img_3.resize((540,160),Image.Resampling.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img_3) 
        
        self.img_3 = Label(img_frame, image=self.photo3)  
        self.img_3.place(x=1000,y=0,width=540,height=160) 
         

    #   MAIN FRAME
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=220,width=1500,height=560) 
    # UPPER FRAME
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text="Information",font=("times new roman",11,"bold"),fg='red', bg='white')
        upper_frame.place(x=10,y=10,width=1480,height=270)
        #   using LABELFRAME --> TEXT in it. 




# Department
        lbl_dep=Label(upper_frame,text='Department:',font=('arial',11,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
        #    place used for non know placing of element
        # Grid--> wor,col, sticky--> stick to the frame 
    
       
 # COMBO_BOX  --> option in HTML
    # puttng var into comboBOX
    #     var --> Entry Fields  
    #         {used for fetching input value}
        combo_dept=ttk.Combobox(upper_frame,textvariable=self.var_dep,text='Departent',font=('arial',12,'bold'),width=17,state='readonly')
    #    Values for option
        combo_dept['value']=('Select Department','HR','Sales','Manager','Social-Media','Tech','Design') 
        combo_dept.current(0)
        combo_dept.grid(row=0,column=1,padx=2,pady=10,sticky=W)

    
 
# Name
        lbl_Name=Label(upper_frame,font=('arial',11,'bold'),text="Name:",bg='white')
        lbl_Name.grid(row=0,column=2,padx=4,pady=7 , sticky=W)
        
        txt_Designation=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
        txt_Designation.grid(row=0,column=3,sticky=W,padx=2,pady=7)

# DEsignation
        lbl_Designation=Label(upper_frame,font=('arial',11,'bold'),text="Designation:",bg='white')
        lbl_Designation.grid(row=1,column=0,padx=2,pady=7 , sticky=W)
        
        txt_Designation=ttk.Entry(upper_frame,textvariable=self.var_designation,width=22,font=('arial',11,'bold'))
        txt_Designation.grid(row=1,column=1,sticky=W,padx=2,pady=7)
# EMAIL
        lbl_Designation=Label(upper_frame,font=('arial',11,'bold'),text="Email",bg='white')
        lbl_Designation.grid(row=1,column=2,padx=4,pady=7 , sticky=W)
        
        txt_Designation=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=('arial',11,'bold'))
        txt_Designation.grid(row=1,column=3,sticky=W,padx=2,pady=7)
# ADDRESS
        lbl_Address=Label(upper_frame,font=('arial',11,'bold'),text="Address",bg='white')
        lbl_Address.grid(row=2,column=0,padx=2,pady=7 , sticky=W)
        
        txt_Address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold'))
        txt_Address.grid(row=2,column=1,sticky=W,padx=2,pady=7)

# DOJ
        lbl_DOJ=Label(upper_frame,font=('arial',11,'bold'),text="DOJ",bg='white')
        lbl_DOJ.grid(row=2,column=2,padx=4,pady=7 , sticky=W)
        
        txt_DOJ=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=('arial',11,'bold'))
        txt_DOJ.grid(row=2,column=3,sticky=W,padx=2,pady=7)

# DOB
        lbl_DOB=Label(upper_frame,font=('arial',11,'bold'),text="DOB",bg='white')
        lbl_DOB.grid(row=3,column=0,padx=2,pady=7 , sticky=W)
        
        txt_DOB=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=('arial',11,'bold'))
        txt_DOB.grid(row=3,column=1 ,sticky=W,padx=2,pady=7)


#  ID Proof
        
        combo_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,text="id_proof_type",font=('arial',12,'bold'),width=17,state='readonly')
    #    Values for option
        combo_proof['value']=('Select ID Proof','PAN','ADHAAR','DRIVING LICENSE','VOTER ID')
        combo_proof.current(0)
        combo_proof.grid(row=4,column=0,padx=2,pady=7,sticky=W)
        
        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=("arial",11,"bold"))
        txt_proof.grid(row=4,column=1,padx=2,pady=7)
# Gender
      
        lbl_gender=Label(upper_frame,font=('arial',11,'bold'),text="Gender:",bg='white')
        lbl_gender.grid(row=3,column=2,padx=4,pady=7 , sticky=W)
        
        combo_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('arial',12,'bold'),width=17,state='readonly')
        combo_gender['value']=('Female','Male')
        combo_gender.current(0)
        combo_gender.grid(row=3,column=3,padx=4,pady=7,sticky=W)
        
    
# Contact Number
        lbl_Contact_Number=Label(upper_frame,font=('arial',11,'bold'),text="Contact",bg='white')
        lbl_Contact_Number.grid(row=4,column=2,padx=4,pady=7,sticky=W)
        
        txt_Contact_Number=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=('arial',11,'bold'))
        txt_Contact_Number.grid(row=4,column=3,sticky=W,padx=4,pady=7)

# contry
        lbl_Country=Label(upper_frame,font=('arial',11,'bold'),text="Country",bg='white')
        lbl_Country.grid(row=1,column=4,padx=4,pady=7 , sticky=W)
        
        txt_Country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=('arial',11,'bold'))
        txt_Country.grid(row=1,column=5,sticky=W,padx=4,pady=7)

# CTC
        lbl_CTC=Label(upper_frame,font=('arial',11,'bold'),text="CTC",bg='white')
        lbl_CTC.grid(row=0,column=4,padx=4,pady=7 , sticky=W)
        
        txt_CTC=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=('arial',11,'bold'))
        txt_CTC.grid(row=0,column=5,sticky=W,padx=2,pady=7)

#  Main image

        img_main=Image.open("images/unity_teammate.png")
        img_main=img_main.resize((235,235),Image.Resampling.LANCZOS)
        self.photomain=ImageTk.PhotoImage(img_main) 
        
        self.img_main= Label(upper_frame, image=self.photomain)  
        self.img_main.place(x=960,y=0,width=235,height=235) 

#  Button-Frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1250,y=20,width=140,height=170)

# making button inseide main button
        btn_add=Button(button_frame,text="Save",command=self.add_data,font=('arial',11,'bold'),width=12,bg='blue', fg='white')
        btn_add.grid(row=0,column=0,padx=7,pady=5)

        btn_update=Button(button_frame,text="Update",command=self.update_data,font=('arial',11,'bold'),width=12,bg='blue', fg='white')
        btn_update.grid(row=1,column=0,padx=7,pady=5)

        btn_delete=Button(button_frame,text="Delete",command=self.delete_data,font=('arial',11,'bold'),width=12,bg='blue', fg='white')
        btn_delete.grid(row=2,column=0,padx=7,pady=5)
        
        btn_clear=Button(button_frame,text="Clear",command=self.clear,font=('arial',11,'bold'),width=12,bg='blue', fg='white')
        btn_clear.grid(row=3,column=0,padx=7,pady=5)


        
# LOWER FRAME
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text="Information table",font=("times new roman",11,"bold"),fg='red', bg='white')
        down_frame.place(x=10,y=280,width=1480,height=270)
 
# SEARCH FRAME

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text="Search Employee Information",font=("times new roman",11,"bold"),fg='red', bg='white')
        search_frame.place(x=10,y=0,width=1456,height=65)
        
        self.var_search_com=StringVar()

        lbl_search=Label(search_frame,font=('arial',11,'bold'),text="Search By",fg='white',bg='red')
        lbl_search.grid(row=0,column=0,padx=20,pady=6,sticky=W)
        
        combo_search=ttk.Combobox(search_frame,textvariable=self.var_search_com,font=('arial',12,'bold'),width=17,state='readonly')
        combo_search['value']=('select one option','Contact','id_proof','Name','Email')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=15,pady=6,sticky=W)
        
        self.var_search=StringVar() 

        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=20,font=('arial',11,'bold'))
        txt_search.grid(row=0,column=2,padx=15,pady=6)

        btn_search=Button(search_frame,command=self.search_data,text="Search",font=('arial',11,'bold'),width=17,bg='blue', fg='white')
        btn_search.grid(row=0,column=3,padx=15,pady=2)

        btn_showall=Button(search_frame,command=self.fetch_data,text="Show All",font=('arial',11,'bold'),width=17,bg='blue', fg='white')
        btn_showall.grid(row=0,column=4,padx=15,pady=2)
    
        lbl_quote=Label(search_frame,font=('times new roman',15,'bold'),text="Efforts could be controlled, Outcomes could'nt",bg='white',fg='firebrick3')
        lbl_quote.grid(row=0,column=5,padx=50,pady=6,sticky=W)
                  

#      ****************** Employee Table  *****************
#        Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=11,y=70,width=1454,height=170)

# Scroll Bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.employee_table=ttk.Treeview(table_frame,column=('dep','name','desg','email','address','dob','doj','idproofcomb','idproof','gender','phone','country','salary',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

# using scroll bar
 
        self.employee_table.heading("dep",text="Department")
        self.employee_table.heading("name",text="Name")
        self.employee_table.heading("desg",text="Designation")
        self.employee_table.heading("email",text="Email")
        self.employee_table.heading("address",text="Address")
        self.employee_table.heading("dob",text="DOB")
        self.employee_table.heading("doj",text="DOJ")    
        self.employee_table.heading("idproofcomb",text="ID Type")
        self.employee_table.heading("idproof",text="ID Proof")
        self.employee_table.heading("gender",text="Gender")
        self.employee_table.heading("phone",text="Phone")
        self.employee_table.heading("country",text="Country")
        self.employee_table.heading("salary",text="Salary")


# removing extra space btw colmns
        self.employee_table['show']='headings' 

        self.employee_table.column("dep",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("desg",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("idproofcomb",width=100)
        self.employee_table.column("idproof",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("country",width=100)
        self.employee_table.column("salary",width=100)
       
# .packing all attributes
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)    # showing saved data into entry fields 
        self.fetch_data()
        

# ******************** Functions****************
    def  add_data(self):
        if self.var_designation.get()=="" or  self.var_idproof.get()=="":
              messagebox.showerror('Error','All fields are required')
        else:
        #        exception handling 
                try:        
                #      connectn with DB
                   conn=mysql.connector.connect(host='localhost',username='root',password='sameer&9990',database='mydata')
                # cursor  Inserting --> data --> into DB
                   my_cursor=conn.cursor()
                # QUERY for INSERTING
                   my_cursor.execute('insert into employee1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                        self.var_dep.get(),
                                                        self.var_name.get(),
                                                        self.var_designation.get(),
                                                        self.var_email.get(),
                                                        self.var_address.get(),
                                                        self.var_doj.get(),
                                                        self.var_dob.get(),
                                                        self.var_idproofcomb.get(),
                                                        self.var_idproof.get(),
                                                        self.var_gender.get(),
                                                        self.var_phone.get(),
                                                        self.var_country.get(),
                                                        self.var_salary.get()
                                                        ))

                 
                   conn.commit()
                   self.fetch_data()  # showing REAL-TIME-DATA into entry fields    
                   conn.close()
                   messagebox.showinfo( 'Success','Employee data had been added',parent=self.root)                    
                except Exception as es:
                   messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)                      
                   
        # Fetching data below search box 
    def fetch_data(self):
            conn=mysql.connector.connect(host='localhost',username='root',password='sameer&9990',database='mydata')
            my_cursor=conn.cursor()
            my_cursor.execute('select * from employee1')
            data=my_cursor.fetchall()
            if len(data)!=0:
                  self.employee_table.delete(*self.employee_table.get_children())
                  for i in data:
                        self.employee_table.insert("",END,values=i)
                  conn.commit()
            conn.close()

#      showing data saved into --> ENTRY FIELDS
    def get_cursor(self,event=""):
          cursor_row=self.employee_table.focus()
          content=self.employee_table.item(cursor_row)
          data=content['values']

          self.var_dep.set(data[0])          
          self.var_name.set(data[1])
          self.var_designation.set(data[2])
          self.var_email.set(data[3])
          self.var_address.set(data[4])
          self.var_dob.set(data[5])
          self.var_doj.set(data[6])
          self.var_idproofcomb.set(data[7])
          self.var_idproof.set(data[8])
          self.var_gender.set(data[9])
          self.var_phone.set(data[10])
          self.var_country.set(data[11])
          self.var_salary.set(data[12])



    
                   #  ******************* function of UPDATE <BUTTON> *********************
    def update_data(self):   
        if not self.var_designation.get() or  not self.var_idproof.get():
              messagebox.showerror('Error','All fields are required')
        else:
                try:       
                   update=messagebox.askyesno('Update','Are you sure ?')
                   if update>0:        #     YES for updation 
                        conn=mysql.connector.connect(host='localhost',username='root',password='sameer&9990',database='mydata')
                        my_cursor=conn.cursor()
                        my_cursor.execute('update employee1 set Department=%s, Name=%s,Designation=%s,Email=%s,Address=%s,DOB=%s,DOJ=%s,id_proof_type=%s,Gender=%s,Contact=%s,Country=%s,CTC=%s where id_proof=%s',(
                                                        self.var_dep.get(),
                                                        self.var_name.get(),
                                                        self.var_designation.get(),
                                                        self.var_email.get(),
                                                        self.var_address.get(),
                                                        self.var_doj.get(),
                                                        self.var_dob.get(),
                                                        self.var_idproofcomb.get(),
                                                        self.var_gender.get(),
                                                        self.var_phone.get(),
                                                        self.var_country.get(),
                                                        self.var_salary.get(),
                                                        self.var_idproof.get()
                                                   ))
                   else:
                         if not update:
                               return 
                   conn.commit()
                   self.fetch_data()
                   conn.close()   
                   messagebox.showinfo('Hurrah ','Updation Successfull', parent=self.root)
                except Exception as es:
                     messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
                
    def delete_data(self):
           if self.var_idproof.get()=="": 
                 messagebox.showerror('Error', "All fields are reqired")
           else:
                 try:
                       delete=messagebox.askyesno('Delete',"Are you sure deleting employee's data")
                       if delete>0:
                               conn=mysql.connector.connect(host='localhost',username='root',password='sameer&9990',database='mydata')
                               my_cursor=conn.cursor()
                               sql='delete from employee1 where id_proof=%s'
                               value=(self.var_idproof.get(),)
                               my_cursor.execute(sql,value)
                       else:
                             if not delete:
                                   return 
                       conn.commit()
                       self.fetch_data()
                       conn.close()
                       messagebox.showinfo('Delete',"Employee's Data succesfully deleted")       
                 except Exception as es:      
                       messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
#       ***************** reseting details    ******************


    def clear(self):   
          self.var_dep.set("")          
          self.var_name.set("")
          self.var_designation.set("")
          self.var_email.set("")
          self.var_address.set("")
          self.var_dob.set("")
          self.var_doj.set("")
          self.var_idproofcomb.set("Select ID_Proof")
          self.var_idproof.set("")
          self.var_gender.set("")
          self.var_phone.set("")
          self.var_country.set("")
          self.var_salary.set("")
    def search_data(self):
     if self.var_search.get() == "" or self.var_search_com.get()=="":
        messagebox.showerror('Error', 'Please select option')
     else:
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='sameer&9990', database='mydata')
            my_cursor = conn.cursor()
            my_cursor.execute('SELECT * FROM employee1 WHERE ' + str(self.var_search_com.get())+" LIKE '%"+str(self.var_search.get())+"%'")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.employee_table.delete(*self.employee_table.get_children())
                for i in rows:
                    self.employee_table.insert("", END, value=i)
            conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror('Error', f'Due to: {str(es)}', parent=self.root)

if __name__=="__main__":
          root=Tk()
          obj=Employee(root)
          root.mainloop()  


