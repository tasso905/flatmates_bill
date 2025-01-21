from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input("Please enter a bill amount: $"))
period = input("What is the bill period? (e.g. December 2020): ")
name_1 = input("What is your name? ")
days_in_house_1 = int(input(f"How many days did {name_1} stay in the house during the bill period? "))
name_2 = input("What is your flatmate's name? ")
days_in_house_2 = int(input(f"How many days did {name_2} stay in the house during the bill period? "))

the_bill = Bill(amount, period)
flatmate_1 = Flatmate(name_1, days_in_house_1)
flatmate_2 = Flatmate(name_2, days_in_house_2)

print(f"{flatmate_1.name} will pay: {round(flatmate_1.pays(the_bill, flatmate_2), 2)}")
print(f"{flatmate_2.name} will pay: {round(flatmate_2.pays(the_bill, flatmate_1), 2)}")

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate_1, flatmate_2, the_bill)

