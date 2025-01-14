# flatmates_bill

**Description:** An application that will get an input for a bill amount for a particular period and the days that each flatmate has stayed in the house for that given period.  It will then return how much each flatmate owes (has to pay). Also, it will generate a PDF report with the flatmates name, period and how much each owes.

**Objects-->** Bill:
                    amount
                    period
                Flatmate:
                    name
                    days_in_house
                    pays (bill)
                Report (PDF):
                    filename
                    generate (save)(flatmate1, flatmate2, bill)

**Formula to calculate amount owing:**
        flatmate_1 = 27 days
        flatmate_2 = 29 days
        bill_amount = 120

        flatmate_1:

        calc_factor: 27/27+29 = 0.482
        amount_owes = 120 * 0.482 = 57.84

        flatmate_2:

        calc_factor: 29/29+27 = 0.518
        amount_owes = 120 * 0.518 = 62.16



