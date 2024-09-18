menu = {
    'food': ['Sandwich - 2 Euro', 'Pasta - 2 Euro', 'Poha - 2 Euro', 'French Fries - 2 Euro', 'Nuggets - 2 Euro', 'Veg Burger - 2 Euro'],
    'drinks': ['Coffee  - 5 Euro', 'Tea - 3 Euro', 'Coke - 2 Euro'],
    'books': ['Harry Potter', 'Book B', 'Book C']
}

def BookDeliveryService():
    print("Books Options:")
    for x in menu['books']:
        print(x)
    Booked_name = input("Enter Your name: ")
    book_name = input("Enter Your Book Name: ")
    address = input("Enter Your address: ")
    print(f"hi {Booked_name} , we will deliver {book_name} to your Address:{address}")
    

def employee_login():
    password = "admin123"
    attempt = input("Enter employee password: ")

    if attempt == password:
        print("Login successful!")
        employee_options()
    else:
        print("Incorrect password! Access denied.")

def employee_options():
    print("\nEmployee Options:")
    print("1. View Customer Details")
    print("2. Modify Food Menu")
    print("3. Modify Book Menu")
    
    k = input("Enter the option: ")
    
    if k == "1":
        print("Customer Details:")
        print("Prachi")
        print("Kavya")
        print("Anu")
        print("Roman")
    
    elif k == "2":
        print("Current Food Menu:")
        print(menu["food"])
        j = input("Enter 1 : Add Item \nEnter 2 : Delete Item ")
        
        if j == "1":
            item_name = input("Enter the name of the new item: ")
            price = input("Enter the price of the new item: ")
            menu['food'].append(f"{item_name} - {price} Euro")
            print('Item added successfully!')
            print("Updated Food Menu:", menu['food'])
        
        elif j == "2":
            print("Current Food Menu:", menu['food'])
            food_del = input("Enter the name of the item to delete: ")
            for item in menu['food']:
                if food_del in item:
                    menu['food'].remove(item)
                    print(f"Item '{food_del}' deleted successfully!")
                    break
            else:
                print(f"Item '{food_del}' not found in the menu.")            
            print("Updated Food Menu:", menu['food'])
        else:
            print("Invalid input.")
    
    elif k == "3":
        print("Current Book Menu:", menu['books'])
        h = input("Enter 1 to Add Book, 2 to Delete Book: ")
        
        if h == "1":
            book_name = input("Enter the name of the new book: ")

            menu['books'].append(book_name)
            print('Book added successfully!')
            print("Updated Book Menu:", menu['books'])
        
        elif h == "2":
            book_del = input("Enter the name of the book to delete: ")
            if book_del in menu['books']:
                menu['books'].remove(book_del)
                print(f"Book '{book_del}' deleted successfully!")
            else:
                print(f"Book '{book_del}' not found in the menu.")
            
            print("Updated Book Menu:", menu['books'])
        else:
            print("Invalid input.")

def customer_order():
    print("\nWelcome to the Bookshop and Cafe!")
    print("\nMenu Options:")
    
    print("\nFood Options:")
    for x in menu['food']:
        print(x)
    
    Foodchoosen = input("\nPlease choose a food item: ")
    print(f"\nThanks for choosing {Foodchoosen}!")
    response = input("Would you like to choose anything else? (yes/no): ").strip().lower()
    if response == 'yes':
        print("\nHere are more options:")
        for y in menu['food']:
            print(y)
        Foodchoosen = input("\nPlease choose another item: ")
        print(f"\nThanks for choosing {Foodchoosen}!")
    else:

        print("Please select your drink:")
        for drink in menu['drinks']:
            print(drink)
        drink_choice = input("\nPlease choose a drink: ")
        print(f"\nThanks for choosing {drink_choice}!")
    
    print("\nYour order has been placed!")


import datetime
def WelcomeBookshop():

    while True:
        print("\nWelcome to PARK Book Cafe")
        print(datetime.datetime.now())
        print("1. Customer Order")
        print("2. Employee Login")
        print("3. Book Delivery Service")
        print("4. Exit")

        option = input("\nEnter your choice: ")

        if option == "1":
            customer_order()  
        elif option == "2":
            employee_login()
        elif option == "3":
           BookDeliveryService() 
        elif option == "4":
            print("Goodbye!")
            exit() 
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    WelcomeBookshop()
