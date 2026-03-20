# Username : admin
# Password : admin

from tkinter import *
from tkinter import messagebox
from PIL import Image as PILImage
from PIL import ImageTk

# -------- IMPORT MODULES ----------
from custmast import open_custmast
from modelmast import open_modelmast
from billmast import open_billmast

from custrepo import open_custreport
from modelrepo import open_modelreport
from billrepo import open_billreport


# ================= MAIN UI =================
def main_ui():

    win = Toplevel()
    win.title("Two Wheeler Sale Purchase System")
    win.state("zoomed")
    win.configure(bg="#e3f2fd")

    # ---------- FONTS ----------
    title_font = ("Georgia", 26, "bold")
    section_font = ("Georgia", 15, "bold")
    btn_font = ("Segoe UI", 12, "bold")

    # ---------- LOGO ----------
    logo_img = PILImage.open("twsps_logo.png")
    logo_img = logo_img.resize((130, 130))
    logo = ImageTk.PhotoImage(logo_img)

    Label(win, image=logo, bg="#e3f2fd").pack(pady=10)
    win.logo = logo

    # ---------- TITLE ----------
    Label(win,
          text="Two Wheeler Sale Purchase System",
          font=title_font,
          bg="#e3f2fd",
          fg="#0d47a1").pack(pady=5)

    # ---------- MAIN FRAME ----------
    main_frame = Frame(win, bg="#e3f2fd")
    main_frame.pack(pady=30)

    # ---------- MASTER FRAME ----------
    master_frame = LabelFrame(
        main_frame,
        text="Master Entry",
        font=section_font,
        bg="#e3f2fd",
        fg="#0d47a1",
        padx=30,
        pady=20
    )
    master_frame.grid(row=0, column=0, padx=40)

    # ---------- REPORT FRAME ----------
    report_frame = LabelFrame(
        main_frame,
        text="Reports",
        font=section_font,
        bg="#e3f2fd",
        fg="#1b5e20",
        padx=30,
        pady=20
    )
    report_frame.grid(row=0, column=1, padx=40)

    # ---------- BUTTON HOVER ----------
    def hover(btn, c1, c2):
        btn.bind("<Enter>", lambda e: btn.config(bg=c2))
        btn.bind("<Leave>", lambda e: btn.config(bg=c1))

    # ---------- MASTER BUTTONS ----------
    b1 = Button(master_frame, text="Customer Register",
                font=btn_font, width=22,
                bg="#ff7043", fg="white",
                command=open_custmast)
    b1.pack(pady=10)
    hover(b1, "#ff7043", "#ff5722")

    b2 = Button(master_frame, text="Model Catalogue",
                font=btn_font, width=22,
                bg="#ff7043", fg="white",
                command=open_modelmast)
    b2.pack(pady=10)
    hover(b2, "#ff7043", "#ff5722")

    b3 = Button(master_frame, text="Billing Desk",
                font=btn_font, width=22,
                bg="#ff7043", fg="white",
                command=open_billmast)
    b3.pack(pady=10)
    hover(b3, "#ff7043", "#ff5722")

    # ---------- REPORT BUTTONS ----------
    r1 = Button(report_frame, text="Customer Report's",
                font=btn_font, width=22,
                bg="#43a047", fg="white",
                command=open_custreport)
    r1.pack(pady=10)
    hover(r1, "#43a047", "#2e7d32")

    r2 = Button(report_frame, text="Model Report's",
                font=btn_font, width=22,
                bg="#43a047", fg="white",
                command=open_modelreport)
    r2.pack(pady=10)
    hover(r2, "#43a047", "#2e7d32")

    r3 = Button(report_frame, text="Bill Report's",
                font=btn_font, width=22,
                bg="#43a047", fg="white",
                command=open_billreport)
    r3.pack(pady=10)
    hover(r3, "#43a047", "#2e7d32")

    # ---------- EXIT BUTTON ----------
    exit_btn = Button(win,
                      text="EXIT",
                      font=btn_font,
                      width=22,
                      bg="#d32f2f",
                      fg="white",
                      command=win.destroy)
    exit_btn.pack(pady=25)
    hover(exit_btn, "#d32f2f", "#b71c1c")

    # ---------- STATUS BAR ----------
    status = Label(win,
                   text="Login Successful - Welcome Admin",
                   bd=1,
                   relief=SUNKEN,
                   anchor=W,
                   bg="#e3f2fd")
    status.pack(side=BOTTOM, fill=X)

    # ---------- SHORTCUT ----------
    win.bind("<Control-e>", lambda e: win.destroy())

    # ---------- FOOTER ----------
    Label(win,
          text="Developed by Lokesh Pawar | Two Wheeler Sale Purchase System",
          font=("Segoe UI", 9),
          bg="#e3f2fd",
          fg="gray").pack(side=BOTTOM, pady=5)


# ================= LOGIN FUNCTION =================
def login():

    if username.get() == "admin" and password.get() == "admin":

        # messagebox.showinfo("Success", "Login Successful!")

        login_win.withdraw()

        main_ui()

    else:

        messagebox.showerror("Login Failed", "Invalid Username or Password")


# ================= LOGIN WINDOW =================
login_win = Tk()
login_win.title("Login - TWSPS System")
login_win.state("zoomed")
login_win.configure(bg="#dbe9f6")

# ---------- LOGIN CARD ----------
card = Frame(login_win, bg="white")
card.place(relx=0.5, rely=0.5, anchor="center")

card.config(padx=40, pady=40)

# ---------- TITLE ----------
Label(card,
      text="LOGIN",
      font=("Georgia", 24, "bold"),
      bg="white",
      fg="#0d47a1").pack(pady=(0, 20))

# ---------- USERNAME ----------
Label(card,
      text="Username",
      font=("Segoe UI", 12),
      bg="white").pack(anchor="w")

username = Entry(card,
                 font=("Segoe UI", 12),
                 width=28)
username.insert(0, "admin")
username.pack(pady=5)

# ---------- PASSWORD ----------
Label(card,
      text="Password",
      font=("Segoe UI", 12),
      bg="white").pack(anchor="w")

password = Entry(card,
                 font=("Segoe UI", 12),
                 width=28,
                 show="*")
password.insert(0, "admin")
password.pack(pady=5)

# ---------- SHOW PASSWORD ----------
def toggle_password():

    if password.cget("show") == "*":

        password.config(show="")

        show_btn.config(text="Hide")

    else:

        password.config(show="*")

        show_btn.config(text="Show")


show_btn = Button(card,
                  text="Show",
                  font=("Segoe UI", 10),
                  bg="white",
                  relief=FLAT,
                  command=toggle_password)

show_btn.pack(pady=(0, 10), anchor="e")

# ---------- LOGIN BUTTON ----------
login_btn = Button(card,
                   text="LOGIN",
                   font=("Segoe UI", 12, "bold"),
                   bg="#43a047",
                   fg="white",
                   width=28,
                   pady=6,
                   command=login)

login_btn.pack(pady=10)

# ---------- FOOTER ----------
Label(login_win,
        text="Developed by Lokesh Pawar | Two Wheeler Sale Purchase System",
        font=("Segoe UI", 9),
        bg="#e3f2fd",
        fg="gray").pack(side=BOTTOM, pady=5)

login_win.mainloop()