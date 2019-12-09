import sys
#from pyspark.sql import SparkSession
#spark = SparkSession.builder.appName("Test Apps1").getOrCreate()
#df=spark.read.csv("Cricket.csv",header=True)



class Account(object):

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)

    def deposit(self,amount):
        if amount > 0 :
            self.balance = self.balance+amount

    def withdraw(self,amount):
        if 0 < amount <= self.balance :
            self.balance = self.balance - amount
        else :
            print("insufficient balance")

    def show_balance(self):
        print("the current balance is {}".format(self.balance))


if __name__ =="__main__":
    vij=Account("Tim",0)
    vij.show_balance()
    vij.withdraw(19)
    vij.deposit(100)
    vij.show_balance()
    vij.deposit(20)
    vij.show_balance()
    vij.withdraw(110)
    vij.show_balance()

