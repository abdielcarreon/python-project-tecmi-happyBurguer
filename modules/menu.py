
import sqlite3

class Menu:
    def __init__(self):
        self.conn = sqlite3.connect('happy_burguer.db')
        self.c = self.conn.cursor()
        
    def add_product(self, clave, name, price):
        """Adding new product on menu"""
        self.c.execute("INSERT INTO menu(clave, name, price) VALUES (?, ?, ?)", (clave, name, price,))
        self.conn.commit()
        print("Product added.")
        
    def delete_product(self, clave):
        """Delete product of menu"""
        self.c.execute("DELETE FROM menu WHERE clave=?", (clave,))
        self.conn.commit()
        print("Product deleted.")
    
    def update_product(self, clave, name=None, price=None):
        """Update product data"""
        if name:
            self.c.execute("UPDATE menu SET name=? WHERE clave=?", (name, clave,))
        if price:
            self.c.execute("UPDATE menu SET price=? WHERE clave=?", (price, clave,))
        self.conn.commit()
        print("Product Updated")
        
    def get_products(self):
        """Get product data"""
        self.c.execute("SELECT * FROM menu")
        return self.c.fetchall()
    
    def exist_product(self, name):
        """Verify product by name"""
        self.c.execute("SELECT 1 FROM menu WHERE name=?", (name,))
        return self.c.fetchone() is not None
        
