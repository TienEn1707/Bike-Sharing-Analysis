import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
hour_df = pd.read_csv('dashboard/main_data.csv')

# Preprocessing data
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
season_dict = {
    1: 'Spring', 
    2: 'Summer', 
    3: 'Fall', 
    4: 'Winter'}
hour_df['season_label'] = hour_df['season'].map(season_dict)

# Title
st.title('Dashboard Penyewaan Sepeda')

# Sidebar untuk interaksi pengguna
st.sidebar.header('Filter Data')

# Widget: Pilih Rentang Tanggal
start_date, end_date = st.sidebar.date_input('Pilih Rentang Tanggal:', [hour_df['dteday'].min(), hour_df['dteday'].max()])
filtered_df = hour_df[(hour_df['dteday'] >= pd.to_datetime(start_date)) & (hour_df['dteday'] <= pd.to_datetime(end_date))]

# Widget: Pilih Musim
selected_season = st.sidebar.multiselect('Pilih Musim:', options=hour_df['season_label'].unique(), default=hour_df['season_label'].unique())
filtered_df = filtered_df[filtered_df['season_label'].isin(selected_season)]




# Hasil analisis data dari main_data.csv
# Pertanyaan 1: Bagaimana Pola Penyewaan Sepeda Berdasarkan Musim?
st.subheader('1. Pola Penyewaan Sepeda Berdasarkan Musim')
monthly_avg = hour_df.groupby(['mnth', 'season_label'])['cnt'].mean().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))

sns.lineplot(x='mnth', y='cnt', hue='season_label', data=monthly_avg, marker='o', palette='tab10', ax=ax)
sns.scatterplot(x='mnth', y='cnt', hue='season_label', data=monthly_avg, palette='tab10', legend=False, s=100, edgecolor='black', ax=ax)

ax.set_title('Tren Penyewaan Sepeda per Bulan Berdasarkan Musim')
ax.set_xlabel('Bulan')
ax.set_ylabel('Rata-rata Jumlah Penyewaan')
ax.set_xticks(ticks=range(1, 13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax.legend(title='Musim', loc='upper right')
ax.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig)

# Insight untuk analisis musiman
st.markdown(
    "Dari grafik di atas, terlihat bahwa **musim gugur (Fall)** memiliki rata-rata penyewaan sepeda tertinggi dibandingkan musim lainnya. "
    "Musim panas (Summer) juga menunjukkan tren penyewaan yang stabil, sedangkan musim dingin (Winter) memiliki penyewaan paling sedikit, kemungkinan karena kondisi cuaca yang kurang mendukung."
)

# Pertanyaan 2: Apakah Ada Perbedaan Signifikan Pola Penyewaan pada Jam Sibuk dan Jam Santai?
st.subheader('2. Perbandingan Penyewaan Sepeda pada Jam Sibuk dan Jam Santai')

# Definisikan jam sibuk: 7-9 pagi dan 5-7 sore
hour_df['peak_hour'] = hour_df['hr'].apply(lambda x: 'Peak' if x in [7,8,9,17,18,19] else 'Off-Peak')

fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(data=hour_df, x='peak_hour', y='cnt', palette='Set1')

ax.set_title('Perbandingan Penyewaan Sepeda pada Jam Sibuk dan Jam Santai')
ax.set_xlabel('Kategori Waktu')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# Distribusi Penyewaan Sepeda per Jam
fig, ax = plt.subplots(figsize=(12, 6))
sns.histplot(data=hour_df, x='hr', weights='cnt', bins=24, hue='peak_hour', multiple='stack', palette='Paired', ax=ax)
ax.set_title('Distribusi Penyewaan Sepeda per Jam')
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah Penyewaan')
ax.grid(True, linestyle='--', alpha=0.7)
st.pyplot(fig)

# Insight untuk distribusi jam
st.markdown(
    "Grafik distribusi menunjukkan lonjakan penyewaan pada **jam sibuk** (7-9 pagi dan 5-7 sore), yang mengindikasikan bahwa sepeda banyak digunakan untuk perjalanan kerja atau sekolah. "
    "Pada jam santai, jumlah penyewaan menurun, menandakan penggunaan sepeda lebih rendah di luar jam komuter."
)



# Hasil dari widget input
# Pertanyaan 1: Bagaimana Pola Penyewaan Sepeda Berdasarkan Musim?
st.header("")
st.write(f'• Hasil Pola Penyewaan Sepeda Berdasarkan Musim, pada tanggal {start_date} hingga {end_date}, sebagai berikut:')
monthly_avg = filtered_df.groupby(['mnth', 'season_label'])['cnt'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='mnth', y='cnt', hue='season_label', data=monthly_avg, marker='o', palette='tab10', ax=ax)
sns.scatterplot(x='mnth', y='cnt', hue='season_label', data=monthly_avg, palette='tab10', legend=False, s=100, edgecolor='black', ax=ax)
ax.set_title('Tren Penyewaan Sepeda per Bulan Berdasarkan Musim')
ax.set_xlabel('Bulan')
ax.set_ylabel('Rata-rata Jumlah Penyewaan')
ax.set_xticks(ticks=range(1, 13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax.legend(title='Musim', loc='upper right')
ax.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig)

# Pertanyaan 2: Apakah Ada Perbedaan Signifikan Pola Penyewaan pada Jam Sibuk dan Jam Santai?
st.write(f'• Hasil Perbandingan Penyewaan Sepeda pada Jam Sibuk dan Jam Santai, pada tanggal {start_date} hingga {end_date}, sebagai berikut:')
filtered_df['peak_hour'] = filtered_df['hr'].apply(lambda x: 'Peak' if x in [7,8,9,17,18,19] else 'Off-Peak')

fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data=filtered_df, x='hr', weights='cnt', bins=24, hue='peak_hour', multiple='stack', palette='Paired', ax=ax)
ax.set_title('Distribusi Penyewaan Sepeda per Jam')
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah Penyewaan')
ax.grid(True, linestyle='--', alpha=0.7) 
st.pyplot(fig)

# Footer
st.write('Dashboard ini dibuat untuk menganalisis pola penyewaan sepeda berdasarkan musim dan waktu. Gunakan filter di sidebar untuk menyesuaikan tampilan visualisasi.')