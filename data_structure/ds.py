class User:
    def __init__(self, user_id = 0, name = "", email = "", password = "", is_deliverer = False):
        self.user_id = user_id
        self.name = user_id
        self.email = email
        self.password = password
        self.is_deliverer = is_deliverer

class Order:
    def __init__(self, order_id = 0, user = User(), product = "", date_ordered = "", quantity = 0, location = ""):
        self.order_id = order_id
        self.user = user
        self.product = product
        self.date_ordered = date_ordered
        self.quantity = quantity
        self.location = location

    def make_string(self):
        return self.product + " " + str(self.quantity)

class Delivery:
    def __init__(self, status = "", date_completed = "", order = Order()):
        self.status = ""
        self.date_completed = ""
        self.order = order
