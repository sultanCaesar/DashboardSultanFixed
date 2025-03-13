import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("main_data.csv")

st.title("Analisis Pengguna Sepeda")
st.markdown("Dashboard ini menampilkan analisis terkait tren penggunaan sepeda berdasarkan berbagai faktor.")

menu = st.sidebar.radio("Pilih Analisis", [
    "Kontribusi Segmen Pengguna", 
    "Faktor Utama Penjualan Tertinggi", 
    "Tren Penjualan dari Waktu ke Waktu"
])

if menu == "Kontribusi Segmen Pengguna":
    st.subheader("Kontribusi Segmen Pengguna")
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='dteday', y='casual', data=df, label='Casual Users')
    sns.lineplot(x='dteday', y='registered', data=df, label='Registered Users')
    plt.title('Kontribusi Segmen Pengguna (Casual vs Registered) terhadap Total Penggunaan Sepeda')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Pengguna Sepeda')
    plt.xticks(rotation=45)  
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)


elif menu == "Faktor Utama Penjualan Tertinggi":
    st.subheader("Faktor Utama Penjualan Tertinggi")
    plt.figure(figsize=(18, 12))

    # Musim
    plt.subplot(3, 2, 1)
    sns.barplot(data=df, x='season', y='cnt', ci=None, palette='viridis')
    plt.title('Pengaruh Musim')
    plt.xlabel('Musim (1=semi, 2=panas, 3=gugur, 4=dingin)')
    plt.ylabel('Jumlah Pengguna Sepeda')

    # Suhu
    plt.subplot(3, 2, 2)
    sns.scatterplot(data=df, x='temp', y='cnt', hue='season', palette='coolwarm')
    plt.title('Hubungan Suhu dan Jumlah Pengguna Berdasarkan Musim')
    plt.xlabel('Suhu (°C)')
    plt.ylabel('Jumlah Pengguna Sepeda')

    # Cuaca
    plt.subplot(3, 2, 3)
    sns.barplot(data=df, x='weathersit', y='cnt', ci=None, palette='coolwarm')
    plt.title('Pengaruh Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca (1=Clear, 2=Misty, 3=Light Snow/Rain)')
    plt.ylabel('Jumlah Pengguna Sepeda')

    # Kelembapan
    plt.subplot(3, 2, 4)
    sns.scatterplot(data=df, x='hum', y='cnt', color='#4CAF50')
    plt.title('Pengaruh Kelembapan')
    plt.xlabel('Kelembapan (%)')
    plt.ylabel('Jumlah Pengguna Sepeda')

    # Kecepatan Angin
    plt.subplot(3, 2, 5)
    sns.scatterplot(data=df, x='windspeed', y='cnt', color='#2196F3')
    plt.title('Pengaruh Kecepatan Angin')
    plt.xlabel('Kecepatan Angin')
    plt.ylabel('Jumlah Pengguna Sepeda')

    plt.tight_layout()
    st.pyplot(plt)

elif menu == "Tren Penjualan dari Waktu ke Waktu":
    st.subheader("Tren Penjualan dari Waktu ke Waktu")
    df['dteday'] = pd.to_datetime(df['dteday'])
    date_range = st.date_input("Pilih Rentang Tanggal", [df['dteday'].min(), df['dteday'].max()])
    filtered_df = df[(df['dteday'] >= pd.to_datetime(date_range[0])) &
                     (df['dteday'] <= pd.to_datetime(date_range[1]))]
    
    plt.figure(figsize=(10, 5))
    plt.plot(filtered_df['dteday'], filtered_df['cnt'], label='Total Penjualan', color='tab:blue')
    plt.xlabel("Tanggal")
    plt.ylabel("Jumlah Pengguna")
    plt.title("Tren Penjualan Sepeda")
    plt.legend()
    st.pyplot(plt)
