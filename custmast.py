from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
import mysql.connector


def open_custmast():

    cust_win = Toplevel()
    cust_win.title("Customer Master Window")
    cust_win.state("zoomed")  # FULLSCREEN
    cust_win.configure(bg="#e3f2fd")

    # ---------------- DATABASE FUNCTIONS ---------------- #

    def clsfields():
        txtcname.delete(0, END)
        txtcadd.delete(0, END)
        txtcity.delete(0, END)
        txtcontact.delete(0, END)
        txtemail.delete(0, END)
        txtpan.delete(0, END)

    def maxrec():
        mydb = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="twsps"
        )
        mycur = mydb.cursor()

        mycur.execute("SELECT MAX(cno) FROM custmast")
        data = mycur.fetchone()

        mx = data[0] + 1 if data[0] else 1

        txtcno.delete(0, END)
        txtcno.insert(0, str(mx))

        clsfields()

    def saverec():

        s1 = txtcno.get()
        s2 = txtcname.get()
        s3 = txtcadd.get()
        s4 = txtcity.get()
        s5 = txtcontact.get()
        s6 = txtemail.get()
        s7 = txtpan.get()

        if not all([s2, s3, s4, s5, s6, s7]):
            messagebox.showwarning("Warning", "All fields required")
            return

        mydb = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="twsps"
        )

        cur = mydb.cursor()

        cur.execute(
            "INSERT INTO custmast VALUES(%s,%s,%s,%s,%s,%s,%s)",
            (s1, s2, s3, s4, s5, s6, s7)
        )

        mydb.commit()

        messagebox.showinfo("Success", "Record Saved Successfully")

        maxrec()

    def serrec():

        clsfields()

        s1 = askstring("Search", "Enter Customer No")

        if not s1:
            return

        mydb = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="twsps"
        )

        cur = mydb.cursor()

        cur.execute("SELECT * FROM custmast WHERE cno=%s", (s1,))
        data = cur.fetchone()

        if not data:
            messagebox.showinfo("Info", "Record Not Found")
            return

        txtcno.delete(0, END)
        txtcno.insert(0, data[0])
        txtcname.insert(0, data[1])
        txtcadd.insert(0, data[2])
        txtcity.insert(0, data[3])
        txtcontact.insert(0, data[4])
        txtemail.insert(0, data[5])
        txtpan.insert(0, data[6])

    def uprec():

        s1 = txtcno.get()
        s2 = txtcname.get()
        s3 = txtcadd.get()
        s4 = txtcity.get()
        s5 = txtcontact.get()
        s6 = txtemail.get()
        s7 = txtpan.get()

        mydb = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="twsps"
        )

        cur = mydb.cursor()

        cur.execute(
            """UPDATE custmast 
            SET cname=%s,cadd=%s,city=%s,contact=%s,email=%s,panno=%s
            WHERE cno=%s""",
            (s2, s3, s4, s5, s6, s7, s1)
        )

        mydb.commit()

        messagebox.showinfo("Updated", "Record Updated")

        maxrec()

    def delrec():

        s1 = txtcno.get()

        if messagebox.askyesno("Confirm", "Delete this record?"):

            mydb = mysql.connector.connect(
                user="root",
                password="",
                host="localhost",
                database="twsps"
            )

            cur = mydb.cursor()

            cur.execute("DELETE FROM custmast WHERE cno=%s", (s1,))
            mydb.commit()

            messagebox.showinfo("Deleted", "Record Deleted")

            maxrec()

    # ---------------- UI DESIGN ---------------- #

    title_font = ("Georgia", 24, "bold")
    label_font = ("Segoe UI", 12)
    btn_font = ("Segoe UI", 11, "bold")

    # CENTER CONTAINER
    main_frame = Frame(cust_win, bg="#e3f2fd")
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    # TITLE
    Label(main_frame,
          text="Two Wheeler Sale Purchase System",
          font=("Georgia", 26, "bold"),
          bg="#e3f2fd",
          fg="#0d47a1").grid(row=0, column=0, columnspan=2, pady=10)

    Label(main_frame,
          text="Customer Master",
          font=("Georgia", 20, "bold"),
          bg="#e3f2fd").grid(row=1, column=0, columnspan=2, pady=10)

    # FORM LABELS + ENTRIES

    Label(main_frame, text="Customer No", font=label_font,
          bg="#e3f2fd").grid(row=2, column=0, sticky="e", pady=6)

    txtcno = Entry(main_frame, width=35, font=label_font)
    txtcno.grid(row=2, column=1, pady=6)

    Label(main_frame, text="Customer Name", font=label_font,
          bg="#e3f2fd").grid(row=3, column=0, sticky="e", pady=6)

    txtcname = Entry(main_frame, width=35, font=label_font)
    txtcname.grid(row=3, column=1, pady=6)

    Label(main_frame, text="Address", font=label_font,
          bg="#e3f2fd").grid(row=4, column=0, sticky="e", pady=6)

    txtcadd = Entry(main_frame, width=35, font=label_font)
    txtcadd.grid(row=4, column=1, pady=6)

    Label(main_frame, text="City", font=label_font,
          bg="#e3f2fd").grid(row=5, column=0, sticky="e", pady=6)

    txtcity = Entry(main_frame, width=35, font=label_font)
    txtcity.grid(row=5, column=1, pady=6)

    Label(main_frame, text="Contact No", font=label_font,
          bg="#e3f2fd").grid(row=6, column=0, sticky="e", pady=6)

    txtcontact = Entry(main_frame, width=35, font=label_font)
    txtcontact.grid(row=6, column=1, pady=6)

    Label(main_frame, text="Email ID", font=label_font,
          bg="#e3f2fd").grid(row=7, column=0, sticky="e", pady=6)

    txtemail = Entry(main_frame, width=35, font=label_font)
    txtemail.grid(row=7, column=1, pady=6)

    Label(main_frame, text="PAN No", font=label_font,
          bg="#e3f2fd").grid(row=8, column=0, sticky="e", pady=6)

    txtpan = Entry(main_frame, width=35, font=label_font)
    txtpan.grid(row=8, column=1, pady=6)

    # BUTTON FRAME

    btn_frame = Frame(main_frame, bg="#e3f2fd")
    btn_frame.grid(row=9, column=0, columnspan=2, pady=20)

    Button(btn_frame, text="ADD", width=10, font=btn_font,
           bg="#03a9f4", command=maxrec).grid(row=0, column=0, padx=5)

    Button(btn_frame, text="SAVE", width=10, font=btn_font,
           bg="#03a9f4", command=saverec).grid(row=0, column=1, padx=5)

    Button(btn_frame, text="SEARCH", width=10, font=btn_font,
           bg="#03a9f4", command=serrec).grid(row=0, column=2, padx=5)

    Button(btn_frame, text="UPDATE", width=10, font=btn_font,
           bg="#03a9f4", command=uprec).grid(row=0, column=3, padx=5)

    Button(btn_frame, text="DELETE", width=10, font=btn_font,
           bg="#03a9f4", command=delrec).grid(row=0, column=4, padx=5)

    Button(btn_frame, text="CLOSE", width=10, font=btn_font,
           bg="#f44336", fg="white",
           command=cust_win.destroy).grid(row=0, column=5, padx=5)