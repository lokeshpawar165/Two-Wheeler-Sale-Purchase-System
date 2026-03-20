from datetime import date
import os
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.ttk import Combobox
from fpdf import FPDF
import mysql.connector
from tkinter import messagebox
from tkcalendar import DateEntry
from printbill import print_bill

def open_billmast():

    bill_win = Toplevel()
    bill_win.title("Billing Management")
    bill_win.state("zoomed")
    bill_win.configure(bg="#eef2f7")

    # ================= HEADER =================

    header = Frame(bill_win,bg="#0b3d91",height=80)
    header.pack(fill=X)

    title = Label(header,
    text="Two Wheeler Sale Purchase System - Billing Management",
    font=("Georgia",24,"bold"),
    bg="#0b3d91",
    fg="white")

    title.pack(pady=18)


    subtitle = Label(bill_win,
    text="Billing Management",
    font=("Segoe UI",16,"bold"),
    bg="#eef2f7",
    fg="#0b3d91")

    subtitle.pack(pady=15)


    # ================= CARD FRAME =================

    card = Frame(bill_win,bg="white",bd=1,relief="solid")
    card.place(relx=0.5,rely=0.5,anchor="center",width=700,height=620)


    form = Frame(card,bg="white")
    form.pack(pady=20)

    f = ("Segoe UI",11)

    # ================= DATABASE FUNCTIONS =================

    def load_customer():
        mydb=mysql.connector.connect(host="localhost",user="root",password="",database="twsps")
        cur=mydb.cursor()
        cur.execute("select cno,cname from custmast")
        data=cur.fetchall()
        txtcno['values']=[f"{x[0]} - {x[1]}" for x in data]
        mydb.close()


    def load_model():
        mydb=mysql.connector.connect(host="localhost",user="root",password="",database="twsps")
        cur=mydb.cursor()
        cur.execute("select mcode,mname from modelmast")
        data=cur.fetchall()
        txtmcode['values']=[f"{x[0]} - {x[1]}" for x in data]
        mydb.close()


    def show_price(event):
        sel=txtmcode.get()
        mcode=sel.split(" - ")[0]

        mydb=mysql.connector.connect(host="localhost",user="root",password="",database="twsps")
        cur=mydb.cursor()
        cur.execute("select total from modelmast where mcode=%s",(mcode,))
        data=cur.fetchone()
        mydb.close()

        if data:
            txttotal.delete(0,END)
            txttotal.insert(0,data[0])


    def clsfields():
        txtbdate.set_date(date.today())
        txtcno.set("")
        txtmcode.set("")
        txtengineno.delete(0,END)
        txtchassisno.delete(0,END)
        txtbatteryno.delete(0,END)
        txtcolor.delete(0,END)
        txttotal.delete(0,END)
        txtremark.delete(0,END)


    def maxrec():
        mydb=mysql.connector.connect(user="root",password="",host="localhost",database="twsps")
        cur=mydb.cursor()
        cur.execute("select max(bno) from billmast")
        data=cur.fetchone()
        mx=data[0]+1 if data[0] else 1

        txtbno.config(state="normal")
        txtbno.delete(0,END)
        txtbno.insert(0,str(mx))
        txtbno.config(state="readonly")

        mydb.close()
        clsfields()


    def saverec():

        s1=txtbno.get()
        s2=txtbdate.get_date().strftime("%Y-%m-%d")
        s3=txtcno.get().split(" - ")[0]
        s4=txtmcode.get().split(" - ")[0]
        s5=txtengineno.get()
        s6=txtchassisno.get()
        s7=txtbatteryno.get()
        s8=txtcolor.get()
        s9=txttotal.get()
        s10=txtremark.get() if txtremark.get()!="" else "NA"

        if s3=="":
            messagebox.showwarning("Warning","Please Select Customer")
            return

        mydb=mysql.connector.connect(user="root",password="",host="localhost",database="twsps")
        cur=mydb.cursor()

        cur.execute(
        "insert into billmast values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (s1,s2,s3,s4,s5,s6,s7,s8,s9,s10)
        )

        mydb.commit()
        mydb.close()

        messagebox.showinfo("Success","Bill Saved Successfully")
        maxrec()


    def serrec():
        s1=askstring("Search","Enter Bill No")

        if not s1:
            return

        mydb=mysql.connector.connect(user="root",password="",host="localhost",database="twsps")
        cur=mydb.cursor()

        cur.execute("select * from billmast where bno=%s",(s1,))
        data=cur.fetchone()

        mydb.close()

        if not data:
            messagebox.showinfo("Info","Record Not Found")
            return

        txtbno.config(state="normal")
        txtbno.delete(0,END)
        txtbno.insert(0,data[0])
        txtbno.config(state="readonly")

        txtbdate.set_date(data[1])
        txtcno.set(data[2])
        txtmcode.set(data[3])
        txtengineno.insert(0,data[4])
        txtchassisno.insert(0,data[5])
        txtbatteryno.insert(0,data[6])
        txtcolor.insert(0,data[7])
        txttotal.insert(0,data[8])
        txtremark.insert(0,data[9])


    def uprec():

        s1=txtbno.get()
        s2=txtbdate.get()
        s3=txtcno.get()
        s4=txtmcode.get()
        s5=txtengineno.get()
        s6=txtchassisno.get()
        s7=txtbatteryno.get()
        s8=txtcolor.get()
        s9=txttotal.get()
        s10=txtremark.get()

        mydb=mysql.connector.connect(user="root",password="",host="localhost",database="twsps")
        cur=mydb.cursor()

        cur.execute(
        "update billmast set bdate=%s,cno=%s,mcode=%s,engineno=%s,chassisno=%s,batno=%s,color=%s,price=%s,remark=%s where bno=%s",
        (s2,s3,s4,s5,s6,s7,s8,s9,s10,s1)
        )

        mydb.commit()
        mydb.close()

        messagebox.showinfo("Success","Record Updated Successfully")
        maxrec()


    def delrec():

        s1=txtbno.get()

        if messagebox.askyesno("Confirm","Delete this record?"):

            mydb=mysql.connector.connect(user="root",password="",host="localhost",database="twsps")
            cur=mydb.cursor()

            cur.execute("delete from billmast where bno=%s",(s1,))

            mydb.commit()
            mydb.close()

            messagebox.showinfo("Deleted","Record Deleted")
            maxrec()




    # ================= FORM FIELDS =================

    Label(form,text="Bill No",font=f,bg="white").grid(row=0,column=0,padx=20,pady=8,sticky="w")
    txtbno=Entry(form,font=f,width=40)
    txtbno.grid(row=0,column=1,pady=8)

    Label(form,text="Bill Date",font=f,bg="white").grid(row=1,column=0,padx=20,pady=8,sticky="w")
    txtbdate=DateEntry(form,font=f,width=37,date_pattern="dd-mm-yyyy")
    txtbdate.grid(row=1,column=1,pady=8)

    Label(form,text="Customer No",font=f,bg="white").grid(row=2,column=0,padx=20,pady=8,sticky="w")
    txtcno=Combobox(form,font=f,width=37,state="readonly")
    txtcno.grid(row=2,column=1,pady=8)
    load_customer()

    Label(form,text="Model Code",font=f,bg="white").grid(row=3,column=0,padx=20,pady=8,sticky="w")
    txtmcode=Combobox(form,font=f,width=37,state="readonly")
    txtmcode.grid(row=3,column=1,pady=8)
    load_model()
    txtmcode.bind("<<ComboboxSelected>>",show_price)

    Label(form,text="Engine No",font=f,bg="white").grid(row=4,column=0,padx=20,pady=8,sticky="w")
    txtengineno=Entry(form,font=f,width=40,bd=1,relief="solid")
    txtengineno.grid(row=4,column=1,pady=8)

    Label(form,text="Chassis No",font=f,bg="white").grid(row=5,column=0,padx=20,pady=8,sticky="w")
    txtchassisno=Entry(form,font=f,width=40,bd=1,relief="solid")
    txtchassisno.grid(row=5,column=1,pady=8)

    Label(form,text="Battery No",font=f,bg="white").grid(row=6,column=0,padx=20,pady=8,sticky="w")
    txtbatteryno=Entry(form,font=f,width=40,bd=1,relief="solid")
    txtbatteryno.grid(row=6,column=1,pady=8)

    Label(form,text="Color",font=f,bg="white").grid(row=7,column=0,padx=20,pady=8,sticky="w")
    txtcolor=Entry(form,font=f,width=40,bd=1,relief="solid")
    txtcolor.grid(row=7,column=1,pady=8)

    Label(form,text="Price",font=f,bg="white").grid(row=8,column=0,padx=20,pady=8,sticky="w")
    txttotal=Entry(form,font=f,width=40,bd=1,relief="solid")
    txttotal.grid(row=8,column=1,pady=8)

    Label(form,text="Remark",font=f,bg="white").grid(row=9,column=0,padx=20,pady=8,sticky="w")
    txtremark=Entry(form,font=f,width=40,bd=1,relief="solid")
    txtremark.grid(row=9,column=1,pady=8)


    # ================= BUTTON PANEL =================

    btnframe=Frame(card,bg="white")
    btnframe.pack(pady=20)

    Button(btnframe,text="ADD",font=("Segoe UI",10,"bold"),bg="#0d47a1",fg="white",width=10,command=maxrec).grid(row=0,column=0,padx=8)

    Button(btnframe,text="SAVE",font=("Segoe UI",10,"bold"),bg="#0d47a1",fg="white",width=10,command=saverec).grid(row=0,column=1,padx=8)

    Button(btnframe,text="SEARCH",font=("Segoe UI",10,"bold"),bg="#0d47a1",fg="white",width=10,command=serrec).grid(row=0,column=2,padx=8)

    Button(btnframe,text="UPDATE",font=("Segoe UI",10,"bold"),bg="#0d47a1",fg="white",width=10,command=uprec).grid(row=0,column=3,padx=8)

    Button(btnframe,text="DELETE",font=("Segoe UI",10,"bold"),bg="#0d47a1",fg="white",width=10,command=delrec).grid(row=0,column=4,padx=8)

    Button(btnframe,text="CLOSE",font=("Segoe UI",10,"bold"),bg="#f51111",fg="white",width=10,command=bill_win.destroy).grid(row=0,column=5,padx=8)

    # Button(card,text="PRINT BILL",font=("Segoe UI",11,"bold"),bg="#43a047",fg="white",width=15,command=print_bill).pack(pady=10)
    
    Button(card, text="PRINT BILL", font=("Segoe UI", 11, "bold"),bg="#43a047", fg="white", width=15,command=lambda: print_bill(
        txtbno,
        txtbdate,
        txtcno,
        txtmcode,
        txtengineno,
        txtchassisno,
        txtbatteryno,
        txtcolor,
        txttotal,
        txtremark)).pack(pady=10)
    
    maxrec()