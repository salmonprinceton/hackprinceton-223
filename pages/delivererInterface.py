import datetime as dt
import pandas as pd
import streamlit as st
from data_structure import ds

ethan = ds.ClientInfo(1, 1, "", "2025151224", "Forbes College A166")
satan = ds.ClientInfo(2, 2, "satan@hell.com", "66666666666", "The Underworld")
impostor = ds.ClientInfo(3, 3, "redimpostor@sussybaka.net", "", "Outer Space")

client_list = [ethan, satan, impostor, satan, ethan]

<<<<<<< Updated upstream

class Product:
    def __init__(self, product_id = 0, name = ""):
        self.product_id = product_id
        self.name = name

product_list = [Product(0, "Levonorgestrel (Plan B)"), Product(1, "Condoms"), Product(2, "Tampons"),
Product(3, "Sacrificial Lamb"),]

class OrderItem:
    def __init__(self, product = Product(), amount = 0):
        self.product = product
        self.amount = amount

# implements order
class Order:
    def __init__(self, order_id = 0, client_id = ClientInfo(), items = [OrderItem()], date_ordered = "", status = "", date_completed = ""):
        self.order_id = order_id
        self.client_info = client_id
        self.items = items
        self.date_ordered = date_ordered
        self.status = status
        self.date_completed = date_completed

    def make_string(self):
        output = ""
        for i in range(0, len(self.items)):
            output += str(self.items[i].amount) + " " + self.items[i].product.name
            if i < len(self.items) - 1:
                output += ", "
        return output
=======
product_list = [ds.Product(0, "Levonorgestrel (Plan B)"), ds.Product(1, "Condoms"), ds.Product(2, "Tampons"),
ds.Product(3, "Sacrificial Lamb"),]
>>>>>>> Stashed changes

order_item_list = {
    0: [ds.OrderItem(product_list[1], 2), ds.OrderItem(product_list[2], 1)],
    1: [ds.OrderItem(product_list[1], 666)],
    2: [ds.OrderItem(product_list[0], 1), ds.OrderItem(product_list[1], 1), ds.OrderItem(product_list[2], 1)],
    3: [ds.OrderItem(product_list[3], 100)],
    4: [ds.OrderItem(product_list[0], 1)],
}
<<<<<<< Updated upstream
=======
order_list = [ds.Order(i, client_list[i], order_item_list[i]) for i in range(0, len(client_list))]
>>>>>>> Stashed changes

date_list = ["09/26/04 12:00", "12/66/66 66:66", "05/05/05", "05/05/05", "05/05/05"]
order_list = [Order(i, client_list[i], order_item_list[i], date_list[i], "Processed") for i in range(0, len(client_list))]

# initializing session state if it doesn't already exist
for order in order_list:
    name = "Order " + str(order.order_id) + " "

    if name + "Date" not in st.session_state:
        st.session_state[name + "Date"] = ""
    if name + "Status" not in st.session_state:
        st.session_state[name + "Status"] = order.status

order_id_modify = st.number_input("Order ID to change", 0)
order_status_modify = st.selectbox("Order Status", ["Processed", "Delivering", "Completed"])
submit_button = st.button("Change order status")

if submit_button:
    name = "Order " + str(order_id_modify)
    if name + " Status" in st.session_state:
        order_list[order_id_modify].status = order_status_modify
        st.session_state[name + " Status"] = order_status_modify
        if order_status_modify == "Completed":
            datestr = dt.datetime.now().strftime("%y/%m/%d %H:%M")
            order_list[order_id_modify].date_completed = datestr
            st.session_state[name + " Date"] = datestr


    

df = pd.DataFrame(
    {
        "Order ID": [order.order_id for order in order_list],
        "Email": [order.client_info.email for order in order_list],
        "Phone Number": [order.client_info.phone for order in order_list],
        "Location": [order.client_info.location for order in order_list],
        "Order" : [order.make_string() for order in order_list],
        "Date Placed" : [order.date_ordered for order in order_list],
        "Status" : [st.session_state["Order " + str(i) + " Status"] for i in range(0, len(order_list))],
        "Date Completed" : [st.session_state["Order " + str(i) + " Date"] for i in range(0, len(order_list))],
    }
)

# print(dt.datetime.now().strftime("%y/%m/%d %H:%M"))

st.dataframe(df)
print(st.session_state["Order 0 Status"] + "alpha")

<<<<<<< Updated upstream
=======
def update_table():
    global df
    df = pd.DataFrame(
    {
        "Order ID": [order.order_id for order in order_list],
        "Email": [order.client_info.email for order in order_list],
        "Phone Number": [order.client_info.phone for order in order_list],
        "Location": [order.client_info.location for order in order_list],
        "Order" : [order.make_string() for order in order_list],
        "Status" : [status for status in status_list]
    }
)

def ohio():
    st.title("No!!!!!!!!!!!!!!!")
    # global status_list
    # status_list = ["Arrived", "Processed", "Delivering", "Delivering", "Arrived"]
    # update_table()

st.button("Go to Ohio", on_click = ohio)
>>>>>>> Stashed changes
