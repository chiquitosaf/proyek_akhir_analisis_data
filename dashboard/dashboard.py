import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

def create_sewa_per_musim_df(df):
    sewa_per_musim = df.groupby('season').cnt.sum().reset_index().sort_values(by = 'cnt', ascending=True)

    return sewa_per_musim

def create_sewa_per_cuaca_df(df):
    sewa_per_cuaca = df.groupby('weathersit').cnt.sum().reset_index().sort_values(by = 'cnt', ascending=True)

    return sewa_per_cuaca

def create_cuaca_pada_musim_df(df):
    cuaca_pada_musim = df.groupby(['season', 'weathersit']).dteday.nunique().unstack(fill_value=0)

    return cuaca_pada_musim

def create_holiday_bike_sharing_df(df):
    holiday_bike_sharing = df.groupby('holiday').agg({
        "instant" : "count",
        "cnt" : "sum"
    }).reset_index()
    
    return holiday_bike_sharing

bike_sharing_df = pd.read_csv("bike_sharing_data.csv")

st.header('Proyek Analisis Data : Bike Sharing Data | Chiquito Shaduq Aurick Fulvian')
st.subheader('Data Jumlah Sewa Sepeda')

tab1, tab2, tab3 = st.tabs(['Musim', 'Cuaca', 'Hari Libur'])

with tab1:
    st.header("Jumlah Sewa Sepeda Berdasarkan Musim")
    sewa_per_musim = create_sewa_per_musim_df(bike_sharing_df)
    fig = plt.figure(figsize=(10,6))
    sns.barplot(x = 'cnt', y = 'season', data = sewa_per_musim)

    plt.title("Jumlah Sewa Sepeda Tiap Musim")
    plt.xlabel('Jumlah Sepeda yang Disewa')
    plt.ylabel('Musim')
    st.pyplot(fig)



with tab2:
    st.header("Jumlah Sewa Sepeda Berdasarkan Cuaca")
    sewa_per_cuaca = create_sewa_per_cuaca_df(bike_sharing_df) 
    fig = plt.figure(figsize=(10,6))
    sns.barplot(x = 'cnt', y = 'weathersit', data = sewa_per_cuaca)

    plt.title("Jumlah Sewa Sepeda Tiap Cuaca")
    plt.xlabel('Jumlah Sepeda yang Disewa')
    plt.ylabel('Cuaca')

    st.pyplot(fig)

    fig1 = plt.figure(figsize=(10,10), dpi=1600)

    cuaca_pada_musim = create_cuaca_pada_musim_df(bike_sharing_df)

    data_musim = cuaca_pada_musim.loc['spring']    
    total_count = data_musim.sum()
    percentages = data_musim / total_count * 100
    ax1 = plt.subplot2grid((2,2), (0,0))
    ax1.pie(percentages, labels=percentages.index, autopct='%1.1f%%', startangle=140)
    ax1.set_title('Presentase cuaca di musim Spring')
    ax1.axis('equal')  

    data_musim = cuaca_pada_musim.loc['summer']    
    total_count = data_musim.sum()
    percentages = data_musim / total_count * 100
    ax1 = plt.subplot2grid((2,2), (0,1))
    ax1.pie(percentages, labels=percentages.index, autopct='%1.1f%%', startangle=140)
    ax1.set_title('Presentase cuaca di musim Summer')
    ax1.axis('equal')  

    data_musim = cuaca_pada_musim.loc['fall']    
    total_count = data_musim.sum()
    percentages = data_musim / total_count * 100
    ax1 = plt.subplot2grid((2,2), (1,0))
    ax1.pie(percentages, labels=percentages.index, autopct='%1.1f%%', startangle=140)
    ax1.set_title('Presentase cuaca di musim Fall')
    ax1.axis('equal')  

    data_musim = cuaca_pada_musim.loc['winter']    
    total_count = data_musim.sum()
    percentages = data_musim / total_count * 100
    ax1 = plt.subplot2grid((2,2), (1,1))
    ax1.pie(percentages, labels=percentages.index, autopct='%1.1f%%', startangle=140)
    ax1.set_title('Presentase cuaca di musim Winter')
    ax1.axis('equal')  
    
    st.pyplot(fig1)



with tab3:
    st.header("Jumlah Sewa Sepeda Berdasarkan Hari Libur")
    holiday_bike_sharing = bike_sharing_df.groupby('holiday').agg({
        "instant" : "count",
        "cnt" : "sum"
    }).reset_index()

    total_non_holiday = holiday_bike_sharing.loc[holiday_bike_sharing['holiday'] == 0, 'instant'].values[0]
    total_sharing_non_holiday = holiday_bike_sharing.loc[holiday_bike_sharing['holiday'] == 0, 'cnt'].values[0]

    total_holiday = holiday_bike_sharing.loc[holiday_bike_sharing['holiday'] == 1, 'instant'].values[0]
    total_sharing_holiday = holiday_bike_sharing.loc[holiday_bike_sharing['holiday'] == 1, 'cnt'].values[0]
    percentage_sharing_holiday = (total_sharing_holiday / total_holiday) 
    percentage_sharing_non_holiday = (total_sharing_non_holiday / total_non_holiday)

    percentage_sharing_holiday
    fig = plt.figure(figsize=(10,6))
    plt.bar(['Hari Libur', 'Hari Kerja'], [percentage_sharing_holiday, percentage_sharing_non_holiday], color=['skyblue', 'salmon'])
    plt.title('Jumlah Sewa Sepeda Pada Hari Libur dan Kerja')
    plt.ylabel('Jumlah Sewa per Hari')
    st.pyplot(fig)