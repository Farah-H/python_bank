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
    