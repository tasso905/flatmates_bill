from fpdf import FPDF
import webbrowser
import os

class PdfReport:
    """
    Generates a report for flatmates with the amount they
    owe for a given period.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        
        #initialize PDF object.
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #add icon/image
        pdf.image("files/house.png", w=35, h=35)

        #insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align='C', ln=1)

        #insert period label and value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=150, h=40, txt="Period: ", border=0)
        pdf.cell(w=200, h=40, txt=bill.period, border=0, ln=1)

        #insert name and amount due for first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=150, h=25, txt=f"{flatmate1.name}: ", border=0)
        pdf.cell(w=200, h=25, txt=str(flatmate1.pays(bill, flatmate2)), border=0, ln=1)

        #insert name and amount due for second flatmate
        pdf.cell(w=150, h=25, txt=f"{flatmate2.name}: ", border=0)
        pdf.cell(w=200, h=25, txt=str(flatmate2.pays(bill, flatmate1)), border=0, ln=1)

        #write to pdf file
        pdf.output(f"files/{self.filename}")
        webbrowser.open('file://'+os.path.realpath(f"files/{self.filename}"))
