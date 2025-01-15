from fpdf import FPDF


class Bill:
    """
    Object that contains the amount of a bill for a given
    period.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Object that contains the name, days in the house and
    amount a flatmate owes.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
    def pays(self, bill, flatmate):
        weight = self.days_in_house/(self.days_in_house + flatmate.days_in_house)
        amount_owing=bill.amount * weight
        return (round(amount_owing, 2))

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

        #insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align='C', ln=1)

        #insert period label and value
        pdf.cell(w=150, h=40, txt="Period: ", border=1)
        pdf.cell(w=200, h=40, txt=bill.period, border=1, ln=1)

        #insert name and amount due for first flatmate
        pdf.cell(w=150, h=40, txt=f"{flatmate1.name}: ", border=1)
        pdf.cell(w=200, h=40, txt=str(flatmate1.pays(bill, flatmate2)), border=1, ln=1)

        #insert name and amount due for second flatmate
        pdf.cell(w=150, h=40, txt=f"{flatmate2.name}: ", border=1)
        pdf.cell(w=200, h=40, txt=str(flatmate2.pays(bill, flatmate1)), border=1, ln=1)

        #write to pdf file
        pdf.output(self.filename)

the_bill = Bill(amount=120, period="December 2024")
mary = Flatmate(name="Mary", days_in_house=27)
john = Flatmate(name="John", days_in_house=29)

print(f"John will pay: {round(john.pays(bill=the_bill, flatmate=mary), 2)}")
print(f"Mary will pay: {round(mary.pays(bill=the_bill, flatmate=john), 2)}")

pdf_report = PdfReport(filename="report_1.pdf")
pdf_report.generate(flatmate1=mary, flatmate2=john, bill=the_bill)

