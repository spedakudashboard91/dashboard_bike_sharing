# dashboard_bike_sharing
Dashboard Analisis Data Sepeda
Proyek ini adalah dashboard analisis data sepeda menggunakan Streamlit. Dashboard ini menampilkan data sepeda berdasarkan hari dan jam.
Install Streamlit: First, you need to install Streamlit in your Colab environment. Run the following command:

!pip install streamlit

Create Your Streamlit App: Write your Streamlit app code into a file named app.py. You can use the following command to create the file:

%%writefile app.py
import streamlit as st
st.title("Dashboard Analisis Penyewaan Sepeda")
st.write("Selamat datang di dashboard penyewaan sepeda!")

Install Localtunnel: To expose your Streamlit app to the internet, you can use Localtunnel. Install it using:
!npm install -g localtunnel

Run the Streamlit App: Use the following command to run your Streamlit app and expose it using Localtunnel:
!streamlit run app.py & npx localtunnel --port 8501
