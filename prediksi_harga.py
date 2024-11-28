import pickle
import streamlit as st
import pandas as pd
import numpy as np
import os

model_path = os.path.join(os.getcwd(), "prediksi_harga_mobil.sav")
model = pickle.load(open(model_path, 'rb'))

st.title("Prediksi Harga Mobil")

st.header("Dataset")
df1 = pd.read_csv("CarPrice.csv")  
st.dataframe(df1)

st.write("Grafik Highwaympg")
chart_highwaympg = pd.DataFrame(df1, columns=["highwaympg"])
st.line_chart(chart_highwaympg)

st.write("Grafik Curbweight")
chart_curbweight = pd.DataFrame(df1, columns=["curbweight"])
st.line_chart(chart_curbweight)

st.write("Grafik Horsepower")
chart_horsepower = pd.DataFrame(df1, columns=["horsepower"])
st.line_chart(chart_horsepower)

st.write("Masukkan Nilai Variabel Independen:")
highwaympg = st.number_input("Highway-mpg", min_value=0, max_value=100, value=25)
curbweight = st.number_input("Curbweight", min_value=0, max_value=5000, value=2500)
horsepower = st.number_input("Horsepower", min_value=0, max_value=1000, value=150)

if st.button("Prediksi"):
    try:
        car_prediction = model.predict([[highwaympg, curbweight, horsepower]])
        
        harga_mobil = float(car_prediction[0])
        harga_mobil_formatted = f"${harga_mobil:,.2f}"  
        
        st.success(f"Harga mobil diprediksi: {harga_mobil_formatted}")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
