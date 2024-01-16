import json
import sqlite3

# Membaca data dari file JSON
data_json = '''
[
    {"id": 1, "name": "Openness"},
    {"id": 2, "name": "Conscientiousness"},
    {"id": 3, "name": "Extraversion"},
    {"id": 4, "name": "Agreeableness"},
    {"id": 5, "name": "Neuroticism"}
]
'''
data = json.loads(data_json)

# Membuat koneksi ke database SQLite yang sudah ada
conn = sqlite3.connect('bigfive.db')
c = conn.cursor()

# Memasukkan data ke dalam tabel yang sudah ada
for item in data:
    c.execute('INSERT INTO Dimension (id, name) VALUES (?, ?)', (item['id'], item['name']))

# Commit perubahan dan tutup koneksi
conn.commit()
conn.close()
