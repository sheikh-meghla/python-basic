class BankAccount:
    def __init__(self, Tk):
        self.__Tk = Tk

    def x(self, amount):
        self.__Tk = amount *2
       # self.__Tk +=amount
    def get_Tk(self):
        return self.__Tk

account = BankAccount(1000)
#account.x(500)
print(account.get_Tk())  

