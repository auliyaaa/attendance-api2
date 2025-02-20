# Attendance API 2

Attendance API 2 adalah aplikasi backend yang dibangun menggunakan **CodeIgniter 4** untuk mengelola data kehadiran karyawan. Aplikasi ini membaca data absensi dari **file Excel**, menyimpannya ke dalam **PostgreSQL**, dan menyajikannya dalam format **JSON**.

---

## 📌 Fitur

- **Import Data Absensi** dari file Excel.
- **Simpan Data** ke dalam **PostgreSQL Database**.
- **RESTful API** untuk menampilkan data kehadiran dalam format JSON.
- **Docker Support** untuk containerization dan deployment yang mudah.

---

## 📁 Struktur Folder

````plaintext
attendance-api2/
├── apache/             # Folder konfigurasi apache
├── app/                # Folder utama aplikasi CodeIgniter 4
│   ├── Config/         # Konfigurasi aplikasi
│   ├── Controllers/    # Logika backend dan API
│   ├── Models/         # Model untuk akses database
│   └── Views/          # Template View (jika digunakan)
├── public/             # Root publik untuk akses URL
├── scripts/            # Folder flask app
├── writable/           # Folder untuk cache, logs, dan uploads
├── .env                # Konfigurasi lingkungan (Environment Variables)
├── composer.json       # Dependensi PHP dengan Composer
└── docker-compose.yml  # File docker compose

## 🚀 Instalasi
### Clone Repository
```sh
git clone https://github.com/auliyaaa/attendance-api2.git
cd attendance-api2

### Instal Dependensi
```sh
composer install

### Salin File .env dan Konfigurasi
```sh
cp env .env

#### Atur konfigurasi database di file .env:
```sh
database.default.hostname = localhost
database.default.database = attendance_db
database.default.username = your_db_username
database.default.password = your_db_password
database.default.DBDriver = Postgre

### Jalankan Migrasi Database
```sh
php spark migrate

### Jalankan Server Development
```sh
php spark serve
#### Akses aplikasi di http://localhost:8080

## 🐳 Menggunakan Docker (Opsional)
#### Jika menggunakan Docker untuk deployment:
```sh
docker-compose up -d
#### Aplikasi akan berjalan di http://localhost:8080.

## 📊 API Endpoint
#### Berikut beberapa endpoint utama dari Attendance API 2:
- GET /api/attendance – Mendapatkan semua data kehadiran.
- POST /api/attendance/import – Mengimpor data absensi dari file Excel.

## 🔧 Teknologi yang Digunakan
- CodeIgniter 4 - Framework PHP untuk backend API.
- PostgreSQL - Database untuk menyimpan data absensi.
- Docker - Containerization untuk deployment yang mudah.

## 👨‍💻 Kontributor
#### auliyaaa – Pengembang utama.
````
