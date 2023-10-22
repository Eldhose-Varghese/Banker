class BankAccount:
  def __init__(self,acc_no,name,amount):
    self.acc_no = acc_no
    self.name = name
    self.amount = amount
  def deposit(self,Deposit_amount):
    self.amount=self.amount+Deposit_amount
    print("Money Successfully added")
    self.display()
  def withdraw(self,withdraw_amount):
    if self.amount < withdraw_amount:
      print("The entered amount is not available in your account")
    else:
      self.amount = self.amount-withdraw_amount
      print("Money successfully withdrawn")
      self.display()
  def display(self):
    print(f'Account No. : {self.acc_no}')
    print(f'Account Holder : {self.name}')
    print(f'Amount : {self.amount}')
ev = BankAccount("SB-123","Eldhose",5000)
ev.display()
ev.deposit(3000)
ev.withdraw(2000)
ev.withdraw(10000)