import streamlit as st
import tools
from tools.fetch_stock_info import Anazlyze_stock

st.title("Stock Analysis bot")
st.write("This bot scraps and gathers real time stock realted information and analyzes it using LLM")

query = st.text_input('Input your investment related query:') 

Enter=st.button("Enter")
clear=st.button("Clear")

if clear:
    print(clear)
    st.markdown(' ')

if Enter:
    import time
    with st.spinner('Gathering all required information and analyzing. Be patient!!!!!'):
        out=Anazlyze_stock(query)
    st.success('Done!')
    st.write(out)


