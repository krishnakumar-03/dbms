from tkinter import *
from tkinter import messagebox
from tabulate import tabulate
import random
import mysql.connector
from mysql.connector import errorcode

root=Tk()
root.title("Billing Project")
root.geometry('1600x750')
bg_color='#0d365c'


#*****************Initialization***********
c_name=StringVar()
c_phone=StringVar()
item=StringVar()
Rate=IntVar()
quantity=IntVar()
bill_no=IntVar()
x=random.randint(1000,9999)
bill_no.set(x)
global l
l=[]

#****************Functions*********************

def additm():
    n=Rate.get()
    m=quantity.get()*n
    l.append(m)
    if item.get()!='':
        textarea.insert((10.0+float(len(l)-1)), f"{item.get()}\t\t{quantity.get()}\t\t{ m}\n")
    else:
        messagebox.showerror('Error','Please enter an item!!')


def gbill():
    if c_name.get() == "" or c_phone.get() == "":
        messagebox.showerror("Error", "Customer detail are must")
    else:
        textAreaText = textarea.get(10.0,(10.0+float(len(l))))
        welcome()
        textarea.insert(END, textAreaText)
        textarea.insert(END, f"\n======================================")
        textarea.insert(END, f"\nTotal Paybill Amount :\t\t      {sum(l)}")
        textarea.insert(END, f"\n\n======================================")
        s=sum(l)
        print(sum(l))
        print(type(sum(l)))
        save_bill()

#****************DB conection*****************

def dbconnect():
    try:
        db = mysql.connector.connect(
            host='localhost',
            user='SYSTEM',
            password='123456',
            database='billing_system'
        )
        mycursor = db.cursor()

        mycursor.execute('''CREATE TABLE IF NOT EXISTS bills (
                                bill_no INT NOT NULL PRIMARY KEY,
                                c_name VARCHAR(20) DEFAULT NULL,
                                c_phone VARCHAR(10) DEFAULT NULL,
                                item VARCHAR(20) DEFAULT NULL,
                                rate INT DEFAULT NULL,
                                quantity INT DEFAULT NULL,
                                total INT DEFAULT NULL);''')

        # get variable values after user input
        a = c_name.get()
        c = c_phone.get()
        i = item.get()
        r = Rate.get()
        q = quantity.get()
        s = sum(l)

        mycursor.execute('''INSERT INTO bills 
                                (bill_no, c_name, c_phone, item, rate, quantity, total) 
                                VALUES (%s,%s,%s,%s,%s,%s,%s)''',
                            [bill_no.get(), a, c, i, r, q, s])

        db.commit()
        print("Data inserted successfully.")
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
            
    finally:
        db.close()


def clear():
    c_name.set('')
    c_phone.set('')
    item.set('')
    Rate.set('')
    quantity.set('')
    welcome()

def exit():
    op = messagebox.askyesno("Exit", "Do you really want to exit?")
    if op > 0:
        root.destroy()


def save_bill():
    op=messagebox.askyesno("Save bill","Do you want to save the Bill?")
    if op>0:
        dbconnect()
        messagebox.showinfo("Saved",f"Bill no, :{bill_no.get()} Saved Successfully")
    else:
        return
    
def welcome():
    textarea.delete(1.0,END)
    textarea.insert(END,"         Welcome to Punithastalam Biryani Center!!")
    textarea.insert(END,f"\n\nBill Number:\t\t{bill_no.get()}")
    textarea.insert(END,f"\nCustomer Name:\t\t{c_name.get()}")
    textarea.insert(END,f"\nPhone Number:\t\t{c_phone.get()}")
    textarea.insert(END,f"\n\n======================================")
    textarea.insert(END,"\nProduct\t\tQTY\t\tPrice")
    textarea.insert(END,f"\n======================================\n")
    textarea.configure(font=('times new roman',16,'bold'))



title=Label(root,pady=2,text="Billing Software",bd=12,bg=bg_color,fg='white',font=('times new roman', 25 ,'bold'),relief=GROOVE,justify=CENTER)
title.pack(fill=X)


#************Product Frames***************
F1=LabelFrame(root,bd=10,relief=GROOVE,text='Customer Details',font=('times new romon',15,'bold'),fg='#ffcc2e',bg=bg_color)
F1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(F1,text='Customer Name',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=0,padx=20,pady=5)
cname_txt=Entry(F1,width=15,textvariable=c_name,font='arial 15 bold',relief=SUNKEN,bd=7).grid(row=0,column=1,padx=10,pady=5)

cphone_lbl=Label(F1,text='Phone No. ',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=2,padx=20,pady=5)
cphone_txt=Entry(F1,width=15,font='arial 15 bold',textvariable=c_phone,relief=SUNKEN,bd=7).grid(row=0,column=3,padx=10,pady=5)


#*****************Product details**********************

F2 = LabelFrame(root, text='Product Details', font=('times new romon', 18, 'bold'), fg='#ffcc2e',bg=bg_color)
F2.place(x=420, y=180,width=550,height=500)
itm= Label(F2, text='Product Name', font=('times new romon',18, 'bold'), bg=bg_color, fg='lightgreen')
itm.grid(row=0, column=0, padx=30, pady=20)
itm_txt = Entry(F2, width=20,textvariable=item, font='arial 15 bold', relief=SUNKEN, bd=7)
itm_txt.grid(row=0, column=1, padx=10,pady=20)

rate= Label(F2, text='Product Rate', font=('times new romon',18, 'bold'), bg=bg_color, fg='lightgreen')
rate.grid(
row=1, column=0, padx=30, pady=20)
rate_txt = Entry(F2, width=20,textvariable=Rate, font='arial 15 bold', relief=SUNKEN, bd=7)
rate_txt.grid(row=1, column=1, padx=10,pady=20)

n= Label(F2, text='Product Quantity', font=('times new romon',18, 'bold'), bg=bg_color, fg='lightgreen')
n.grid(
row=2, column=0, padx=30, pady=20)
n_txt = Entry(F2, width=20,textvariable=quantity, font='arial 15 bold', relief=SUNKEN, bd=7)
n_txt.grid(row=2, column=1, padx=10,pady=20)

#****************Menu****************

f3 = LabelFrame(root, text='Menu', font=('times new romon', 18, 'bold'), fg='#ffcc2e',bg=bg_color)
f3.place(x=20, y=180,width=370,height=500)

itm1= Label(f3, text='Chicken Biryani', font=('times new romon',14, 'bold'), bg=bg_color, fg='lightgreen')
itm1.grid(row=0, column=0, padx=30, pady=15, sticky='W')

itm2= Label(f3, text='Rs.190', font=('times new romon',14, 'bold'), bg=bg_color, fg='lightgreen')
itm2.grid(row=0, column=1, padx=10, pady=15, sticky='W')

itm3= Label(f3, text='Mutton Biryani', font=('times new romon',14, 'bold'), bg=bg_color, fg='lightgreen')
itm3.grid(row=1, column=0, padx=30, pady=15, sticky='W')

itm4= Label(f3, text='Rs.240', font=('times new romon',14, 'bold'), bg=bg_color, fg='lightgreen')
itm4.grid(row=1, column=1, padx=10, pady=15, sticky='W')

itm5= Label(f3, text='Chicken 65(100gms)', font=('times new romon',14, 'bold'), bg=bg_color, fg='lightgreen')
itm5.grid(row=2, column=0, padx=30, pady=15, sticky='W')

itm6= Label(f3, text='Rs.150', font=('times new romon',14, 'bold'), bg=bg_color, fg='lightgreen')
itm6.grid(row=2, column=1, padx=10, pady=15, sticky='W')

itm7= Label(f3, text='Chicken 65(Boneless)', font=('times new romon',14, 'bold'), bg=bg_color, fg='lightgreen')
itm7.grid(row=3, column=0, padx=30, pady=15, sticky='W')

itm8= Label(f3, text='Rs.200', font=('times new romon',14, 'bold'), bg=bg_color, fg='lightgreen')
itm8.grid(row=3, column=1, padx=10, pady=15, sticky='W')

itm9= Label(f3, text='Veg Shawarma', font=('times new romon',14, 'bold'), bg=bg_color, fg='lightgreen')
itm9.grid(row=4, column=0, padx=30, pady=15, sticky='W')

itm10= Label(f3, text='Rs.50', font=('times new romon',14, 'bold'), bg=bg_color, fg='lightgreen')
itm10.grid(row=4, column=1, padx=10, pady=15, sticky='W')

itm11= Label(f3, text='NV Shawarma', font=('times new romon',14, 'bold'), bg=bg_color, fg='lightgreen')
itm11.grid(row=5, column=0, padx=30, pady=15, sticky='W')

itm12= Label(f3, text='Rs.70', font=('times new romon',14, 'bold'), bg=bg_color, fg='lightgreen')
itm12.grid(row=5, column=1, padx=10, pady=15, sticky='W')

itm13= Label(f3, text='Prawn 65', font=('times new romon',14, 'bold'), bg=bg_color, fg='lightgreen')
itm13.grid(row=6, column=0, padx=30, pady=15, sticky='W')

itm14= Label(f3, text='Rs.140', font=('times new romon',14, 'bold'), bg=bg_color, fg='lightgreen')
itm14.grid(row=6, column=1, padx=10, pady=15, sticky='W')

itm15= Label(f3, text='Fresh Juice', font=('times new romon',14, 'bold'), bg=bg_color, fg='lightgreen')
itm15.grid(row=7, column=0, padx=30, pady=15, sticky='W')

itm16= Label(f3, text='Rs.50', font=('times new romon',14, 'bold'), bg=bg_color, fg='lightgreen')
itm16.grid(row=7, column=1, padx=10, pady=15, sticky='W')

#========================Bill area================
f4=Frame(root,relief=RAISED,bd=10)
f4.place(x=1000,y=180,width=500,height=500)

bill_title=Label(f4,text='BILL AREA',font='arial 25 bold',bd=30,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(f4,orient=VERTICAL)
textarea=Text(f4,yscrollcommand=scrol_y)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack()

welcome()

#*****************Buttons***************
btn1=Button(F2,text='Add item',font='arial 15 bold',command=additm,padx=5,pady=10,bg='lime',width=15)
btn1.grid(row=3,column=0,padx=10,pady=30)
btn2=Button(F2,text='Generate Bill',font='arial 15 bold',command=gbill,padx=5,pady=10,bg='lime',width=15)
btn2.grid(row=3,column=1,padx=10,pady=30)
btn3=Button(F2,text='Clear',font='arial 15 bold',padx=5,pady=10,command=clear,bg='lime',width=15)
btn3.grid(row=4,column=0,padx=10,pady=30)
btn4=Button(F2,text='Exit',font='arial 15 bold',padx=5,pady=10,command=exit,bg='lime',width=15)
btn4.grid(row=4,column=1,padx=10,pady=30)

root.mainloop()
print(c_name)
