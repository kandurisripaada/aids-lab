
print("Welcome to the ABC Bank")



class Bank:

   def __init__(self):

       self.bal = 10000

       self.c = 0

   def options(self):

       print("********")

       print("1. Deposit")

       print("2. Withdraw")

       print("3. Balance Enquiry")

       print("0. Exit")

       op = int(input("Enter the option: "))

       match op:

           case 1:

               self.deposit()

               obj.options()

           case 2:

               self.c=self.c+1

               self.withdraw()

               if self.c>=3:

                   print("transaction limit completed")

                   exit()

               obj.options()

           case 3:

               self.balance()

               obj.options()

           case 0:

               self.exit()



   def valid(self):

       i = 3

       j = 0

       while i > 0:

           pin = int(input("Enter PIN: "))

           if pin == 1234:

               i = 0

               self.options()

           else:

               i -= 1

               j += 1

               print("Invalid PIN")

               if j == 3:

                   print("Card is blocked")

                   break



   def deposit(self):

       amt = int(input("Enter the amount to deposit: "))

       if amt >= 100 and (amt%100)==0:

           self.bal += amt

           print(f"Deposited successfully. New balance: {self.bal}")

       elif amt>50000:

           print("invalid amount. Maximum deposit is <50K")

       else:

           print("Invalid amount. Minimum deposit is 100.")



   def withdraw(self):

       amt = int(input("Enter the amount to withdraw: "))

       if amt > self.bal:

           print("Insufficient balance")

       elif amt%100!=0:

           print("unable to withdraw")

       elif amt>20000:

           print("maximum limit is 20K")

       elif amt<100:

           print("minimum withdraw should ne >100")

       else:

           self.bal -= amt

           if(self.bal<500):

               print("Minimum Balance should be maintained")

           else:

               print(f"Withdrawal successful. New balance: {self.bal}")



   def balance(self):
        print(f"Available balance is: {self.bal}")
   def exit(self):
        print("Exited the transaction.")

obj = Bank()

obj.valid()