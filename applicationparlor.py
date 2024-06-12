import sqlite3

class IceCreamParlor:
    def __init__(self, db_name='ice_cream_parlor.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_flavor(self, name, ingredients):
        self.cursor.execute('INSERT INTO seasonal_flavors (name, ingredients) VALUES (?, ?)', (name, ingredients))
        self.conn.commit()

    def add_ingredient(self, name, quantity):
        self.cursor.execute('INSERT INTO ingredients (name, quantity) VALUES (?, ?)', (name, quantity))
        self.conn.commit()

    def add_suggestion(self, flavor, suggestion, allergens):
        self.cursor.execute('INSERT INTO customer_suggestions (flavor, suggestion, allergens) VALUES (?, ?, ?)', (flavor, suggestion, allergens))
        self.conn.commit()

    def add_allergen(self, name):
        self.cursor.execute('INSERT INTO allergens (name) VALUES (?)', (name,))
        self.conn.commit()

    def search_flavors(self, keyword):
        self.cursor.execute('SELECT * FROM seasonal_flavors WHERE name LIKE ?', ('%' + keyword + '%',))
        return self.cursor.fetchall()

    def add_to_cart(self, flavor_id, quantity):
        self.cursor.execute('INSERT INTO cart (flavor_id, quantity) VALUES (?, ?)', (flavor_id, quantity))
        self.conn.commit()

    def view_cart(self):
        self.cursor.execute('''
            SELECT seasonal_flavors.name, cart.quantity 
            FROM cart 
            JOIN seasonal_flavors ON cart.flavor_id = seasonal_flavors.id
        ''')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

# Example Usage
parlor = IceCreamParlor()
parlor.add_flavor('Strawberry', 'Strawberries, Sugar, Milk')
parlor.add_ingredient('Sugar', 100)
parlor.add_suggestion('Mango', 'More mango chunks', 'None







