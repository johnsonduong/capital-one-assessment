class Transaction:
    def __init__(self, date, merchant_code, amount_cents):
        self.date = date
        self.merchant_code = merchant_code
        self.amount_cents = amount_cents

class Rule:
    def __init__(self, points, requirements):
        self.points = points
        self.requirements = requirements