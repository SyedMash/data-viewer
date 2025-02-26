import streamlit as st
import pandas as pd

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Data Preview")
    st.write(df.head())
    
    st.subheader("Data Summary")
    st.write(df.describe())
    
    st.subheader("Filter Data")
    col = df.columns.to_list()
    selected_col = st.selectbox("Select a column to filter by", col)
    unique_values = df[selected_col].unique()
    selected_value = st.selectbox("Select a value", unique_values)
    
    filtered_df = df[df[selected_col] == selected_value]
    st.write(filtered_df)
    
    st.subheader("Plot Data")
    x_col = st.selectbox("Select x-axis column", col)
    y_col = st.selectbox("Select y-axis column", col)
    
    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_col)[y_col])
    else:
        st.write("Waiting on file upload.")