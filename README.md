Aplikasi ini adalah sebuah web sederhana untuk **prediksi harga mobil** menggunakan model Machine Learning yang telah dilatih sebelumnya. Aplikasi ini dibangun menggunakan **Streamlit** dan memanfaatkan file model yang disimpan dengan format `.sav`. Selain itu, aplikasi juga menampilkan beberapa grafik terkait data mobil untuk eksplorasi visual.

---

### Fitur Utama
1. **Menampilkan Dataset**  
   - Dataset berisi informasi terkait spesifikasi mobil. Data diimpor dari file `CarPrice.csv` dan ditampilkan di aplikasi.

2. **Visualisasi Data**  
   - Grafik interaktif untuk atribut berikut:
     - `highwaympg`: Konsumsi bahan bakar di jalan raya.
     - `curbweight`: Berat kendaraan.
     - `horsepower`: Tenaga kuda mesin mobil.

3. **Prediksi Harga Mobil**  
   - Menggunakan input pengguna berupa:
     - **Highway-mpg** (Konsumsi bahan bakar jalan raya)
     - **Curbweight** (Berat kendaraan)
     - **Horsepower** (Tenaga kuda mesin)
   - Model Machine Learning memprediksi harga mobil berdasarkan nilai-nilai input tersebut.

---

### Struktur File
- `prediksi_harga_mobil.sav`: File model Machine Learning yang telah dilatih untuk memprediksi harga mobil.
- `CarPrice.csv`: Dataset berisi informasi data mobil untuk ditampilkan dan digunakan sebagai contoh.
- `app.py`: File utama Streamlit untuk menjalankan aplikasi.

---

### Cara Menjalankan
1. **Persyaratan Sistem**  
   Pastikan Anda telah menginstal:
   - Python 3.8 atau lebih baru
   - Streamlit
   - Pandas
   - NumPy
   - scikit-learn

2. **Instalasi Dependensi**  
   Jalankan perintah berikut untuk menginstal semua dependensi:
   ```bash
   pip install streamlit pandas numpy scikit-learn
   ```

3. **Menjalankan Aplikasi**  
   Gunakan perintah berikut untuk menjalankan aplikasi Streamlit:
   ```bash
   streamlit run app.py
   ```

4. **Akses Aplikasi**  
   Setelah dijalankan, aplikasi dapat diakses melalui browser pada alamat:  
   `http://localhost:8501`

---

### Catatan
- Pastikan file `prediksi_harga_mobil.sav` dan `CarPrice.csv` berada di direktori yang sama dengan `app.py`.
- Jika ada kesalahan atau bug saat menjalankan aplikasi, pastikan dependensi telah terinstal dengan benar.
- 
