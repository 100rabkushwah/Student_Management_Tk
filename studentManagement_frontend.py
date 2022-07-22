"""
sms_tk_sqlite.py
Student managemenet system

"""
#Frontend

from tkinter import *
from tkinter import messagebox
import stdDatabase_backend

sd=""
class Student:
	def display_window(self,root):
		self.root=root
		self.root.title("Student DataBase Managemenet System")
		self.root.geometry('1350x700+0+0')
		self.root.config(bg='cadet blue')

		#==========variables==============
		StdID=StringVar()
		Firstname=StringVar()
		Surname=StringVar()
		Dob=StringVar()
		Age=StringVar()
		Gender=StringVar()
		Address=StringVar()
		Mobile=StringVar()
		#==========End variables==============


		#==========Function Call==============
		def iexit():
			iexit=messagebox.askyesno("Student DataBase Managemenet System","Confirm if you want to Exit ?")
			if iexit>0:
				root.destroy()
				return

		def clearData():
			messagebox.showinfo("Student DataBase Managemenet System","Clear")
			self.txtStdID.delete(0,END)
			self.txtFirstname.delete(0,END)
			self.txtSurname.delete(0,END)
			self.txtDob.delete(0,END)
			self.txtAge.delete(0,END)
			self.txtGender.delete(0,END)
			self.txtAddress.delete(0,END)
			self.txtMobile.delete(0,END)

		def addData():
			#sID=stdID.get()
			messagebox.showinfo("Student DataBase Managemenet System","Add data")
			messagebox.showinfo("Student DataBase Managemenet System",StdID.get()+Firstname.get()+Surname.get()+Dob.get()+ \
				Age.get()+Gender.get()+Address.get()+Mobile.get())
			if(len(StdID.get())!=0):
				stdDatabase_backend.addStdRecord(StdID.get(),Firstname.get(),Surname.get(),Dob.get(), Age.get(), Gender.get(), Address.get(),Mobile.get())
				studentlist.delete(0,END)
				studentlist.insert(END,StdID.get(),Firstname.get(),Surname.get(),Dob.get(), Age.get(), Gender.get(), Address.get(),Mobile.get())

		def DisplayData():
			messagebox.showinfo("Student DataBase Managemenet System","Display data")
			studentlist.delete(0,END)
			for row in stdDatabase_backend.viewData():
				#print(row)
				studentlist.insert(END,row,str(""))
		def StudnetRec(event):
			global sd
			searchStd=studentlist.curselection()[0]
			#print(searchStd)
			sd=studentlist.get(searchStd)
			self.txtStdID.delete(0,END)
			self.txtStdID.insert(END,sd[1])
			self.txtFirstname.delete(0,END)
			self.txtFirstname.insert(END,sd[2])
			self.txtSurname.delete(0,END)
			self.txtSurname.insert(END,sd[3])
			self.txtDob.delete(0,END)
			self.txtDob.insert(END,sd[4])
			self.txtAge.delete(0,END)
			self.txtAge.insert(END,sd[5])
			self.txtGender.delete(0,END)
			self.txtGender.insert(END,sd[6])
			self.txtAddress.delete(0,END)
			self.txtAddress.insert(END,sd[7])
			self.txtMobile.delete(0,END)
			self.txtMobile.insert(END,sd[8])

		def DeleteData():
			global sd
			messagebox.showinfo("Student DataBase Managemenet System","Delete data")
			if(len(StdID.get())!=0):
				stdDatabase_backend.deleteRec(sd[0])
				clearData()
				DisplayData()

		def searchDatabase():
			messagebox.showinfo("Student DataBase Managemenet System","Search data")
			studentlist.delete(0,END)
			for row in stdDatabase_backend.searchData(StdID.get(), Firstname.get(), Surname.get(),Dob.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()):
				studentlist.insert(END,row,str(""))

		def update():
			global sd
			messagebox.showinfo("Student DataBase Managemenet System","update data")
			if (len(StdID.get())!=0):
				stdDatabase_backend.deleteRec(sd[0])
			if(len(StdID.get())!=0):
				stdDatabase_backend.addStdRecord(StdID.get(), Firstname.get(), Surname.get(),Dob.get(),Age.get(), Gender.get(), Address.get(), Mobile.get())
				studentlist.delete(0,END)
				studentlist.insert(END,(StdID.get(), Firstname.get(), Surname.get(),Dob.get(),Age.get(), Gender.get(), Address.get(), Mobile.get()))



		#==========Frmes==============
		#==========Main Frame Frmes==============
		MainFrame=Frame(self.root,bg='cadet blue')
		MainFrame.grid()

		TitleFrame=Frame(MainFrame,bd=2,padx=54,pady=5,bg='Ghost White')
		TitleFrame.pack(side=TOP)

		self.lblTitle=Label(TitleFrame,font=('arial',47,'bold'),text='Student DataBase Managemenet System',bg='Ghost White')
		self.lblTitle.grid()

		ButtonFrame=Frame(MainFrame,bd=2,width=1350,height=70,padx=18,pady=10,bg='Ghost White',relief=RIDGE)
		ButtonFrame.pack(side=BOTTOM)

		DataFrame=Frame(MainFrame,bd=1,width=1300,height=400,padx=20,pady=20,relief=RIDGE,bg='cadet blue')
		DataFrame.pack(side=BOTTOM)

		DataFrameLEFT=LabelFrame(DataFrame,bd=1,width=1000,height=600,padx=20,pady=3,bg='Ghost White',
			font=('arial',20,'bold'),text="Student Info\n")
		DataFrameLEFT.pack(side=LEFT)

		DataFrameRIGHT=LabelFrame(DataFrame,bd=1,width=450,height=300,padx=31,pady=3,relief=RIDGE,bg='Ghost White',
			font=('arial',20,'bold'),text="Student Details\n")
		DataFrameRIGHT.pack(side=RIGHT)


		#==========Entry form=====DataFrameLEFT  =========
		#StdID
		self.lblStdID=Label(DataFrameLEFT,font=('arial',20,'bold'),text='Student ID ',padx=2,pady=2,bg='Ghost White')
		self.lblStdID.grid(row=0,column=0,sticky=W)
		self.txtStdID=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=StdID,width=39)
		self.txtStdID.grid(row=0,column=1)
		#Firstname
		self.lblFirstname=Label(DataFrameLEFT,font=('arial',20,'bold'),text='Firstname ',padx=2,pady=2,bg='Ghost White')
		self.lblFirstname.grid(row=1,column=0,sticky=W)
		self.txtFirstname=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Firstname,width=39)
		self.txtFirstname.grid(row=1,column=1)
		#Surname
		self.lblSurname=Label(DataFrameLEFT,font=('arial',20,'bold'),text='Surname ',padx=2,pady=2,bg='Ghost White')
		self.lblSurname.grid(row=2,column=0,sticky=W)
		self.txtSurname=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Surname,width=39)
		self.txtSurname.grid(row=2,column=1)
		#Dob
		self.lblDob=Label(DataFrameLEFT,font=('arial',20,'bold'),text='Date of Birth ',padx=2,pady=2,bg='Ghost White')
		self.lblDob.grid(row=3,column=0,sticky=W)
		self.txtDob=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Dob,width=39)
		self.txtDob.grid(row=3,column=1)
		#Age
		self.lblAge=Label(DataFrameLEFT,font=('arial',20,'bold'),text='Age ',padx=2,pady=2,bg='Ghost White')
		self.lblAge.grid(row=4,column=0,sticky=W)
		self.txtAge=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Age,width=39)
		self.txtAge.grid(row=4,column=1)
		#Gender
		self.lblGender=Label(DataFrameLEFT,font=('arial',20,'bold'),text='Gender ',padx=2,pady=2,bg='Ghost White')
		self.lblGender.grid(row=5,column=0,sticky=W)
		self.txtGender=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Gender,width=39)
		self.txtGender.grid(row=5,column=1)
		#Address
		self.lblAddress=Label(DataFrameLEFT,font=('arial',20,'bold'),text='Address ',padx=2,pady=2,bg='Ghost White')
		self.lblAddress.grid(row=6,column=0,sticky=W)
		self.txtAddress=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Address,width=39)
		self.txtAddress.grid(row=6,column=1)
		#Mobile
		self.lblMobile=Label(DataFrameLEFT,font=('arial',20,'bold'),text='Mobile ',padx=2,pady=2,bg='Ghost White')
		self.lblMobile.grid(row=7,column=0,sticky=W)
		self.txtMobile=Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Mobile,width=39)
		self.txtMobile.grid(row=7,column=1)

		#==========List box and scrollbar on DataFrameRIGHT============
		scrollbar=Scrollbar(DataFrameRIGHT)
		scrollbar.grid(row=0,column=1,sticky='ns')

		studentlist=Listbox(DataFrameRIGHT,width=41,height=16,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
		studentlist.bind('<<ListboxSelect>>',StudnetRec)
		studentlist.grid(row=0,column=0,padx=8)
		scrollbar.config(command=studentlist.yview)

		#==========Adding Buttons on ButtonFrame============

		self.btnAddData=Button(ButtonFrame,text="Add New",font=('arial',20,'bold'),height=1,width=10,bd=4,command=addData)
		self.btnAddData.grid(row=0,column=0)
		self.btnDisplay=Button(ButtonFrame,text="Display",font=('arial',20,'bold'),height=1,width=10,bd=4,command=DisplayData)
		self.btnDisplay.grid(row=0,column=1)
		self.btnClear=Button(ButtonFrame,text="Clear",font=('arial',20,'bold'),height=1,width=10,bd=4,command=clearData)
		self.btnClear.grid(row=0,column=2)
		self.btnDelete=Button(ButtonFrame,text="Delete",font=('arial',20,'bold'),height=1,width=10,bd=4,command=DeleteData)
		self.btnDelete.grid(row=0,column=3)
		self.btnSearch=Button(ButtonFrame,text="Search",font=('arial',20,'bold'),height=1,width=10,bd=4,command=searchDatabase)
		self.btnSearch.grid(row=0,column=4)
		self.btnUpdate=Button(ButtonFrame,text="Update",font=('arial',20,'bold'),height=1,width=10,bd=4,command=update)
		self.btnUpdate.grid(row=0,column=5)
		self.btnExit=Button(ButtonFrame,text="Exit",font=('arial',20,'bold'),height=1,width=10,bd=4,command=iexit)
		self.btnExit.grid(row=0,column=6)



def main():
	root=Tk()
	application=Student()
	application.display_window(root)
	root.mainloop()

if __name__=='__main__':
	main()