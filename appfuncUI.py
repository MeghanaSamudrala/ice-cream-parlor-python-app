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

def main():
    parlor = IceCreamParlor()
    
    while True:
        print("\nWelcome to the Ice Cream Parlor!")
        print("1. Add Seasonal Flavor")
        print("2. Add Ingredient")
        print("3. Add Customer Suggestion")
        print("4. Add Allergen")
        print("5. Search Flavors")
        print("6. Add to Cart")
        print("7. View Cart")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter flavor name: ")
            ingredients = input("Enter ingredients: ")
            parlor.add_flavor(name, ingredients)
            print("Flavor added!")
        
        elif choice == '2':
            name = input("Enter ingredient name: ")
            quantity = int(input("Enter quantity: "))
            parlor.add_ingredient(name, quantity)
            print("Ingredient added!")
        
        elif choice == '3':
            flavor = input("Enter suggested flavor: ")
            suggestion = input("Enter suggestion: ")
            allergens = input("Enter allergens (if any): ")
            parlor.add_suggestion(flavor, suggestion, allergens)
            print("Suggestion added!")
        
        elif choice == '4':
            name = input("Enter allergen name: ")
            parlor.add_allergen(name)
            print("Allergen added!")
        
        elif choice == '5':
            keyword = input("Enter search keyword: ")
            results = parlor.search_flavors(keyword)
            print("Search results:")
            for result in results:
                print(result)
        
        elif choice == '6':
            flavor_id = int(input("Enter flavor ID to add to cart: "))
            quantity = int(input("Enter quantity: "))
            parlor.add_to_cart(flavor_id, quantity)
            print("Added to cart!")
        
        elif choice == '7':
            cart_items = parlor.view_cart()
            print("Your cart:")
            for item in cart_items:
                print(f"Flavor: {item[0]}, Quantity: {item[1]}")
        
        elif choice == '8':
            parlor.close()
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
