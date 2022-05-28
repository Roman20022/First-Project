class Client:
    def __init__(self,name,balans,creditBalans,passport):
        self.name = name
        self.balansOwnFunds = balans
        self.balansCreditFunds = creditBalans
        self.passport = passport
    def addOwnFunds(self, money):
        self.balansOwnFunds =+ money
    def addCreditFunds(self, money):
        self.balansCreditFunds =+ money
account1 = Client("Bob",1000,300,8970665028)
print(account1.name)
print(account1.balansOwnFunds)
print(account1.balansCreditFunds)
print(account1.passport)