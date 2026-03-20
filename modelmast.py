from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.simpledialog import askstring
import mysql.connector

def open_modelmast():
    model_win = Toplevel()
    model_win.title("Model Master Window")

    # -------- FULL SCREEN MODE --------
    model_win.state("zoomed")  # Windows fullscreen
    model_win.configure(bg="#d6eaf8")

    # ---------- CENTER FRAME ----------
    center_frame = Frame(model_win, bg="#d6eaf8")
    center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # --------------------------------
    #       Database Functions
    # --------------------------------

    def clsfields():
        txtmname.delete(0, END)
        txtmtype.delete(0, END)
        txtmprice.delete(0, END)
        txtrto.delete(0, END)
        txtins.delete(0, END)
        txtacc.delete(0, END)
        txtmtax.delete(0, END)
        txttotal.delete(0, END)

        txtmprice.insert(0, 0)
        txtrto.insert(0, 0)
        txtins.insert(0, 0)
        txtacc.insert(0, 0)
        txtmtax.insert(0, 0)

    def safe_int(entry):
        v = entry.get()
        return int(v) if v.isdigit() else 0

    def cal(event=None):
        p = safe_int(txtmprice)
        r = safe_int(txtrto)
        i = safe_int(txtins)
        a = safe_int(txtacc)
        m = safe_int(txtmtax)
        total = p + r + i + a + m
        txttotal.delete(0, END)
        txttotal.insert(0, total)

    def maxrec():
        mydb = mysql.connector.connect(user="root", password="", host="localhost", database="twsps")
        mycur = mydb.cursor()
        mycur.execute("select max(mcode) from modelmast")
        mydata = mycur.fetchone()
        mx = mydata[0] + 1 if mydata[0] else 1

        txtmcode.config(state="normal")
        txtmcode.delete(0, END)
        txtmcode.insert(0, str(mx))
        txtmcode.config(state="readonly")
        clsfields()

    def saverec():
        s1 = txtmcode.get()
        s2 = txtmname.get()
        s3 = txtmtype.get()
        s4 = txtmprice.get()
        s5 = txtrto.get()
        s6 = txtins.get()
        s7 = txtacc.get()
        s8 = txtmtax.get()
        s9 = txttotal.get()

        if not all([s2, s3, s4, s5, s6, s7, s8, s9]):
            messagebox.showinfo("Warning", "All fields are required")
            return

        mydb = mysql.connector.connect(user="root", password="", host="localhost", database="twsps")
        mycur = mydb.cursor()
        mycur.execute(
            "insert into modelmast values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (s1, s2, s3, s4, s5, s6, s7, s8, s9)
        )
        mydb.commit()
        messagebox.showinfo("Success", "Record Saved Successfully")
        maxrec()

    def serrec():
        clsfields()
        s1 = askstring("Search", "Enter Model Code")
        if not s1:
            return

        mydb = mysql.connector.connect(user="root", password="", host="localhost", database="twsps")
        mycur = mydb.cursor()
        mycur.execute("select * from modelmast where mcode=%s", (s1,))
        data = mycur.fetchone()

        if not data:
            messagebox.showinfo("Info", "Record Not Found")
            return
        
        txtmcode.config(state="normal")
        txtmcode.delete(0, END)
        txtmcode.insert(0, data[0])
        txtmcode.config(state="readonly")

        txtmname.insert(0, data[1])
        txtmtype.insert(0, data[2])
        txtmprice.insert(0, data[3])
        txtrto.insert(0, data[4])
        txtins.insert(0, data[5])
        txtacc.insert(0, data[6])
        txtmtax.insert(0, data[7])
        txttotal.insert(0, data[8])

    def uprec():
        s1 = txtmcode.get()
        s2 = txtmname.get()
        s3 = txtmtype.get()
        s4 = txtmprice.get()
        s5 = txtrto.get()
        s6 = txtins.get()
        s7 = txtacc.get()
        s8 = txtmtax.get()
        s9 = txttotal.get()

        mydb = mysql.connector.connect(user="root", password="", host="localhost", database="twsps")
        mycur = mydb.cursor()
        mycur.execute(
            "update modelmast set mname=%s, mtype=%s, mprice=%s, rto=%s, insurance=%s, accessory=%s, mtax=%s, total=%s where mcode=%s",
            (s2, s3, s4, s5, s6, s7, s8, s9, s1)
        )
        mydb.commit()
        messagebox.showinfo("Success", "Record Updated Successfully")
        maxrec()

    def delrec():
        s1 = txtmcode.get()
        if messagebox.askyesno("Confirm", "Delete this record?"):
            mydb = mysql.connector.connect(user="root", password="", host="localhost", database="twsps")
            mycur = mydb.cursor()
            mycur.execute("delete from modelmast where mcode=%s", (s1,))
            mydb.commit()
            messagebox.showinfo("Deleted", "Record Deleted")
            maxrec()

    # --------------------------------
    #            UI DESIGN
    # --------------------------------

    title = Label(center_frame, text="Two Wheeler Sale Purchase System", font=("Georgia", 26, "bold"), bg="#d6eaf8", fg="#0d47a1")
    title.grid(row=0, column=0, columnspan=2, pady=10)

    subtitle = Label(center_frame, text="Model Master", font=("Georgia", 20, "bold"), bg="#d6eaf8")
    subtitle.grid(row=1, column=0, columnspan=2, pady=10)

    labels = [
        "Model Code", "Model Name", "Model Type", "Ex-Showroom Price",
        "RTO Charges", "Insurance", "Accessory", "Model Tax", "Total Price"
    ]

    entries = []

    # ---------- Create Labels & Entries ----------
    for i, text in enumerate(labels):
        Label(center_frame, text=text, font=("Segoe UI", 12), bg="#d6eaf8").grid(row=i+2, column=0, pady=5, sticky=E)
        ent = Entry(center_frame, font=("Segoe UI", 12), width=40)
        ent.grid(row=i+2, column=1, pady=5, padx=10)
        entries.append(ent)

    txtmcode, txtmname, txtmtype, txtmprice, txtrto, txtins, txtacc, txtmtax, txttotal = entries

    txtmprice.bind("<KeyRelease>", cal)
    txtrto.bind("<KeyRelease>", cal)
    txtins.bind("<KeyRelease>", cal)
    txtacc.bind("<KeyRelease>", cal)
    txtmtax.bind("<KeyRelease>", cal)

    # ---------- BUTTONS ROW ----------
    btn_frame = Frame(center_frame, bg="#d6eaf8")
    btn_frame.grid(row=20, column=0, columnspan=2, pady=20)

    buttons = [
        ("ADD", maxrec),
        ("SAVE", saverec),
        ("SEARCH", serrec),
        ("UPDATE", uprec),
        ("DELETE", delrec),
        ("CLOSE", model_win.destroy),
    ]

    for i, (text, cmd) in enumerate(buttons):
        Button(btn_frame, text=text, command=cmd, width=12,
               font=("Segoe UI", 10, "bold"), bg="#0d47a1", fg="white").grid(row=0, column=i, padx=5)

    # Default load next ID
    maxrec()