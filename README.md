# Indie Game Data Business Analysis

## Project Overview

Project ini merupakan studi kasus Exploratory Data Analysis (EDA) untuk memahami dinamika bisnis di industri game indie. Fokus utamanya adalah menganalisis faktor-faktor yang mendorong sebuah game menjadi menguntungkan (profitable) dan bagaimana menangani anomali data yang sering ditemui di lapangan. Project ini mengikuti alur CRISP-DM, dimulai dari Business Understanding hingga Data Preparation.

## Objective

- Statistical Integrity: Mendemonstrasikan pentingnya penggunaan Median dibandingkan Mean dalam menghadapi data yang memiliki outlier (anomali).
- Profitability Analysis: Mengidentifikasi persentase kesuksesan game indie berdasarkan simulasi pasar.
- Correlation Study: Menemukan hubungan antara biaya pengembangan (Dev Cost), biaya pemasaran (Marketing), dan harga jual (Price) terhadap profitabilitas.
- Leakage Audit: Mengidentifikasi potensi Data Leakage untuk mempersiapkan fase Machine Learning di masa depan.

## Dataset

Dataset ini dibuat secara sintetis menggunakan Python Data Generator dengan logika bisnis sebagai berikut:

- Revenue: Dihitung dari Player Base \* Price Tag (dengan potongan platform 30%).
- Success Factors: Popularitas dipengaruhi secara non-linear oleh biaya marketing dan kualitas game.
- Anomalies: Disuntikkan data glitch pada variabel avg_playtime (999 jam) untuk mensimulasikan kegagalan sistem pencatatan data.

## Key Insights

- The Outlier Trap: Rata-rata (Mean) waktu bermain terdistorsi oleh data anomali (999 jam), membuktikan bahwa Median adalah metrik yang lebih jujur untuk representasi perilaku pemain.
- Pricing Strategy: Sebagian besar game yang tidak menguntungkan (Non-profitable) memiliki korelasi kuat dengan harga jual yang terlalu rendah (atau gratis) tanpa strategi monetisasi tambahan.
- Marketing Effectiveness: Biaya marketing yang tinggi tidak selalu menjamin profit jika tidak dibarengi dengan konversi player base yang cukup untuk menutupi development cost.

## Disclaimer

Analisis ini fokus pada model bisnis Premium Games (Direct Purchase). Model ini belum memperhitungkan:

- In-App Purchases (IAP) atau sistem langganan.
- Pendapatan dari iklan (Ads Revenue).
- Biaya operasional server untuk game multiplayer.

## Files

- `indie-game-data-generator` -> generate data utama
- `indie-game-data.csv` -> data utama
- `analysis.ipynb` -> analisis

## Tools Used

- Python (Pandas, NumPy)
- Matplotlib & Seaborn (Data Visualization)
- Jupyter Notebook

## Author

Ryan
