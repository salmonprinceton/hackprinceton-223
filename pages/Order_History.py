import datetime as dt
import pandas as pd
import streamlit as st
from data_structure import ds

ethan = ds.User(1, "", "ep0148@princeton.edu", "curiousSalmon2", False)
satan = ds.User(2, "Satan", "satan666@hell.com", "IHATEGOD666", False)
impostor = ds.User(3, "Red Impostor", "reallyred@sussybaka.net", "YOUARESUS", False)

user_list = [ethan, satan, impostor, satan, ethan]
product_list = ["Levonorgestrel (Plan B)", "Condoms", "Tampons", "Female Condoms", "Samsung Mega Capacity 31.5-cu ft Smart French Door Refrigerator with Dual Ice Maker (Fingerprint Resistant Stainless Steel) ENERGY STAR"]
date_list = ["09/26/2004 12:00:00", "09/26/2004 12:00:00", "09/26/2004 12:00:00", "09/26/2004 12:00:00", "09/26/2004 12:00:00"]
quantity_list = [1, 2, 3, 4, 5]
location_list = ["Forbes College A166", "Hell", "Outer Space", "Hell", "Forbes College A166"]

order_list = [ds.Order(i, user_list[i], product_list[i], date_list[i], quantity_list[i], location_list[i]) for i in range(0, len(user_list))]
delivery_list = [ds.Delivery("Processed", "", order_list[i]) for i in range(0, len(user_list))]

# initializing session state if it doesn't already exist
for delivery in delivery_list:
    name = "Order " + str(delivery.order.order_id) + " "

    if name + "Date" not in st.session_state:
        st.session_state[name + "Date"] = ""
    if name + "Status" not in st.session_state:
        st.session_state[name + "Status"] = delivery.status

df = pd.DataFrame(
        {
            "Order ID": [order.order_id for order in order_list],
            "Email": [order.user.email for order in order_list],
            "Location": [order.location for order in order_list],
            "Order" : [order.make_string() for order in order_list],
            "Date Placed" : [order.date_ordered for order in order_list],
            "Status" : [st.session_state["Order " + str(i) + " Status"] for i in range(0, len(order_list))],
            "Date Completed" : [st.session_state["Order " + str(i) + " Date"] for i in range(0, len(order_list))],
        }
    )
st.dataframe(df)