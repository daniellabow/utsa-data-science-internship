from datetime import date, datetime


class Bank:
    def __init__(self, firstname, lastname, birthdate):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate  # format: 'YYYY-MM-DD'
        self.mailing_address = None
        self.email_address = f"{firstname.lower()}.{lastname.lower()}@gmail.com"
        self.username = self.email_address
        self.password = None
        self.bank_balance = 1000
        self.net_worth = None

    def deposit_money(self, amount):
        self.bank_balance += amount

    def withdraw_money(self, amount):
        if amount <= self.bank_balance:
            self.bank_balance -= amount

    def get_age(self):
        bday = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        return (today - bday).days

    def get_networth(self):
        return self.bank_balance

    def __str__(self):
        return f"{self.firstname} {self.lastname}: ${self.bank_balance}"

    def __eq__(self, other):
        return self.username == other.username

    def __le__(self, other):
        return self.bank_balance <= other.bank_balance

    def __ge__(self, other):
        return self.bank_balance >= other.bank_balance


class Credit_Card(Bank):
    def __init__(self, firstname, lastname, birthdate, issue_date, expiration_date, card_balance=1000, ):
        super().__init__(firstname, lastname, birthdate)
        self.issue_date = issue_date
        self.expiration_date = expiration_date
        self.card_balance = card_balance

    def get_networth(self):
        return self.bank_balance - self.card_balance

#dummy data for output
customer1 = Bank("John", "Doe", datetime.date(1990, 1, 1))

#use functions
customer1.deposit_money