<<<<<<< Updated upstream
import streamlit  as st 

st.write("MONKEY")
franksButton =st.button("Frank Buttom")
=======
import streamlit as st

st.title("Welcome to Campus Care")

with st.form(customerInfo_form):
    email = st.text_input(label = "Email")
    passWord = st.text_input(label = "Password", type = "password")
    name = st.text_input(label = "Enter your name (Optional)")
    submitButton = st.button("Submit")
st.write("HI EHTAN")
>>>>>>> Stashed changes
