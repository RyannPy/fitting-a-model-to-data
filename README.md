# Indie Studio Ads Optimizer: Predicting Premium Upgrade & Total Spend

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Library-Pandas-orange.svg)](https://pandas.pydata.org/)

## Project Overview

## Dataset Description

Dataset yang digunakan merupakan hasil dari generator sintetis menggunakan file `dataset-generator.py` dengan korelasi antar-variabel disimulasikan sesuai dengan kondisi di dunia nyata. Berikut variabel yang dihasilkan:

- **days_active** : Jumlah hari akun dari player tersebut aktif, variabel ini dapat menjadi indikator loyalitas seorang player. Semakin tinggi nilainya, pemain tersebut memiliki kemungkinan besar lebih dekat dan terbiasa dengan game.
- **avg_session_time** : Rata-rata durasi bermain player per-hari (dalam menit). Durasi yang lama menandakan kenaikan kemungkinan ketertarikan player terhadap game.
- **community_engagement** : Skor interaksi komunitas (skala 1-100). Keaktifan player dalam forum, komunitas, atau guild melalui chat atau komentar mewakili kesan player terhadap game.
- **total_spend** : Seberapa banyak player menghabiskan uang untuk game tersebut (dalam rupiah). Variabel ini linear dengan days_active, avg_session_time, dan community_engagement.
- **is_premium** : Berupa kelas 0/1, berasal dari probabilitas seorang player akan premium. Probabilitas premium ini berasal dari skor premium berdasarkan pada kualitas variabel sebelumnya.
