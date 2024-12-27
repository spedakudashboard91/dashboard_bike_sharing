# dashboard_bike_sharing
Dashboard Analisis Data Sepeda
Proyek ini adalah dashboard analisis data sepeda menggunakan Streamlit. Dashboard ini menampilkan data sepeda berdasarkan hari dan jam.

Cara Menjalankan Dashboard
1. Persyaratan
Pastikan Anda memiliki Python 3.6 atau lebih baru terinstal di sistem Anda. Anda juga perlu menginstal pip jika belum terinstal.

2. Mengunduh Dataset
Sebelum menjalankan dashboard, Anda perlu mengunduh dataset yang diperlukan. Dataset dapat diunduh dari Google Drive atau sumber lain. Pastikan Anda memiliki dua file CSV: day_dataset.csv dan hour_dataset.csv.

3. Setting Environment
Buat virtual environment (opsional) dan aktifkan:

python -m venv venv
source venv/bin/activate  # Untuk Linux/Mac
venv\Scripts\activate  # Untuk Windows

File Structures
├── .streamlit
├── Dashboard
│   ├── dashboard_bike.py
│   └── day.csv
├── Dataset
│   ├── day.csv
│   ├── hour.csv
|   └── Readme.txt
├── README.md
├── notebook1.ipynb
└── requirements.txt
