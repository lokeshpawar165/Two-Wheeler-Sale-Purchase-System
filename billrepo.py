# Project ui structure : Create a Customer Entry Form using Tkinter with fields Billmast (Bill Master ) for model info:  bno, bdate, cno, mcode, engineno, chassisno, batteryno, color, price, remark Include buttons for ADD, SAVE, SEARCH, UPDATE, DELETE and Exit.
def open_billreport():
    from fpdf import FPDF
    from datetime import datetime
    import mysql.connector
    import os

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="twsps"
    )
    mycur = mydb.cursor()
    mycur.execute("SELECT * FROM billmast ORDER BY bno")
    sdata = mycur.fetchall()

    if not sdata:
        print("No data found")
        mydb.close()
        return

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # ---------- HEADER ----------
    if os.path.exists("twsps_logo.png"):
        pdf.image("twsps_logo.png", x=10, y=8, w=25)

    pdf.set_xy(40, 10)
    pdf.set_font("Arial", "B", 18)
    pdf.cell(130, 10, "LOKESH WHEELS", ln=True, align="C")

    pdf.set_x(40)
    pdf.set_font("Arial", size=12)
    pdf.cell(130, 6, "Authorized Two Wheeler Dealer", ln=True, align="C")

    pdf.ln(8)

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 6, f"Report Date : {datetime.now().strftime('%d-%m-%Y')}", ln=True)
    pdf.cell(0, 6, f"Total Records : {len(sdata)}", ln=True)

    pdf.ln(5)

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 8, "Vehicle Bill Information", ln=True, align="C")

    pdf.ln(4)

    # ---------- TABLE HEADER ----------
    pdf.set_font("Arial", "B", 9)

    headers = [
        "Bill No", "Bill Date", "Cust No", "Model",
        "Engine No", "Chassis No", "Battery No",
        "Color", "Price"
    ]

    widths = [15, 22, 18, 15, 30, 30, 25, 20, 20]

    for i in range(len(headers)):
        pdf.cell(widths[i], 8, headers[i], 1, 0, "C")
    pdf.ln()

    # ---------- TABLE DATA ----------
    pdf.set_font("Arial", size=9)

    for row in sdata:
        pdf.cell(widths[0], 8, str(row[0]), 1, 0, "C")
        pdf.cell(widths[1], 8, str(row[1]), 1, 0, "C")
        pdf.cell(widths[2], 8, str(row[2]), 1, 0, "C")
        pdf.cell(widths[3], 8, str(row[3]), 1, 0, "L")
        pdf.cell(widths[4], 8, str(row[4]), 1, 0, "L")
        pdf.cell(widths[5], 8, str(row[5]), 1, 0, "L")
        pdf.cell(widths[6], 8, str(row[6]), 1, 0, "L")
        pdf.cell(widths[7], 8, str(row[7]), 1, 0, "C")
        pdf.cell(widths[8], 8, str(row[8]), 1, 0, "R")
        pdf.ln()

    # ---------- SAVE & OPEN ----------
    filename = "billreport.pdf"
    pdf.output(filename)

    mydb.close()
    os.startfile(filename)
