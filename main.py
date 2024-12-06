from base import *
from borrower import *
from items import *
import datetime

class LibrarySystem:
    def __init__(self):
        self.borrowers = []
        self.items = []
    def add_borrower(self, name, email=None):
        borrower = Borrower(name, email)
        self.borrowers.append(borrower)
        print(f"Borrower {name} added with ID {borrower.getBorrowerID()}.")

    def remove_borrower(self, borrower_id):
        for borrower in self.borrowers:
            if borrower.getBorrowerID() == borrower_id:
                self.borrowers.remove(borrower)
                print(f"Borrower with ID {borrower_id} removed.")
                return
        print(f"Borrower with ID {borrower_id} not found.")

    def list_borrowers(self):
        if not self.borrowers:
            print("No borrowers in the system.")
        for borrower in self.borrowers:
            borrower.print_details()

    def borrow_item(self, borrower_id, item_name):
        for item in self.items:
            if item.ULR() == item_name:
                borrowed_item = item
                break
        else:
            print("Unkown ULR")
            return
        for borrower in self.borrowers:
            if borrower.getBorrowerID() == borrower_id:
                borrower.borrow_item(borrowed_item)
                duedate = datetime.date.today() - datetime.timedelta(days=30)
                borrowed_item.setDueDate(duedate)
                print("Return before", duedate)
                return
        print(f"Borrower with ID {borrower_id} not found.")

    def return_item(self, borrower_id, item_name):
        for item in self.items:
            if item.ULR() == item_name:
                borrowed_item = item
                break
        else:
            print("Unkown ULR")
            return
        for borrower in self.borrowers:
            if borrower.getBorrowerID() == borrower_id:
                duedate = borrowed_item.getDueDate()
                if duedate < datetime.date.today():
                    loop = True
                    while loop:
                        try:
                            print("Pay the fine.")
                            # pay 
                            input()
                            loop = False
                        except KeyboardInterrupt:
                            print("Cannot quit pay the fine.")
                    print("Thank you.")
                borrower.return_item(borrowed_item)
                return
        print(f"Borrower with ID {borrower_id} not found.")

    def print_all_details(self):
        print("\n--- All Borrower Details ---")
        if not self.borrowers:
            print("No borrowers in the system.")
        for borrower in self.borrowers:
            borrower.print_details()
            print("----------------------------")


# Menu-driven LMS system
def main():
    system = LibrarySystem()
    system.items = load_items_from_file()
    while True:
        print("\nLibrary Management System")
        print("1. Add Borrower")
        print("2. Remove Borrower")
        print("3. List Borrowers")
        print("4. Borrow Item")
        print("5. Return Item")
        print("6. Print All Details")
        print("7. New item in library")
        print("8. Change Attributes of items")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter borrower's name: ")
            email = input("Enter borrower's email (or leave blank): ")
            system.add_borrower(name, email if email.strip() else None)
        elif choice == "2":
            borrower_id = int(input("Enter borrower ID to remove: "))
            system.remove_borrower(borrower_id)
        elif choice == "3":
            system.list_borrowers()
        elif choice == "4":
            show_available(system.items)
            borrower_id = int(input("Enter borrower ID: "))
            item = input("Enter item to borrow: ")
            system.borrow_item(borrower_id, item)
        elif choice == "5":
            borrower_id = int(input("Enter borrower ID: "))
            item = input("Enter item to return: ")
            system.return_item(borrower_id, item)
        elif choice == "6":
            system.print_all_details()
        elif choice == "7":
            typeof = input("Type of item (CD[C] or Book[B]: ").strip().lower()
            title = input("Title of this item: ")
            maker = input("Author/Artist: ")
            if typeof == "c":
                newitem = CD(title, maker)
            elif typeof == "b":
                newitem = Book(title, maker)
            system.items.append(newitem)
            update_file(system.items)
        elif choice == "8":
            for i in system.items:
                print(i)
            item_name = input("Enter item ULR: ")
            for item in system.items:
                if item.ULR() == item_name:
                    target = item
                break
            change_attribute(target)
            update_file(system.items)
        elif choice == "9":
            update_file(system.items)
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()