class Product:
    def __init__(self,p_id,p_name,p_price,stock):
        self.p_id = p_id
        self.p_name = p_name
        self.p_price = p_price
        self.stock = stock

    def __str__(self):
        return f"Id: {self.p_id}, {self.p_name}, Stock: {self.stock}"

class Shopping:
    def __init__(self):
        self.cart = {}
    
    def add_item(self,i,s):
        if i.p_id not in self.cart:
            self.cart[i.p_id] = {'product' : i, 'quantity': s}
        
        if 0 < s <= i.stock:
            self.cart[i.p_id]['quantity'] += s
            i.stock -= s
            print(f"{i.p_name} has been added.")
        else:
            print("Out of Stock!!!")

    def remove_item(self,i,s):
        if i.p_id in self.cart and s > 0:
            if s <= self.cart[i.p_id]['quantity']:
                self.cart[i.p_id]['quantity'] -= s
                i.stock += s
                print(f"{s} {i.p_name}(s) removed from the cart.")
            else:
                print("Invalid quantity.")
            if self.cart[i.p_id]['quantity'] == 0:
                del self.cart[i.p_id]

        else:
            print(f"{i.p_name} not found in the cart.")

    def bill(self):
        if not self.cart:
            print("Cart is empty")
        else:
            amount = 0
            for i in self.cart.values():
                p = i['product'] 
                q = i['quantity']
                price = q*p.p_price
                amount += price
                print(f"{p.p_name}, Quantity: {q}, Price: ${price}")

            print("Total Amount:", amount)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.order_history = []

    def login(self, entered_password):
        return self.password == entered_password

    def view_order_history(self):
        for order in self.order_history:
            order.bill()
    
a =  Product(1, "Apples", 15, 100)
s = Product(2,"Soaps", 50, 25)
p = Product(3, "Plates", 150, 20)
u1 = User("Renu" , "Prashu@123")
if u1.login("Prashu@123"):
     shop = Shopping()
     shop.add_item(a,6)
     shop.add_item(p,2)
     shop.bill()
     shop.remove_item(p,1)
     u1.order_history.append(shop)
     u1.view_order_history()
else:
    print("Invalid Login")