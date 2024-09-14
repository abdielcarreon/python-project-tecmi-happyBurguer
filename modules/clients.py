import sqlite3

class Client:
    def __init__(self):
        self.conn = sqlite3.connect('happy_burguer.db')
        self.c = self.conn.cursor()
        
    def add_client(self, clave, name, address, email, tel):
        """Adding new client"""
        self.c.execute("INSERT INTO clients(clave, name, address, email, tel) VALUES(?, ?, ?, ?, ?)", (clave, name, address, email, tel,))
        self.conn.commit()
        print("Client added.")
        
    def delete_client(self, clave):
        """Delete client"""
        self.c.execute("DELETE FROM clients WHERE clave=?", (clave))
        self.conn.commit()
        print("Client deleted.")
    
    def update_client(self, clave, name=None, address=None, email=None, tel=None):
        """Update client data"""
        if name:
            self.c.execute("UPDATE clients SET name=? WHERE clave=?", (name, clave,))
        if address:
            self.c.execute("UPDATE clients SET address=? WHERE clave=?", (address, clave,))
        if email:
            self.c.execute("UPDATE clients SET email=? WHERE clave=?", (email, clave,))
        if tel:
            self.c.execute("UPDATE clients SET tel=? WHERE clave=?", (tel, clave,))
        self.conn.commit()
        print("Client Updated")
        
    def get_clients(self):
        """Get client data"""
        self.c.execute("SELECT * FROM clients")
        return self.c.fetchall()
    
    def exist_client(self, name):
        """Verify client by name"""
        self.c.execute("SELECT 1 FROM clients WHERE name=?", (name,))
        return self.c.fetchone() is not None
        



