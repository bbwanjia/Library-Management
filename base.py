from borrower import Borrower
from items import *
from datetime import date

# List to store library items (this simulates a database of items)
library_items = []

# Load items from the file (if it exists)
def load_items_from_file():
    library_items = []
    try:
        with open("library_items.txt", "r") as file:
            for line in file:
                data = line.strip().split("|")
                item_type, ULR, title, maker, loan_status, due_date = data
                loan_status = loan_status.lower() == "true"  # Convert "True"/"False" to boolean
                due_date = date.fromisoformat(due_date)  # Convert due date string to a date object
                
                # Create the appropriate item based on the flag (B for Book, C for CD)
                if item_type == "B":
                    item = Book(title, maker, ULR, loan_status, due_date)
                elif item_type == "C":
                    item = CD(title, maker, ULR, loan_status, due_date)
                else:
                    print(f"Unknown item type {item_type} for item {title}. Skipping.")
                    continue
                
                library_items.append(item)
    except FileNotFoundError:
        print("No previous library data found. Starting with an empty library.")
    return library_items

# Update the library_items file after changes
def update_file(library_items):
    with open("library_items.txt", "w") as file:
        for item in library_items:
            # Convert each item to a string representation with a flag (B or C for Book or CD)
            if isinstance(item, Book):
                item_type = "B"
            elif isinstance(item, CD):
                item_type = "C"
            else:
                continue  # Skip items that are not of type Book or CD

            # Write item details to the file
            item_data = f"{item_type}|{item.ULR()}|{item.getTitle()}|{item.getMaker()}|{item.isLoan()}|{item.getDueDate()}\n"
            file.write(item_data)


# Show all borrowed items
def show_borrowed():
    borrowed_items = [item for item in library_items if item.isLoan()]
    if borrowed_items:
        print("Borrowed items:")
        for item in borrowed_items:
            print(item)
    else:
        print("No items currently borrowed.")

# Show all available items
def show_available(library_items):
    available_items = [item for item in library_items if not item.isLoan()]
    if available_items:
        print("Available items:")
        for item in available_items:
            print(item)
    else:
        print("No items available for borrowing.")

# Change an item's attribute (allow librarian to modify attributes)
def change_attribute(item: LibraryItem):
    print(f"Current details for {item.getTitle()}:")
    print(item)
    
    # Prompt librarian for the attribute to change
    print("\nWhat would you like to change?")
    print("1. Title")
    print("2. Maker/Artist/Author")
    print("3. Loan Status")
    print("4. Due Date")
    choice = input("Enter the number of the attribute to change: ")

    if choice == "1":
        new_title = input("Enter the new title: ")
        item.setTitle(new_title)
    elif choice == "2":
        new_maker = input("Enter the new maker/author/artist: ")
        item.setMaker(new_maker)
    elif choice == "3":
        new_loan_status = input("Is it on loan? (yes/no): ").lower()
        if new_loan_status == 'yes':
            item.setLoan(True)
        elif new_loan_status == 'no':
            item.setLoan(False)
        else:
            print("Invalid input. Keeping the current loan status.")
    elif choice == "4":
        new_due_date_str = input("Enter the new due date (YYYY-MM-DD): ")
        new_due_date = date.fromisoformat(new_due_date_str)
        item.setDueDate(new_due_date)
    else:
        print("Invalid choice. No changes made.")
    
    print(f"Updated details: {item}")
    
    # Update the file after changes
