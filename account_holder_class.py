# Create an AccountHolderDetails class with attributes name, address, age,
class AccountHolderDetails:


    # initialising the class with account holder details, saved as __detail for security
    def __init__(self,name, address, age):
        self.__name = name
        self.__address = address
        self.__age = age



    #using getters and setters to change / display account details
    @property
    def account_holder(self):
        # getting account details 
        return self.__name, self.__address, self.__age
    

    # setting / changing account details
    @account_holder.setter
    def account_holder(self,name,address,age):
        self.__name = name
        self.__address = address
        self.__age = age

    # deleting account
    @account_holder.deleter
    def account_holder(self):
        del self.__name, self.__address, self.__age
    
# Inherit Account holder class into MyAccount


# Create a class called MyAccount which represents a bank account, 
# having as attributes: accountNumber (numeric type), balance.

# Create a constructor () method? with parameters: accountNumber, balance.

# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details.

# Create manageAccount class and import everything from BankAccount class
# call all methods in manageAccount class that have are available from parent class

# Create a display() method to display account details.

# Create a README.md for your docu