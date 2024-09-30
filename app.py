import streamlit as st
import pandas as pd  # Tambahkan impor pandas

st.title('Streamlit Simple App')

page = st.sidebar.radio("Pilih halaman", ["Dataset", "Visualisasi"])

if page == "Dataset":
    st.header("Halaman Dataset")
    data = pd.read_csv("pddikti_example.csv")
    st.write(data)

elif page == "Visualisasi":  # Pastikan ini sama dengan pilihan yang ada di radio
    st.header("Halaman Visualisasi")
    # Tambahkan konten untuk visualisasi di sini
