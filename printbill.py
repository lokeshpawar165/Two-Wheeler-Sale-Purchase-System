from tkinter import messagebox


def print_bill(txtbno, txtbdate, txtcno, txtmcode,
               txtengineno, txtchassisno, txtbatteryno,
               txtcolor, txttotal, txtremark):
    
    
    from fpdf import FPDF
    import os
    
    # Read widget values directly
    bno = txtbno.get()
    bdate = txtbdate.get()
    cust = txtcno.get()
    model = txtmcode.get()
    engno = txtengineno.get()
    chsno = txtchassisno.get()
    bat = txtbatteryno.get()
    clr = txtcolor.get()
    pr = txttotal.get()
    rem = txtremark.get()

    if bno == "":
        messagebox.showwarning("Warning", "Bill No Missing")
        return
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Company heading
    logo_path = os.path.join(os.getcwd(), "twsps_logo.png")
    if os.path.exists(logo_path):
        pdf.image(logo_path, x=10, y=8, w=30)

    pdf.set_xy(45,10)
    pdf.set_font("Arial","B",20)
    pdf.cell(135,10,"LOKESH WHEELS",ln=True,align="C")

    pdf.set_x(45)
    pdf.set_font("Arial", size=14)
    pdf.cell(120,6,"Authorized Two Wheeler Dealer",ln=True)

    pdf.ln(12)

    pdf.set_font("Arial","B",16)
    pdf.cell(0,10,"Bill Receipt",ln=True,align="C")
    pdf.ln(5)

    pdf.set_font("Arial", size=11)
    pdf.cell(0,8,f"Bill No   : {bno}",ln=True)
    pdf.cell(0,8,f"Bill Date : {bdate}",ln=True)

    pdf.ln(5)
    pdf.set_font("Arial","B",12)
    pdf.cell(0,8,"Customer Details",ln=True)

    pdf.set_font("Arial", size=11)
    pdf.cell(0,8,f"Customer : {cust}",ln=True)

    pdf.ln(4)
    pdf.set_font("Arial","B",12)
    pdf.cell(0,8,"Vehicle Details",ln=True)

    pdf.set_font("Arial", size=11)
    pdf.cell(0,8,f"Model       : {model}",ln=True)
    pdf.cell(0,8,f"Engine No   : {engno}",ln=True)
    pdf.cell(0,8,f"Chassis No  : {chsno}",ln=True)
    pdf.cell(0,8,f"Battery No  : {bat}",ln=True)
    pdf.cell(0,8,f"Color       : {clr}",ln=True)

    pdf.ln(5)
    pdf.set_font("Arial","B",12)
    pdf.cell(0,8,f"Total Amount : Rs. {pr}",ln=True)

    pdf.ln(3)
    pdf.set_font("Arial", size=11)
    pdf.cell(0,8,f"Remark : {rem}",ln=True)

    pdf.ln(15)
    pdf.set_font("Arial","I",10)
    pdf.cell(0,10,"Thank You For Your Purchase!",align="C")

    filename = f"Bill_{bno}.pdf"
    pdf.output(filename)
    os.startfile(filename)