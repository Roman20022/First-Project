class Client:
    def __init__(self,name,balans,creditBalans,passport):
        self.__name = name
        self.__balansOwnFunds = balans
        self.__balansCreditFunds = creditBalans
        self.__passport = passport
    def addOwnFunds(self, money):
        self.balansOwnFunds =+ money
    def addCreditFunds(self, money):
        self.balansCreditFunds =+ money
    # def printProtecrionData(self):
    #     print(self._name, self._balansOwnFunds,self._balansCreditFunds,self._passport)



    def __printPrivatData(self):
        print(self.__name, self.__balansOwnFunds,self.__balansCreditFunds,self.__passport)

account1 = Client("Bob", 1000, 300, 8970665028)
account1.addOwnFunds(1000)
account1._Client__printPrivatData()
# print.printProtecrionData()
# print(account1.__name)
# print(account1.__balansOwnFunds)
# print(account1.__balansCreditFunds)
# print(account1.__passport)