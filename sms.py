from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import cx_Oracle
import socket
import requests
import bs4
import datetime

def f1():
	root.withdraw()
	add.deiconify()
def f2():
	view.withdraw()
	root.deiconify()
def f3():
	root.withdraw()
	up.deiconify()
def f4():
	root.withdraw()
	dele.deiconify()
def f5():
	viewdata.delete(1.0,END)
	root.withdraw()
	view.deiconify()
	con = None
	try:
		con = cx_Oracle.connect('system/abc123')
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		msg= ""
		for d in data:
			msg = msg +"\n"+"roll no "+str( d[0])+"\nname "+ str(d[1])+"\n"+ "marks "+str( d[2])+"\n"
		viewdata.insert(INSERT,msg)
	except cx_Oracle.DatabaseError as e:
		messagebox.showerror("issue ",string(e))
	finally:
		if con is not None:
			con.close()
		

	
def f6():
	con = None
	try:
		con = cx_Oracle.connect('system/abc123')
		rno = entrno.get()
		name = entname.get()
		marks = entmarks.get()
		if rno=="":
			messagebox.showwarning("issue "," invalid roll no \n roll no cannot be empty")
			entrno.delete(0,END)
			entrno.focus_set()
		elif rno.isdigit() == False:
			messagebox.showwarning("issue "," invalid roll no \n roll no. should only be numeric")
			entrno.delete(0,END)
			entrno.focus_set()
		elif (int(rno)<=0):
			messagebox.showwarning("issue "," invalid roll no \n roll no cannot be negative or zero")
			entrno.delete(0,END)
			entrno.focus_set()
		elif name == "":
			messagebox.showwarning("issue "," invalid name \n name cannot be empty ")
			entname.delete(0,END)
			entname.focus_set()
		elif name.isalpha()== False:
			messagebox.showwarning("issue "," invalid name \n name should be only alphabetic ")
			entname.delete(0,END)
			entname.focus_set()
		elif len(name)<2:
			messagebox.showwarning("issue "," invalid name \n name cannot be of a single letter")
			entname.delete(0,END)
			entname.focus_set()
		elif marks == "":
			messagebox.showwarning("issue "," invalid marks \n marks cannot be empty ")
			entmarks.delete(0,END)
			entmarks.focus_set()
		elif marks.isdigit() == False:
			messagebox.showwarning("issue "," invalid marks \n marks should be only digit ")
			entmarks.delete(0,END)
			entmarks.focus_set()
		elif int(marks) >100:
			messagebox.showwarning("issue "," invalid marks \n marks cannot be greater than 100")
			entmarks.delete(0,END)
			entmarks.focus_set()
		elif int(marks)<0:
			messagebox.showwarning("issue "," invalid marks \n marks cannot negative")
			entmarks.delete(0,END)
			entmarks.focus_set()
		else:	
			cursor =con.cursor()
			sql = "insert into student values('%s','%s','%s')"
			args =(rno,name,marks)
			cursor.execute(sql % args)
			con.commit()
			messagebox.showinfo("success "," record inserted " )
			entrno.delete(0,END)
			entname.delete(0,END)
			entmarks.delete(0,END)
			entrno.focus_set()
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("issue "," roll no already exists")
		entrno.delete(0,END)
		entrno.focus_set()
	finally:
		if con is not None:
			con.close()
	
	
			
def f7():
	add.withdraw()
	root.deiconify()
def f8():
	name =[]
	marks = []
	import matplotlib.pyplot as plt
	import numpy as np
	con = None
	try:
		con = cx_Oracle.connect('system/abc123')
		cursor = con.cursor()
		sql = "select * from student order by marks DESC"
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			name.append(d[1])
			marks.append(d[2])
		hname = (name[0],name[1],name[2])
		hmarks = (marks[0],marks[1],marks[2])
		plt.gcf().canvas.set_window_title("Top three students")
		x = np.arange(len(hname))
		plt.bar(x,hmarks,width = 0.25,label = "marks")
		plt.xticks(x,hname)
		plt.title("highest marks gaining students")
		plt.xlabel('names',fontsize = 20)
		plt.ylabel('marks',fontsize = 20)
		plt.legend()
		plt.grid()
		plt.show()
	except cx_Oracle.DatabaseError as e:
		messagebox.showerror("issue",e)
	except Exception as s:
		messagebox.showerror("issue",s)
	finally:
		if con is not None:
			con.close()
def f9():
	con =None
	try:
		con = cx_Oracle.connect('system/abc123')
		entuprno.focus_set()
		rno = entuprno.get()
		name = entupname.get()
		marks = entupmarks.get()
		
		cursor = con.cursor()
		sql = "select rno from student where rno='%s'"
		cursor.execute(sql % rno)
		data = cursor.fetchall()
		if rno=="":
			messagebox.showwarning("issue "," invalid roll no \n roll no cannot be empty")
			entuprno.delete(0,END)
			entuprno.focus_set()
		elif len(data)==0:
			messagebox.showerror("Error", "Record does not exists")
			entuprno.delete(0, END)
			entuprno.focus()
		elif rno.isdigit() == False:
			messagebox.showwarning("issue "," invalid roll no \n roll no. should only be numeric")
			entuprno.delete(0,END)
			entuprno.focus_set()
		elif (int(rno)<=0):
			messagebox.showwarning("issue "," invalid roll no \n roll no cannot be negative or zero")
			entuprno.delete(0,END)
			entuprno.focus_set()
		elif name == "":
			messagebox.showwarning("issue "," invalid name \n name cannot be empty ")
			entupname.delete(0,END)
			entupname.focus_set()
		elif name.isalpha()== False:
			messagebox.showwarning("issue "," invalid name \n name should be only alphabetic ")
			entupname.delete(0,END)
			entupname.focus_set()
		elif len(name)<2:
			messagebox.showwarning("issue "," invalid name \n name cannot be of a single letter")
			entupname.delete(0,END)
			entupname.focus_set()
		elif marks == "":
			messagebox.showwarning("issue "," invalid marks \n marks cannot be empty ")
			entupmarks.delete(0,END)
			entupmarks.focus_set()
		elif marks.isdigit() == False:
			messagebox.showwarning("issue "," invalid marks \n marks should be only digit ")
			entupmarks.delete(0,END)
			entupmarks.focus_set()
		elif int(marks) >100:
			messagebox.showwarning("issue "," invalid marks \n marks cannot be greater than 100")
			entupmarks.delete(0,END)
			entupmarks.focus_set()
		elif int(marks)<0:
			messagebox.showwarning("issue "," invalid marks \n marks cannot negative")
			entupmrks.delete(0,END)
			entupmrks.focus_set()
		else:
			cursor = con.cursor()
			sql = "update student set name =('%s'),marks=('%s') where rno=('%s')"
			args = (name,marks,rno)
			cursor.execute(sql % args)
			con.commit()
			messagebox.showinfo("success","Record updated")
			entuprno.delete(0,END)
			entupname.delete(0,END)
			entupmarks.delete(0,END)
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("issue",e)
	finally:
		if con is not None:
			con.close()
			
	
def f10():
	up.withdraw()
	root.deiconify()
def f11():
	con = None
	try:
		con = cx_Oracle.connect('system/abc123')
		entdelrno.focus_set()
		rno = entdelrno.get()

		cursor = con.cursor()
		sql = "select * from student where rno= '%s'"
		cursor.execute(sql % rno)
		data = cursor.fetchall()
		if len(data)==0:
			messagebox.showerror("Error", "Record does not exists")
			entdelrno.delete(0, END)
			entdelrno.focus()
		else:
			cursor = con.cursor()
			sql = "delete from student where rno=('%s')"
			args = (rno)
			cursor.execute(sql % args)
			con.commit()
			messagebox.showinfo("success" ,"Record deleted ")
			entdelrno.delete(0,END)
			entdelrno.focus_set()
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("issue ",e)	
	finally:
		if con is not None:
			con.close()
			
	
def f12():
	dele.withdraw()
	root.deiconify()


root = Tk()      #window
root.title("Student Mangement System")  #for title
root.geometry("600x600+300+50") #for lenbred+x+y
#add button
btnadd = Button(root,text='ADD' , font=('Gabriola',16,'italic'),width=15,bg='light green',command=f1)
btnadd.pack(pady = 10)
#view button
btnview = Button(root,text="VIEW",font=("Gabriola",16,"italic"),width=15,bg='yellow',command=f5)
btnview.pack(pady = 10)
#update button
btnup = Button(root,text="UPDATE",font=("Gabriola",16,"italic"),width=15,bg='pink',command=f3)
btnup.pack(pady = 10)
#delete button
btndel = Button(root,text="DELETE",font=("Gabriola",16,"italic"),width=15,bg='brown',command=f4)
btndel.pack(pady = 10)
#graph button
btngraph=Button(root,text='GRAPH',font=('Gabriola',16,'bold'),width=15,bg='peach puff',command=f8)
btngraph.pack(pady=10)

#for city
res=requests.get("https://ipinfo.io")
data = res.json()
city=data['city']
lblcity = Label(root,text = "CITY: ",font=("Gabriola",16,"italic"))
lblci = Label(root,text = city , font= ("Gabriola",16,"bold"))
lblcity.place(x=100,y=500)
lblci.place(x=150,y=500)


#for temp

a1 = "https://api.openweathermap.org/data/2.5/weather?units=metric"
a2 = "&q=" + city
a3 ="&appid=c6e315d09197cec231495138183954bd"
api_address=a1+a2+a3
res = requests.get(api_address)
data = res.json()
main = data['main']
temp = main['temp']
lbltemp = Label(root,text = "Temperature : ",font = ("Gabriola",16,"italic"))
lbl = Label(root,text =temp, font = ("Gabriola",16,"bold"))
lbltemp.place(x=375,y=500)
lbl.place(x=500,y=500)


#for qotd
res = requests.get("http://www.brainyquote.com/quotes_of_the_day.html")
soup = bs4.BeautifulSoup(res.text,'lxml')
date = datetime.datetime.now().date()
quote = soup.find('img',{"class": "p-qotd"})
msg = quote['alt']
lblqotd = Label(root,text = "QOTD :",font =("Gabriola",16,"italic"))
lbl = Label(root, text = msg,font=("Gabriola",16,"bold"))
lblqotd.place(x=50,y=550)
lbl.place(x=110,y=550)

#new add student window

add=Toplevel(root)
add.title("NEW ENTRIES")
add.geometry("600x600+300+5")
add.configure(background = "sky blue")

#for roll no:
lblrno = Label(add,text = "ENTER THE ROLL NO. ",font=("Times of Roman",16,"bold"),bg='light green')
entrno = Entry(add,bd = 6, font = ("Times of Roman",18,"italic"))
lblrno.pack()
entrno.pack()

#for name:
lblname = Label(add,text = "Enter the Name",font=("Times of Roman",16,"bold"),bg='light green')
entname = Entry(add,bd = 6,font=("Gabriola",18,"italic","bold"))
lblname.pack()
entname.pack()

#for marks:
lblmarks = Label(add,text = "Enter the Marks",font=("Times of Roman",16,"italic"),bg='light green')
entmarks = Entry(add,bd = 6,font=("Gabriola",16,"italic","bold"))
lblmarks.pack()
entmarks.pack()

#save button
btnsave= Button(add,text= "SAVE",font=("Gabriola",16,"bold"),width=15,fg='hot pink',command=f6)
btnsave.pack(pady = 10)

#back button
btnback= Button(add,text= "BACK",font=("Gabriola",16,"bold"),width=15,fg='coral',command=f7)
btnback.pack(pady = 10)
add.withdraw()


#for view window

view = Toplevel(root)
view.title("VIEW LIST OF STUDENTS")
view.geometry("600x600+300+50")
view.configure(background='linen')

viewdata = scrolledtext.ScrolledText(view,width = 30,height=20)
viewdata.pack(pady = 20)
#back button
btnback = Button(view,text="BACK",font = ('Gabriola',16,"bold"),fg="red",width=10,command = f2)
btnback.pack(pady = 20)
view.withdraw()

#update window
up =  Toplevel(root)
up.title("UPDATE LIST OF STUDENT")
up.geometry("600x600+300+50")
#for rollno
lbluprno=Label(up,text="ENTER THE ROLL NO TO UPDATE",font=("Gabriola",16,"bold"),bg='pink')
entuprno=Entry(up,bd=6,font=("Gabriola",16,"italic"))
lbluprno.pack()
entuprno.pack()

#for name
lblupname=Label(up,text="ENTER THE NAME",font=("Gabriola",16,"bold"),bg='pink')
entupname=Entry(up,bd=6,font=("Gabriola",16,"italic"))
lblupname.pack()
entupname.pack()

#for marks
lblupmarks=Label(up,text="ENTER THE MARKS",font=("Gabriola",16,"bold"),bg='pink')
entupmarks=Entry(up,bd=6,font=("Gabriola",16,"italic"))
lblupmarks.pack()
entupmarks.pack()


#for update button
btnup = Button(up,text="UPDATE",font=("Gabriola",16,"bold"),width=10,command = f9)
btnup.pack(pady=10)

#for back button
btnback = Button(up,text="BACK",font=("Gabriola",16,"bold"),width=10,command = f10)

btnback.pack(pady=10)
up.withdraw()


#for delete window
dele = Toplevel(root)
dele.title("WANT TO DELETE")
dele.geometry("600x600+350+50")


#fo roll no
lbldelrno = Label(dele,text = "ENTER THE ROLL NO TO DELETE",font=("Gabriola",16,"bold"))
entdelrno = Entry(dele,bd= 6,font=("Gabriola",18,"bold"))
lbldelrno.pack()
entdelrno.pack()
#for delete button
btndel = Button(dele,text="DELETE",font=("Gabriola",16,"bold"),width=20,command = f11)
btndel.pack(pady=10)
#for back button
btndelback = Button(dele,text="BACK",font=("Gabriola",16,"bold"),width= 20,command=f12)
btndelback.pack(pady = 20)
dele.withdraw();





















root.mainloop()




  
	
