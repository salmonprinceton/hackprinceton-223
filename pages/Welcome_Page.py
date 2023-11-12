import requests
import streamlit as st
import datetime as dt
import json

st.title("Welcome to Princeton Care Package")
if "Current User" not in st.session_state:
    st.session_state["Current User"] = ""
if "User Display" not in st.session_state:
    st.session_state["User Display"] = "Hello! Please create a new account or log in :)"
st.caption(st.session_state["User Display"])

with st.form("customerInfo_form"):
    email = st.text_input(label="Email")
    password = st.text_input(label="Password", type="password")
    name = st.text_input(label="Enter your name (Optional)")
    deliverer = st.radio(
        "Are you a deliverer?",
        ["Yes", "No"])

    deliverer = 1 if deliverer == "Yes" else 0

    submitButton = st.form_submit_button(label="Enter")

st.button("Show Order History")

with st.form("placingOrder_form"):
    dt = dt.datetime.now()
    dt_str = dt.strftime("%Y-%m-%d %H:%M:%S")
    order_date = json.dumps(dt_str)
    location = st.text_input(label="Enter Your Building and Entryway")
    product = st.selectbox(
        "What would you like to order?", ('Pads', 'Tampons', 'Plan B', 'Condoms', 'Female Condoms'))
    quantity = st.number_input(label="Insert the amount of the product needed:", min_value=1, max_value=10)
    submitOrder = st.form_submit_button(label="Submit Order")
st.header('Thank you for ordering!')

url = 'http://10.24.106.64:5000/data'
order_url = 'http://10.24.106.64:5000/order_data'
data = {'email': email,
        'password': password,
        'name': name,
        'deliverer': deliverer
        }

order_data = {'product': product,
              'location': location,
              'order_date': order_date,
              'quantity': quantity,
              }

headers = {'Content-Type': 'application/json'}

existing_login = {
    "ep0148@princeton.edu" : "baka"
}

if submitButton:
    response = requests.post(url, json=data, headers=headers)
    if email in existing_login:
        if existing_login[email] == password:
            st.session_state["Current User"] = email
            st.session_state["User Display"] = "Welcome back, " + email + "!"
        else:
            st.session_state["User Display"] = "The entered password is incorrect. Did you make a typo?"
    # print(response.text)
    else:
        existing_login[email] = password
        st.session_state["Current User"] = email
        st.session_state["User Display"] = "A new account was created for " + email + ". Welcome!~"
    st.rerun()


if submitOrder:
    order_response = requests.post(order_url, json=order_data, headers=headers)

    print(order_response.text)
