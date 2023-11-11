import streamlit as st

st.title("Welcome to Campus Care")

with st.form("customerInfo_form"):
    email = st.text_input(label = "Email")
    passWord = st.text_input(label = "Password", type = "password")
    name = st.text_input(label = "Enter your name (Optional)")
    
    st.write("Are you a deliverer?")
    isDeliver = st.checkbox(label = "Yes")
    notDeliver = st.checkbox(label = "No")

    submitButton = st.form_submit_button(label = "Enter")

st.button("Place Order")

st.button("Show Order History")

with st.form("placingOrder_form"):
    product = st.selectbox(
        'What would you like to order?',
        ('Pads', 'Tampons', 'Condoms', 'Female Condoms', 'Birth Control Pills (Plan B)'))
    productAmount = st.number_input(label = "Insert the amount of the product needed:", min_value = 1, max_value = 10)
    submitButton = st.form_submit_button(label = "Confirm Choices")

st.button("Done With Purchase")

st.button("Do More Shopping")