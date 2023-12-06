import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 


#membaca dataframe yang ada
aotizhongxin_df = pd.read_csv("aotizhongxin_df")
changping_df = pd.read_csv("changping_df")
dingling_df = pd.read_csv("dingling_df")
dongs_df = pd.read_csv("dongs_df")
guanyuan_df = pd.read_csv("guanyuan_df ")
gucheng_df = pd.read_csv("gucheng_df")
huairou_df = pd.read_csv("huairou_df")
nongzhanguan_df = pd.read_csv("nongzhanguan_df")
shunyi_df = pd.read_csv("shunyi_df")
tiantan_df = pd.read_csv("tiantan_df")
wanliu_df = pd.read_csv("wanliu_df")
wanshouxigong_df = pd.read_csv("wanshouxigong_df")

#EDA
#membuat list untuk station dan year
station_list = [aotizhongxin_df,changping_df,dingling_df,
                dongs_df,guanyuan_df,gucheng_df,huairou_df,
                nongzhanguan_df,shunyi_df,tiantan_df,wanliu_df,
                wanshouxigong_df]
year_list = [2013,2014,2015,2016,2017]

#memilih suhu maksimal setiap tahunnya untuk semua station
max_temp_all = pd.DataFrame(columns=aotizhongxin_df.columns)

for year in year_list:
    for station in station_list:
        year_temp = station[station['year'] == year]
        max_temp = year_temp[year_temp['TEMP'] == year_temp['TEMP'].max()]
        max_temp_all = pd.merge(max_temp, max_temp_all, how='outer')
    
#mengelompoknya suhu tertinggi setiap tahun di masing-masing station
aotizhongxin_maxtemp = max_temp_all[max_temp_all['station'] == 'Wanshouxigong']
changping_maxtemp = max_temp_all[max_temp_all['station'] == 'Changping']
dingling_maxtemp = max_temp_all[max_temp_all['station'] == 'Dingling']
dongs_maxtemp = max_temp_all[max_temp_all['station'] == 'Dongsi']
guanyuan_maxtemp = max_temp_all[max_temp_all['station'] == 'Guanyuan']
gucheng_maxtemp = max_temp_all[max_temp_all['station'] == 'Gucheng']
huairou_maxtemp = max_temp_all[max_temp_all['station'] == 'Huairou']
nongzhanguan_maxtemp = max_temp_all[max_temp_all['station'] == 'Nongzhanguan']
shunyi_maxtemp = max_temp_all[max_temp_all['station'] == 'Shunyi']
tiantan_maxtemp = max_temp_all[max_temp_all['station'] == 'Tiantan']
wanliu_maxtemp = max_temp_all[max_temp_all['station'] == 'Wanliu']
wanshouxigong_maxtemp = max_temp_all[max_temp_all['station'] == 'Wanshouxigong']


#mencari suhu minimal setiap tahunnya disemua kota
min_temp_all =pd.DataFrame(columns=aotizhongxin_df.columns)

for year in year_list:
    for station in station_list:
        year_temp = station[station['year'] == year]
        min_temp = year_temp[year_temp['TEMP'] == year_temp['TEMP'].min()]
        min_temp_all = pd.merge(min_temp, min_temp_all, how='outer')

aotizhongxin_mintemp = min_temp_all[min_temp_all['station'] == 'Aotizhongxin']
    
#mengelompoknya suhu tertinggi setiap tahun di masing-masing station
aotizhongxin_mintemp = min_temp_all[min_temp_all['station'] == 'Aotizhongxin']
changping_mintemp = min_temp_all[min_temp_all['station'] == 'Changping']
dingling_mintemp = min_temp_all[min_temp_all['station'] == 'Dingling']
dongs_mintemp = min_temp_all[min_temp_all['station'] == 'Dongsi']
guanyuan_mintemp = min_temp_all[min_temp_all['station'] == 'Guanyuan']
gucheng_mintemp = min_temp_all[min_temp_all['station'] == 'Gucheng']
huairou_mintemp = min_temp_all[min_temp_all['station'] == 'Huairou']
nongzhanguan_mintemp = min_temp_all[min_temp_all['station'] == 'Nongzhanguan']
shunyi_mintemp = min_temp_all[min_temp_all['station'] == 'Shunyi']
tiantan_mintemp = min_temp_all[min_temp_all['station'] == 'Tiantan']
wanliu_mintemp = min_temp_all[min_temp_all['station'] == 'Wanliu']
wanshouxigong_mintemp = min_temp_all[min_temp_all['station'] == 'Wanshouxigong']

#mencari nilai pm2.5 maksimal setiap tahun untuk seluruh kota
pm25_all_max = pd.DataFrame(columns=aotizhongxin_df.columns)
for year in year_list:
    for station in station_list:
        year_pm25 = station[station['year'] == year]
        max_pm25 = year_pm25[year_pm25['PM2.5'] == year_pm25['PM2.5'].max()]
        pm25_all_max= pd.merge(max_pm25, pm25_all_max, how='outer')
 
#mengelompokan nilai pm2.5 rata - rata berdasarkan station, year, month   
pm25_max = pm25_all_max.groupby(['station','year','month'])['PM2.5'].mean()

#mencari nilai pm2.5 minimal setiap tahun untuk seluruh kota
pm25_all_min = pd.DataFrame(columns=aotizhongxin_df.columns)
for year in year_list:
    for station in station_list:
        year_pm25 = station[station['year'] == year]
        min_pm25 = year_pm25[year_pm25['PM2.5'] == year_pm25['PM2.5'].min()]
        pm25_all_min = pd.merge(min_pm25, pm25_all_min, how='outer')

#mengelompokan nilai pm2.5 rata - rata berdasarkan station, year, month 
pm25_min = pm25_all_min.groupby(['station','year','month'])['PM2.5'].mean()

#mencari nilai rain lebih dari 0 setiap tahun disemua kota
rain_total_greater =pd.DataFrame(columns=aotizhongxin_df.columns)
for station in station_list:
    rain = station[station['RAIN'] > 0]
    rain_total_greater= pd.merge(rain, rain_total_greater, how='outer')

#membuang kolom yang tidak dibutuhkan dan mengganti index dengan datetime untuk keperluan membuat tabel hubungan rain dengan wspm
rain_total_greater.drop(['No','year','month','day','hour','PM2.5','PM10','SO2','NO2','CO','O3','TEMP','PRES','DEWP','wd','station'], axis=1, inplace=True)
rain_total_greater.set_index('datetime', inplace=True)
df = rain_total_greater

#mencari nilai rain sama dengan 0
rain_total_equal =pd.DataFrame(columns=aotizhongxin_df.columns)
for station in station_list:
    rain = station[station['RAIN'] == 0]
    rain_total_equal= pd.merge(rain, rain_total_equal, how='outer')
    
#membuang kolom yang tidak dibutuhkan dan mengganti index dengan datetime untuk keperluan membuat tabel hubungan rain dengan wspm
rain_total_equal.drop(['No','year','month','day','hour','PM2.5','PM10','SO2','NO2','CO','O3','TEMP','PRES','DEWP','wd','station'], axis=1, inplace=True)
rain_total_equal.set_index('datetime', inplace=True)
df1 = rain_total_equal

#Data Vizualitation
#membuat lis untuk menampilkan suhu maksimal dan minimal setiap tahunnya dimasing-masing kota
max_temp_list = [
    aotizhongxin_maxtemp, changping_maxtemp, dingling_maxtemp,
    dongs_maxtemp, guanyuan_maxtemp, gucheng_maxtemp, huairou_maxtemp,
    nongzhanguan_maxtemp, shunyi_maxtemp, tiantan_maxtemp, wanliu_maxtemp,
    wanshouxigong_maxtemp
]

max_temp_list1 = [
    'aotizhongxin_maxtemp', 'changping_maxtemp', 'dingling_maxtemp',
    'dongs_maxtemp', 'guanyuan_maxtemp', 'gucheng_maxtemp', 'huairou_maxtemp',
    'nongzhanguan_maxtemp', 'shunyi_maxtemp', 'tiantan_maxtemp', 'wanliu_maxtemp',
    'wanshouxigong_maxtemp'
]

min_temp_list = [
    aotizhongxin_mintemp, changping_mintemp, dingling_mintemp,
    dongs_mintemp, guanyuan_mintemp, gucheng_mintemp, huairou_mintemp,
    nongzhanguan_mintemp, shunyi_mintemp, tiantan_mintemp, wanliu_mintemp,
    wanshouxigong_mintemp
]

min_temp_list1 = [
    'aotizhongxin_mintemp', 'changping_mintemp', 'dingling_mintemp',
    'dongs_mintemp', 'guanyuan_mintemp', 'gucheng_mintemp', 'huairou_mintemp',
    'nongzhanguan_mintemp', 'shunyi_mintemp', 'tiantan_mintemp', 'wanliu_mintemp',
    'wanshouxigong_mintemp'
]








st.title('Belajar Analisis Data')
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
 
with tab1:
    st.header("Tab 1")
    fig, ax = plt.subplots(figsize=(20, 5))
    df.plot(kind='line', ax=ax, title='Hubungan Rain>0 dengan WSPM')
    plt.savefig('grafik_rain_wspm_1.png')
    st.image('grafik_rain_wspm_1.png')

    fig1, ax = plt.subplots(figsize=(20, 5))
    df1.plot(kind='line', title='Hubungan Rain=0 dengan WSPM')
    plt.savefig('grafik_rain_wspm_2.png')
    st.image('grafik_rain_wspm_2.png')
 
with tab2:
    st.header("Tab 2")
    # Buat grafik
    fig, ax = plt.subplots(figsize=(15, 10))
    pm25_max.unstack().plot(kind='bar', ax=ax)
    ax.set_title('Rata-rata Konsentrasi PM2.5 Setiap Bulannya')
    plt.ylabel('Nilai PM2.5 (µg/m3)')

    # Tampilkan grafik
    with st.container():
        st.title('Grafik Rata-rata Konsentrasi PM2.5 Setiap Bulannya')
        st.pyplot(fig)

    # Buat grafik
    fig, ax = plt.subplots(figsize=(15, 10))
    pm25_min.unstack().plot(kind='bar', ax=ax)
    ax.set_title('Rata-rata Konsentrasi PM2.5 Setiap Bulannya')
    plt.ylabel('Nilai PM2.5 (µg/m3)')

    # Tampilkan grafik
    with st.container():
        st.title('Grafik Rata-rata Konsentrasi PM2.5 Setiap Bulannya')
        st.pyplot(fig)
 
with tab3:
    st.header("Tab 3")
    #menampilkan grafik rata - rata suhu maksimal disetiap kota
    for station, title in zip(max_temp_list, max_temp_list1):
        fig, ax = plt.subplots()

        ax.plot(station['datetime'], station['TEMP'], marker='o', linewidth=2, color='#72BCD4')
        ax.set_title(title)
        

        st.pyplot(fig)

    # Tampilkan grafik suhu minimal
    for station, title in zip(min_temp_list, min_temp_list1):
        fig, ax = plt.subplots()

        ax.plot(station['datetime'], station['TEMP'], marker='o', linewidth=2, color='#72BCD4')
        ax.set_title(title)
        

        st.pyplot(fig)
        
