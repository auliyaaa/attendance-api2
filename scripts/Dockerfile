# Gunakan image Python resmi yang lebih ringan
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Salin dependensi aplikasi
COPY requirements.txt /app/

# Install dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode aplikasi
COPY . /app/

# Expose kedua port yang digunakan oleh Flask
EXPOSE 5000 8080

# Jalankan Flask di kedua port menggunakan multiprocessing
CMD ["python", "app.py"]
