# Gunakan Debian Bullseye Slim sebagai base image
FROM debian:bullseye-slim

# Update dan install Apache dan mod_proxy
RUN apt-get update && apt-get install -y \
    apache2 \
    apache2-utils \
    && a2enmod proxy proxy_http \
    && rm -rf /var/lib/apt/lists/*

# Salin file konfigurasi Apache ke dalam container
COPY apache.conf /etc/apache2/sites-available/000-default.conf

# Expose port 80
EXPOSE 80

# Jalankan Apache di foreground
CMD ["apache2ctl", "-D", "FOREGROUND"]
