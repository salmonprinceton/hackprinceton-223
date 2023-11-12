class ClientInfo:
    def __init__(self, client_id = 0, user_id = 0, email = "", phone = "", location = ""):
        self.client_id = client_id
        self.user_id = user_id
        self.email = email
        self.phone = phone
        self.location = location

class Product:
    def __init__(self, product_id = 0, name = ""):
        self.product_id = product_id
        self.name = name

class OrderItem:
    def __init__(self, product = Product(), amount = 0):
        self.product = product
        self.amount = amount

class Order:
    def __init__(self, order_id = 0, client_id = ClientInfo(), items = [OrderItem()]):
        self.order_id = order_id
        self.client_info = client_id
        self.items = items

    def make_string(self):
        output = ""
        for i in range(0, len(self.items)):
            output += str(self.items[i].amount) + " " + self.items[i].product.name
            if i < len(self.items) - 1:
                output += ", "
        return output
