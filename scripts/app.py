from flask import Flask, jsonify, request
import psycopg2
import multiprocessing

app = Flask(__name__)

# Fungsi untuk menghubungkan ke database PostgreSQL
def get_db_connection(): 
    conn = psycopg2.connect(
        host="db",  # Ganti dengan host Anda
        database="attendance2_db",  # Ganti dengan nama database Anda
        user="postgres",  # Ganti dengan username PostgreSQL Anda
        password="akucantik"  # Ganti dengan password PostgreSQL Anda
    )
    return conn

# Endpoint untuk menampilkan semua data
@app.route('/api/data', methods=['GET'])
def get_all_data():
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute('SELECT date, name, time, location, id FROM attendance_table;')# Ganti dengan nama tabel Anda
    rows = cur.fetchall()
    
    columns = ["Date", "Name", "Time", "Location", "id"]  # Sesuaikan dengan kolom tabel Anda
    result = [dict(zip(columns, row)) for row in rows]
    
    cur.close()
    conn.close()
    
    return jsonify(result)

# Endpoint untuk menampilkan data berdasarkan lokasi
@app.route('/api/data/location', methods=['GET'])
def get_data_by_location():
    location = request.args.get('location')  # Mengambil parameter lokasi dari URL
    
    if not location:
        return jsonify({'error': 'Location parameter is required'}), 400
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute('SELECT date, name, time, location, id FROM attendance_table WHERE location = %s;', (location,))
    rows = cur.fetchall()
    
    columns = ["Date", "Name", "Time", "Location", "id"]  # Sesuaikan dengan kolom tabel Anda
    result = [dict(zip(columns, row)) for row in rows]
    
    cur.close()
    conn.close()
    
    return jsonify(result)

# Endpoint untuk menghapus data berdasarkan ID menggunakan GET
@app.route('/api/data/delete/id/<int:id>', methods=['GET'])

def delete_data_by_id(id):
    conn = get_db_connection()
    cur = conn.cursor()

    # Perbaiki query SQL dengan menggunakan nama kolom yang benar
    cur.execute('DELETE FROM attendance_table WHERE id = %s;', (id,))
    conn.commit()

    if cur.rowcount == 0:
        return jsonify({'error': 'Data not found'}), 404

    cur.close()
    conn.close()

    return jsonify({'message': f'Data with ID {id} has been deleted successfully'}), 200

# Fungsi untuk menjalankan Flask di port tertentu
def run_server(port):
    app.run(debug=True, host='0.0.0.0', port=port, use_reloader=False)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=run_server, args=(5000,))
    p2 = multiprocessing.Process(target=run_server, args=(8080,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
