from datetime import datetime
class BankAccount:

    def __init__(self, first_name, last_name,  bank, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        self.bank = bank
        self.phone_number = phone_number
        self.deposits = []
        self.withdrawals = []
        self.loan = 0
        self.pay_loan = 0

    def account_name(self):
        name= "{} account for {} {} {}".format(self.bank, self.first_name,self.second_name, self.phone_number)
        return name

    def deposit(self, amount):
        try:
            amount + 1
            except TypeError:
                print("The amount should be numbers")
                return
        if amount <= 0:
            try:
                amount + 1
                except TypeError:
                    print("The amount should be in numbers")
                    return
                    deposit=self.deposits.append(amount)
                    print("You have to deposit a higher amount")
        else:
            self.balance += amount
            time = datetime.now()
            get_time = time.strftime("%H:%M%p , %d/%m/%Y")
            deposit = {
                "time": "time",
                "amount" : "amount"
            }
            print("Dear {} ,you have deposited {} at {}.Your current balance is {}".format(self.account_name(),amount,get_time,self.balance))

        if amount <= 0:
            print("You cannot deposit zero or negative")
        else:
            self.balance += amount
            print("You have deposited {} to {}".format(amount, self.account_name()))

    def withdraw(self,amount):
        try:
            amount + 1
        except TypeError:
            print("The amount should be in numbers")
            return
        if amount <= 0:
            

            deposit=self.withdrawals.append(deposit)
            print("You have to withdraw a positive amount")
        elif amount > self.balance:
            print("You don't have enough balance to make the transition")
        else:
            self.balance -= amount
            time = datetime.now()
            get_time = time.strftime("%H:%M%p ,  %d/%m/%Y")
            deposit = {
                "time": "time",
                "amount" : "amount"
            }
            print("Dear {} you have withdrawn {} at {} .Your current balance is {}".format(self.account_name(),amount,get_time,self.balance))

    def get_balance(self):
        time = datetime.now()
        get_time = time.strftime("%H:%M%p ,  %d/%m/%Y")
        return "The balance for {} is {} at".format(self.account_name(), self.balance,get_time)
        
    def deposit_statements(self):
        for deposit in self.deposits:
            time = datetime.now()
            get_time = time.strftime("%H:%M%p  , %d/%m/%Y")
            print("{} at {}".format(deposit(),get_time))
      
    def withdrawal_statements(self):
        for withdraw in self.withdrawals:
            time = datetime.now()
            get_time = time.strftime("%H:%M%p , ++ %d/%m/%Y")
            print("{} at {}".format(withdraw(),get_time))

    def request_loan(self,amount):
        try:
            amount + 1
        except TypeError:
            print("The amount should be numbers")
            return
        if amount <= 0:

            try:
                amount + 1
            except TypeError:
                print("The amount should be numbers")
                return

        
            print("you cannot withdraw a negative value")
        else:
            self.loan = amount
            time = datetime.now()
            get_time = time.strftime("%H:%M%p  %d/%m/%Y")
            print("you have been granted a loan of shillings {} at {}".format(amount,get_time))   
    def repay_loan(self,amount):
        try:
            amount + 1
        except TypeError:
            print("The amount should be numbers")
            return
        if amount <= 0:
            print("you cannot repay a negative amount.Kindly top up")
        elif self.loan == 0:
            print("you do not have an existing loan")
        elif amount > self.loan:
            print("your loan is {}, please enter a amount that is less or equal to your loan".format(self.loan))
        else:
            self.loan -= amount
            self.repay = self.loan - amount
            time = datetime.now()
            get_time = time.strftime("%H:%M%p  %d/%m/%Y")
            print("you have repaid your loan with this {}, your existing balance is {} at {}".format(amount,self.loan,get_time))
class BankAccount(Account):
    def __init__(self,first_name,last_name,phone_number,bank);
    self.bank=bank
    super().__init__(first_name,last_name,phone_number)


class MobileMoneyAccount(account):
 def__init__(self,first_name,last_name,phone_number,service_provider):
    self.service_provider= service_provider
    self.airtime=[]
    self.pay_bills=[]
    self.send_money=[]
    self.recieve_money[]
    
    super().__init__(first_name,last_name,phone_number)

def  buy_airtime(self,amount);
    try:
       amount+1
    expect TypeError:
        print("Please enter the amount in digits")
    return

   if amount>self.balance:
       print("You have insufficient balance to make this request")
  else:
      self.balance<=amount
      time=datetime.now() 
      airtime={
          "time":time,
          "airtime":amount
      }    
      self.airtime.append(airtime)
      print("You have bought airtime worth{} on {}".format (amount,self.get_formated_time(time)))

 def pay_bills(self,amount):
        try:
            amount+1
        expect TypeError:
            print("Please enter the amount in figures")
            return
    
    if amount>self.balance:
        print("You have insufficient balance to make this request")
    else:
        self.balance<=amount
        time=datetime.now()   
        pay_bills{
            "time":time,
            "pay_bills":amount
        }
        self.pay_bills.append(pay_bills)
        print("You have successfully paid your bills worth {} on {}".format (amount,get_formated_time(time)))


def send_money(self,amount):
    try:
        amount+1
        expect TypeError:
        print("Enter the amount in figures")
        return

        if amount>self.balance:
            print("You have insufficient balance to make the transaction")

        else:
            self.balance>=amount
            time=datetime.now()
            send_money{
                "time":time,
                "send_money":amount
            }
            self.send_money.append(send_money)
            print("You have successfully transfered {} from your account on {}. Your new balance is {}".format (amount,get_formated_time(time),self.balance))


def recieve_money(self,amount):
    time=datetime.now()
    recieve_money{
        "time":time,
        "recieve_money":amount
    }
    self.recieve_money.append(recieve_money)
    print("You have recieved {} on {} your new balance is {}".format(amount,get_formated_time(time),self.balance))