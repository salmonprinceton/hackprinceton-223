import datetime as dt
import pandas as pd
import streamlit as st
import requests
import json

order_url = 'http://10.24.106.64:5000/order_data'
response = requests.get(order_url)
order_data = response.json()
delivery_url = 'http://10.24.106.64:5000/delivery_data'
delivery_response = requests.get(delivery_url)
delivery_list = delivery_response.json()

# initializing session state if it doesn't already exist
for delivery in delivery_list:
    name = "Order " + str(delivery.Order_ID) + " "

    if name + "Date" not in st.session_state:
        st.session_state[name + "Date"] = ""
    if name + "Status" not in st.session_state:
        st.session_state[name + "Status"] = delivery.status

isDeliverer = True

if isDeliverer:
    Order_ID = st.number_input("Order ID to change", 0)
    dt = dt.datetime.now()
    dt_str = dt.strftime("%Y-%m-%d %H:%M:%S")
    completed_date = json.dumps(dt_str)
    status = st.selectbox("Order Status", ["Processed", "Delivering", "Completed"])
    submit_button = st.button("Change order status")

    df = pd.DataFrame(order_data)
    st.dataframe(df)
else:
    st.write("GET YOUR GOOFY ASS OUT OF HERE!!!!")

delivery_url = 'http://10.24.106.64:5000/delivery_data'
delivery_data = {'Order_ID': Order_ID,
                 'completed_date': completed_date,
                 'status': status
                 }

headers = {'Content-Type': 'application/json'}

if submit_button:
    response = requests.post(delivery_url, json=delivery_data, headers=headers)

    print(response.text)
