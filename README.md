# Indie Studio Ads Optimizer: Predicting Premium Upgrade & Total Spend

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Library-Pandas-orange.svg)](https://pandas.pydata.org/)

## Project Overview

Project ini merupakan simulasi analisis data pada sebuah studio game indie untuk memahami perilaku pemain berdasarkan aktivitas bermain mereka. Fokus utama project adalah memprediksi:

1. **Total pengeluaran pemain (`total_spend`)** menggunakan pendekatan **Linear Regression**.
2. **Kemungkinan pemain menjadi Premium (`is_premium`)** menggunakan pendekatan **Logistic Regression** dan **Support Vector Machine (SVM)**.

Dataset pada project ini dibuat secara sintetis untuk mensimulasikan kondisi nyata dalam industri game, termasuk:

- loyal player,
- hardcore free-to-play player,
- casual spender,
- hingga whale player dengan pengeluaran ekstrem.

Selain melakukan prediksi, project ini juga berfokus pada interpretasi bisnis dari model machine learning, seperti:

- fitur apa yang paling memengaruhi spending,
- faktor utama peningkatan probabilitas premium,
- serta bagaimana perilaku pemain dapat digunakan untuk strategi monetisasi game.

---

## Dataset Description

Dataset yang digunakan merupakan hasil dari generator sintetis menggunakan file `dataset-generator.py` dengan korelasi antar-variabel disimulasikan sesuai dengan kondisi di dunia nyata. Berikut variabel yang dihasilkan:

- **days_active** : Jumlah hari akun dari player tersebut aktif. Variabel ini dapat menjadi indikator loyalitas seorang player. Semakin tinggi nilainya, pemain tersebut memiliki kemungkinan lebih besar untuk dekat dan terbiasa dengan game.

- **avg_session_time** : Rata-rata durasi bermain player per hari (dalam menit). Durasi bermain yang lebih lama menandakan tingkat keterlibatan pemain yang lebih tinggi terhadap game.

- **community_engagement** : Skor interaksi komunitas (skala 1-100). Keaktifan player dalam forum, komunitas, guild, atau percakapan sosial menjadi representasi keterikatan sosial pemain terhadap game.

- **total_spend** : Total pengeluaran player untuk game (dalam rupiah). Variabel ini memiliki hubungan linear dengan beberapa fitur seperti `days_active`, `avg_session_time`, dan `community_engagement`.

- **is_premium** : Variabel klasifikasi biner (0/1) yang menunjukkan apakah player merupakan pengguna premium atau bukan. Nilai ini berasal dari probabilitas premium berdasarkan perilaku dan aktivitas player.

---

## Project Workflow

Project ini dikerjakan melalui beberapa tahap utama:

1. **Synthetic Dataset Generation**
   - Membuat dataset sintetis menggunakan NumPy dan Pandas.
   - Menambahkan noise dan player personas agar distribusi data lebih realistis.

2. **Exploratory Data Analysis (EDA)**
   - Analisis statistik deskriptif.
   - Visualisasi distribusi data.
   - Correlation analysis.
   - Premium vs non-premium comparison.
   - Scatterplot analysis.

3. **Preprocessing**
   - Feature-target separation.
   - Train-test split.
   - Feature scaling menggunakan `StandardScaler`.

4. **Machine Learning Modeling**
   - Linear Regression.
   - Logistic Regression.
   - Support Vector Machine (SVM).

5. **Evaluation & Business Insight**
   - Regression metrics:
     - MAE
     - RMSE
     - R² Score
   - Classification metrics:
     - Accuracy
     - Precision
     - Recall
     - F1-Score
   - Confusion Matrix analysis.
   - Feature coefficient interpretation.
   - Decision boundary visualization.

---

## Key Findings

- `avg_session_time` menjadi faktor paling berpengaruh terhadap pengeluaran pemain (`total_spend`).
- `days_active` dan `avg_session_time` merupakan indikator utama kemungkinan player menjadi premium.
- Logistic Regression memberikan performa terbaik dibandingkan SVM pada dataset ini.
- Dataset menunjukkan pola realistis dengan keberadaan:
  - hardcore free-to-play player,
  - casual premium player,
  - dan whale spender.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## Author

Ryan
