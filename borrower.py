import random


class Borrower():
    used_ids = set()
    def __init__(self, BorrowerName, EmailAddress=None,):
        """
        Constructor to initialize the Borrower object.
        Generates a unique Borrower ID and sets email_address to 'Unknown' if not provided.
        """

        self.__BorrowerName = BorrowerName
        self.__EmailAddress = EmailAddress
        self.__BorrowerID = self.generate_unique_id()
        self.__ItemsOnLoan = []
        
    @classmethod
    def generate_unique_id(cls):
        """Generates a unique Borrower ID."""
        while True:
            new_id = random.randint(10000, 99999)  # Random ID between 10000 and 99999
            if new_id not in cls.used_ids:  # Ensure the ID is not already used
                cls.used_ids.add(new_id)
                return new_id


    def getBorrowerName(self):
        return self.__BorrowerName
    
    def setBorrowerName(self, name):
        self.__BorrowerName = name
    
    def getEmailAddress(self):
        return self.__EmailAddress
    
    def setEmailAddress(self, email):
        self.__EmailAddress = email
    
    def getBorrowerID(self):
        return self.__BorrowerID
    
    def getItemsOnLoan(self):
        # self.__ItemsOnLoan.append(item)
        return self.__ItemsOnLoan.copy()
        
        
    def borrow_item(self, item):
        self.__ItemsOnLoan.append(item)
        item.setLoan(True)



    def return_item(self, item):
        """Removes an item from the list of items on loan, if it exists."""
        if item in self.__ItemsOnLoan:
            self.__ItemsOnLoan.remove(item)
            item.setLoan(False)
        else:
            print(f"Item '{item}' not found in the list of items on loan.")
            
    def print_details(self):
        print(f"Borrower Name: {self.__BorrowerName}")
        print(f"Email Address: {self.__EmailAddress}")
        print(f"Borrower ID: {self.__BorrowerID}")
        print(f"Items on Loan: {', '.join(map(str, self.__ItemsOnLoan)) if self.__ItemsOnLoan else 'No items on loan'}")
