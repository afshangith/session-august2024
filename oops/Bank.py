class Bank():

    def getroi(self):
        return 10;


class BankOfAmerica(Bank):

    def getroi(self):
        return 8;

class ChaseBank(Bank):

    def getroi(self):
        return 7;

bank = Bank()
print(bank.getroi())

b = BankOfAmerica()
print(b.getroi())

c = ChaseBank()
print(c.getroi())




