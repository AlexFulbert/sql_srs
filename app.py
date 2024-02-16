import pandas as pd
import streamlit as st
import duckdb

st.write("#SQL SRS - Spaced Repetition System SQL practice")
option = st.selectbox('What would you like to review', ('Joins', 'GroupBy', 'Windows Functions'), index=None, placeholder="Select option")
st.write(f"You selected {option}")

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)
tab1, _ = st.tabs(['h', ''])

with tab1:
    sql_query = st.text_area(label='text')
    try:
        result = duckdb.sql(sql_query).df()
        st.write(f" La query {sql_query}")
        st.dataframe(result)
        # Do something with the result
    except Exception as e:
        print("An error occurred:", e)
