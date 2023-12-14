<a name="readme-top"></a>
<h1 align="center">Reservasi Rumah Sakit Medikakuy</h1>
<p align="center">Basis Data 2023 - P1 Kelompok 11</p>

<details>
  <summary>Anggota Kelompok</summary>
  <ul>
    <li>G6401221023 - Ahmad Subhan Daryhadi</li>
    <li>G6401221036 - Ahmad Faiq Izzulhaq</li>
    <li>G6401221059 - Muhammad Bagir Shahab</li>
  </ul>
</details>

<details>
  <summary>Daftar Isi</summary>
  <ol>
    <li><a href="#tentang-projek">Tentang Projek</a></li>
    <li><a href="#menjalankan-website">Menjalankan Website</a>
      <ul>
        <li><a href="#prerequisite">Prerequisite</a></li>
        <li><a href="#cara-menjalankan">Cara Menjalankan</a></li>
      </ul>
    </li>
    <li><a href="#erd-dan-diagram-skematik">Erd dan Diagram Skematik</a></li>
    <li><a href="#crud">CRUD</a>
      <ul>
        <li><a href="#create">Create</a></li>
        <li><a href="#read">Read</a></li>
        <li><a href="#update">Update</a></li>
        <li><a href="#delete">Delete</a></li>
      </ul>
    </li>
    <li><a href="#dokumentasi-lainnya">Dokumentasi Lainnya</a></li>
  </ol>
</details>

## Tentang Projek
Sebuah website yang menghubungkan pasien dengan rumah sakit yang dipilih untuk membuat reservasi yang sesuai dengan jadwal yang tersedia. Melalui website ini, diharapkan pasien dapat memilih rumah sakit, dokter, dan jadwal yang sesuai dengan kebutuhan mereka. Sementara itu dokter dapat mengelola reservasi yang dipesan. Teknologi yang digunakan dalam membuat website ini adalah Django dan DB Browser for SQLite.
<p align="right">(<a href="#readme-top">Kembali ke atas</a>)</p>

## Menjalankan Website
Berikut adalah hal-hal yang diperlukan beserta langkah-langkah agar dapat menjalankan website ini secara lokal.
### Prerequisite
- Python (minimal versi 3.8)  
  Download python <a href="https://www.python.org/downloads/" target="_blank">disini</a>  
  Cek di terminal apakah sudah terinstall dengan benar, ketik:
  ```sh
  python --version
  ```
- Django  
  Download Django, di terminal ketik:
  ```sh
  python -m pip install django==4.1.6
  ```
  Cek di terminal apakah sudah terinstall dengan benar, ketik:
  ```sh
  python -m pip show django
  ```
### Cara Menjalankan
1. Download repositori ini dan ekstrak
2. Buka terminal, pastikan alamat sudah masuk ke dalam folder yang sudah diekstrak
3. Dalam terminal, ketik:
   ```sh
   python manage.py runserver
   ```
4. Salin alamat yang muncul ke browser dan jalankan
   ```sh
   http://127.0.0.1:8000/
   ```
<p align="right">(<a href="#readme-top">Kembali ke atas</a>)</p>

## ERD dan Diagram Skematik
- ERD
  <br> <img src="/screenshot/erd.png">
- Diagram skematik
  <br> <img src="/screenshot/diagramskematik.png">
<p align="right">(<a href="#readme-top">Kembali ke atas</a>)</p>

## CRUD
Create, read, update, delete.
### Create
- Membuat akun oleh pasien 
  <br> <img src="/screenshot/signup_pasien.png">
- Membuat reservasi oleh pasien
  <br> <img src="/screenshot/create_reservasi.png">
### Read
- Sign in
  <br> <img src="/screenshot/signin_dokter.png">
  <br> <img src="/screenshot/signin_pasien.png"> 
- Menampilkan jadwal reservasi beserta profil
  <br> <img src="/screenshot/mainpage_dokter.png" id="dokter">
  <br> <img src="/screenshot/mainpage_pasien.png" id="pasien">
### Update
- Mengubah data diri oleh pasien
  <br> <img src="/screenshot/edit_profil.png">
- Mengubah note dalam reservasi
  <br> <img src="/screenshot/note_dokter.png">
  <br> <img src="/screenshot/note_pasien.png">
- Menerima dan membatalkan reservasi oleh dokter  
  Terdapat icon centang dan silang dalam screenshot [menampilkan jadwal reservasi beserta profil](#dokter) di bagian Read  
- Mengubah dan membatalkan reservasi oleh pasien  
  Terdapat icon pensil dan silang dalam screenshot [menampilkan jadwal reservasi beserta profil](#pasien) di bagian Read
  <br> <img src="/screenshot/edit_reservasi.png">
### Delete
- Menghapus jadwal reservasi oleh pasien  
  Terdapat icon tempat sampah dalam screenshot [menampilkan jadwal reservasi beserta profil](#pasien) di bagian Read
<p align="right">(<a href="#readme-top">Kembali ke atas</a>)</p>

## Dokumentasi Lainnya
- Landing page
  <br> <img src="/screenshot/landing_page.png">
- Kerkom
  <br> <img src="/screenshot/dokumentasi.jpg">
<p align="right">(<a href="#readme-top">Kembali ke atas</a>)</p>
