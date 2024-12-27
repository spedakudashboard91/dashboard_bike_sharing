
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache
def load_data():
    # Gantilah dengan path ke dataset Anda
    day_df = pd.read_csv('/content/drive/My Drive/Notebook/day_dataset.csv')  # Sesuaikan path sesuai kebutuhan
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    day_df['month'] = day_df['dteday'].dt.month
    day_df['year'] = day_df['dteday'].dt.year
    day_df['day_of_week'] = day_df['dteday'].dt.dayofweek
    day_df['is_weekend'] = day_df['day_of_week'].apply(lambda x: 1 if x >= 5 else 0)
    day_df['total_rentals'] = day_df['casual'] + day_df['registered']
    return day_df

data = load_data()

# Dashboard Title
st.title("Dashboard Analisis Penyewaan Sepeda")

# 1. Perkembangan Jumlah Penyewaan Sepeda dari Tahun ke Tahun
st.header("Perkembangan Jumlah Penyewaan Sepeda dari Tahun ke Tahun")
monthly_rentals = data.groupby(['year', 'month'])['cnt'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_rentals, x='month', y='cnt', hue='year', marker='o')
plt.title('Jumlah Penyewaan Sepeda per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Total Penyewaan')
plt.xticks(monthly_rentals['month'])
plt.grid()
st.pyplot(plt)

# 2. Pengaruh Faktor Cuaca terhadap Penyewaan Sepeda
st.header("Pengaruh Faktor Cuaca terhadap Penyewaan Sepeda")
weather_columns = ['temp', 'atemp', 'hum', 'windspeed']
correlation = data[weather_columns + ['cnt']].corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriks Korelasi antara Cuaca dan Penyewaan')
st.pyplot(plt)

# 3. Pola Penggunaan Sepeda pada Hari Kerja, Hari Libur, dan Hari Biasa
st.header("Pola Penggunaan Sepeda: Hari Kerja vs Hari Libur")
holiday_rentals = data.groupby('holiday')['cnt'].sum().reset_index()
plt.figure(figsize=(8, 5))
plt.bar(holiday_rentals['holiday'].map({0: 'Hari Biasa', 1: 'Hari Libur'}), holiday_rentals['cnt'], color=['blue', 'orange'])
plt.title('Total Penyewaan pada Hari Libur vs Hari Biasa')
plt.ylabel('Total Penyewaan')
st.pyplot(plt)

# 4. Hubungan antara Suhu Udara dan Tingkat Penyewaan Sepeda
st.header("Hubungan antara Suhu Udara dan Penyewaan Sepeda")
plt.figure(figsize=(10, 5))
sns.scatterplot(data=data, x='temp', y='cnt')
plt.title('Hubungan antara Suhu dan Penyewaan Sepeda')
plt.xlabel('Suhu (°C)')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(plt)

# Fitur Unik: Filter Data
st.sidebar.header("Filter Data")
selected_year = st.sidebar.selectbox("Pilih Tahun", data['year'].unique())
filtered_data = data[data['year'] == selected_year]

st.write(f"Data Penyewaan Sepeda untuk Tahun: {selected_year}")
st.dataframe(filtered_data)

# Fitur Unik: Descriptive Statistics
st.sidebar.header("Statistik Deskriptif")
if st.sidebar.button("Tampilkan Statistik"):
    st.write(filtered_data.describe())

# Fitur Unik: Visualisasi Penyewaan Berdasarkan Musim
st.sidebar.header("Visualisasi Penyewaan Berdasarkan Musim")
seasonal_rentals = data.groupby('season')['cnt'].sum().reset_index()
seasonal_rentals['season'] = seasonal_rentals['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
plt.figure(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=seasonal_rentals, palette='viridis')
plt.title('Total Penyewaan Sepeda Berdasarkan Musim')
