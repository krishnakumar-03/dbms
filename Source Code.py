from tkinter import *
from tkinter import messagebox
from tabulate import tabulate
import random
import sqlite3
root=Tk()
root.title("Grocery Billing Project")
root.geometry('1600x750')
bg_color='#4D0039'

#**********variable*************

c_name=StringVar()
c_phone=StringVar()
item=StringVar()
Rate=IntVar()
quantity=IntVar()
bill_no=StringVar()
x=random.randint(1000,9999)
bill_no.set(str(x))



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

'''def price():
    roo = Tk()
    roo.title("Price List")
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Products", bg="darkblue", fg="white", bd=5)
    lblrestaurant.grid(row=0, column=0)
    lblrestaurant = Label(roo, font=('aria', 15,'bold'), text="                 ", fg="white", anchor=W)
    lblrestaurant.grid(row=0, column=2)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="PRICE",bg="darkblue", fg="white", anchor=W)
    lblrestaurant.grid(row=0, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Maggi", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="12", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Toothpaste", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="20", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Five star", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="10", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Perfumes", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="230", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Ice cream", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="45", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="100", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=3)
'''

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
        save_bill()

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
        bill_details=textarea.get('1.0',END)
        f1=open("bills/"+str(bill_no.get())+".txt","w")
        f1.write(bill_details)
        f1.close()
        messagebox.showinfo("Saved",f"Bill no, :{bill_no.get()} Saved Successfully")
    else:
        return
def welcome():
    textarea.delete(1.0,END)
    textarea.insert(END,"      Welcome Punithastalam Shopping Center")
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
F1=LabelFrame(root,bd=10,relief=GROOVE,text='Customer Details',font=('times new romon',15,'bold'),fg='gold',bg=bg_color)
F1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(F1,text='Customer Name',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=0,padx=20,pady=5)
cname_txt=Entry(F1,width=15,textvariable=c_name,font='arial 15 bold',relief=SUNKEN,bd=7).grid(row=0,column=1,padx=10,pady=5)

cphone_lbl=Label(F1,text='Phone No. ',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=2,padx=20,pady=5)
cphone_txt=Entry(F1,width=15,font='arial 15 bold',textvariable=c_phone,relief=SUNKEN,bd=7).grid(row=0,column=3,padx=10,pady=5)

F2 = LabelFrame(root, text='Product Details', font=('times new romon', 18, 'bold'), fg='gold',bg=bg_color)
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

F10 = LabelFrame(root, text='Menu', font=('times new romon', 18, 'bold'), fg='gold',bg=bg_color)
F10.place(x=20, y=180,width=360,height=500)
'''head1= Label(F10, text='Name', font=('times new romon',18, 'bold'), bg=bg_color, fg='lightgreen')
head1.grid(row=0, column=0, padx=30, pady=20)

head2= Label(F10, text='Cost', font=('times new romon',18, 'bold'), bg=bg_color, fg='lightgreen')
head2.grid(row=0, column=1, padx=30, pady=20)

itm1= Label(F10, text='Maggi', font=('times new romon',18, 'bold'), bg=bg_color, fg='lightgreen')
itm1.grid(row=1, column=0, padx=30, pady=20)
#itm_txt = Entry(F10, width=20,textvariable=item, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=0, column=1, padx=10,pady=20)

itm2= Label(F10, text='Product Rate', font=('times new romon',18, 'bold'), bg=bg_color, fg='lightgreen')
itm2.grid(row=1, column=1, padx=30, pady=20)
#rate_txt = Entry(F10, width=20,textvariable=Rate, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=1, column=1, padx=10,pady=20)

itm3= Label(F10, text='Product Quantity', font=('times new romon',18, 'bold'), bg=bg_color, fg='lightgreen')
itm3.grid(row=2, column=0, padx=30, pady=20)
#n_txt = Entry(F10, width=20,textvariable=quantity, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=2, column=1, padx=10,pady=20)'''

#========================Bill area================
F3=Frame(root,relief=RAISED,bd=10)
F3.place(x=1000,y=180,width=500,height=500)

bill_title=Label(F3,text='BILL AREA',font='arial 25 bold',bd=30,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scrol_y)
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
#btn5=Button(F2,text='Menu',font='arial 15 bold',padx=5,pady=10,command=price,bg='lime',width=15)
#btn5.grid(row=5,column=0,padx=10,pady=30)

root.mainloop()
print(c_name)
