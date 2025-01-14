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
        return (amount_owing)

class PdfReport:
    """
    Generates a report for flatmates with the amount they
    owe for a given period.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass

the_bill = Bill(amount=120, period="December 2024")
mary = Flatmate(name="Mary", days_in_house=27)
john = Flatmate(name="John", days_in_house=29)

print(f"John will pay: {round(john.pays(bill=the_bill, flatmate=mary), 2)}")
print(f"Mary will pay: {mary.pays(bill=the_bill, flatmate=john)}")