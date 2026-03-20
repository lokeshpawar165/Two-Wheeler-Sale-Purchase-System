def open_modelreport():
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
    mycur.execute("SELECT * FROM modelmast ORDER BY mcode")
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
    pdf.cell(0, 8, "Vehicle Model Information", ln=True, align="C")

    pdf.ln(4)

    # ---------- TABLE HEADER ----------
    pdf.set_font("Arial", "B", 10)
    headers = ["Code", "Model Name", "Type", "Price", "RTO", "Ins", "Acc", "Tax", "Total"]
    widths = [12, 40, 18, 20, 18, 18, 18, 18, 20]

    for i in range(len(headers)):
        pdf.cell(widths[i], 8, headers[i], 1, 0, "C")
    pdf.ln()

    # ---------- TABLE DATA ----------
    pdf.set_font("Arial", size=9)

    for row in sdata:
        for i in range(9):
            pdf.cell(widths[i], 8, str(row[i]), 1, 0, "C")
        pdf.ln()

    # ---------- SAVE & OPEN ----------
    filename = "modelreport.pdf"
    pdf.output(filename)

    mydb.close()
    os.startfile(filename)
