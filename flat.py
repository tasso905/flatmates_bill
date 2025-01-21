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