# Bike Sharing Dashboard 🌟

## Instruksi untuk menjalankan dashboard.py

## Setup Environment - Anaconda
```
conda create --name bike-sharing-env python=3.9
conda activate bike-sharing-env
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir bike_sharing_dashboard
cd bike_sharing_dashboard
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run Streamlit App
```
streamlit run dashboard/dashboard.py
```

## Project Structure
```
submission
├── dashboard
│   ├── main_data.csv
│   └── dashboard.py
├── data
│   ├── day.csv
│   └── hour.py
│   └── Readme.txt
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

## Description
Dashboard ini dibuat untuk menganalisis pola penyewaan sepeda berdasarkan musim, dan waktu menggunakan dataset Bike Sharing. Dashboard ini memungkinkan pengguna untuk memfilter data berdasarkan rentang tanggal dan musim, serta memberikan visualisasi interaktif untuk memahami tren penyewaan sepeda.

**Fitur:**
- Filter rentang tanggal dan musim.
- Visualisasi tren penyewaan sepeda per bulan berdasarkan musim.
- Analisis perbedaan penyewaan sepeda pada jam sibuk dan santai.

Gunakan perintah di atas untuk mengatur dan menjalankan dashboard.