# orders.py
import sqlite3

class Orders:
    def __init__(self):
        self.conn = sqlite3.connect('happy_burguer.db')
        self.c = self.conn.cursor()
        
    def add_order(self, order_id, client, product, price):
        """Adding new order"""
        self.c.execute("INSERT INTO orders(order_id, client, product, price) VALUES (?, ?, ?, ?)", (order_id, client, product, price,))
        self.conn.commit()
        print("order added.")
        self.create_ticket(order_id, client, product, price)
        
    def callOff_order(self, order_id):
        """Call off order"""
        self.c.execute("DELETE FROM orders WHERE order_id=?", (order_id,))
        self.conn.commit()
        print("Order deleted.")
    
    def get_order(self):
        """Get all orders"""
        self.c.execute("SELECT * FROM orders")
        return self.c.fetchall()
        
    def getOrderById(self, order_id):
        """Get order by ID"""
        self.c.execute("SELECT * FROM orders WHERE order_id=?", (order_id,))
        return self.c.fetchone()
    
    def create_ticket(self, order_id, client, product, price):
        """Create ticket over txt file"""
        with open(f"ticket_{order_id}.txt", "w") as f:
            f.write(f"Order ticket\n")
            f.write(f"Order ID: {order_id}\n")
            f.write(f"Client: {client}\n")
            f.write(f"Product: {product}\n")
            f.write(f"Price: {price}\n")
        print(f"Ticket: ticket_{order_id}.txt")
        