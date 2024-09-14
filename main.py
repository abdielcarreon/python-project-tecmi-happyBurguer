
from modules._init_ import Client,  Menu, Orders 

import db


def show_menu():
    
    print("\n--- Main Menu ---")
    print("1. Orders")
    print("2. Clients")
    print("3. Menu")
    print("4. Exit")
 
 
def select_option():
     while True:
         show_menu()
         option = input("Choose one option: ")
         if option == '1':
             manage_orders()
         elif option == '2':
             manage_clients()
         elif option == '3':
             manage_menu()
         elif option == '4':
             print("Leaving program...")
             break
         
         else:
            print("Not valid option, try it again")
    
def manage_orders():
    order_manager = Orders()
    client_manager = Client()
    menu_manager = Menu()
    while True:
        print("\n--- Orders Manager ---")
        print("1. Create order")
        print("2. Delete Order")
        print("3. Show actual orders")
        print("4. Create ticket")
        print("5. Return main menu back")
        option = input("Choose one option: ")
        
        if option == '1':
            try:
                order_id = int(input("Order ID: "))
                client = input("Client Name: ").strip()
                if not client_manager.exist_client(client):
                    raise ValueError("Isn't exist client.")
                product = input("Product Name: ").strip()
                if not menu_manager.exist_product(product):
                    raise ValueError("Isn't exist  product.")
                price = float(input("price: "))
                if not client or not product:
                     raise ValueError("Client and Product must has information.")
                order_manager.add_order(order_id, client, product, price)
            except ValueError as e:
                print(f"Error: {e}")
        elif option == '2':
            try:
                order_id = int(input("Order ID: "))
                order_manager.callOff_order(order_id)
            except ValueError as e:
                print("Order ID not valid.")
        elif option == '3':
            orders = order_manager.get_order()
            if orders:
                for order in orders:
                    print(order)
                    
            else:
                print("There aren't orders.")
                
        elif option == '4':
            try:
                order_id = int(input("Order ID: "))
                order = order_manager.getOrderById(order_id)
                if order:
                    order_manager.create_ticket(order_id, order[1], order[2], order[3])
                else:
                    print("Order not found.")
            except ValueError as e:
                print("Order ID not valid.")
        elif option == '5':
            break
        else:
            print("Invalid Option, try it again")

def manage_clients():
    client_manager = Client()
    while True:
        print("\n--- Clients Manager ---")
        print("1. Add client")
        print("2. Delete client")
        print("3. Update client")
        print("4. Show actual client")
        print("5. Return main menu back")
        option = input("Choose one option: ")
        if option == '1':
            clave = input("Client Key: ").strip()
            name = input("Client Name: ").strip()
            address = input("Client Address: ").strip()
            email = input("Client Email: ").strip()
            tel = input("Client Tel: ").strip()
            if clave and name and address and email and tel:
                client_manager.add_client(clave, name, address, email, tel)
            else:
                print("All fields are required.")
        elif option == '2':
            clave = input("Client key: ").strip()
            if clave:
                client_manager.delete_client(clave)
            else:
                print("Client Key must has information.")
        elif option == '3':
            clave = input("Client key: ").strip()
            if clave:
                name = input("New Name: ").strip()
                address = input("New Address").strip()
                email = input("New Email: ").strip()
                tel = input("New Tel").strip()
                client_manager.update_client(clave, name, address, email, tel)
            else:
                print("Client Key must has information.")
        elif option == '4':
            clients = client_manager.get_clients()
            if clients:
                for client in clients:
                    print(client)
            else:
                print("There aren't clients.")
        elif option == '5':
            break
        else:
            print("Not valid option, try it again")
            
def manage_menu():
    menu_manager = Menu()
    while True:
        print("\n--- Menu Manager ---")
        print("1. Add product")
        print("2. Delete product")
        print("3. Update product")
        print("4. Show menu products")
        print("5. Return main menu back")
        option = input("Choose one option: ")
        if option == '1':
            clave = input('Product Key: ').strip()
            name = input("Name: ").strip()
            try:
                price = float(input("Price: "))
                if clave and name:
                    menu_manager.add_product(clave, name, price)
                else:
                    print("Clave and name are required.")
            except ValueError:
                print("Price not valid.")
        elif option == '2':
            clave = input("Key Product: ").strip()
            if clave:
                menu_manager.delete_product(clave)
            else:
                print("Key Product must has information.")
        elif option == '3':
            clave = input("Key Product: ").strip()
            if clave:
                name = input("New Name: ").strip()
                price = input("New Price: ").strip()
                price = float(price) if price else None
                menu_manager.update_product(clave, name, price)
            else:
                print("Key Product must has information.")
        elif option =='4':
            products = menu_manager.get_products()
            if products:
                for product in products:
                    print(product)
            else:
                print("There aren't products")
        elif option == '5':
            break
        else:
            print('Not valid option, try it again.')
            
# if __name__ == '__main__':
db.create_tables()
select_option()
                


        
                    
        
    
            
                

        
             
         
    
    
    
