import sqlite3

conn = sqlite3.connect('../db.sqlite3')
cursor = conn.cursor()
SQL = '''SELECT * FROM Used_auto'''
cursor.execute(SQL)
Used_auto = cursor.fetchall()
print(Used_auto)
for i in range(len(Used_auto)):
    auto = Used_auto[i]
    SQL = '''INSERT INTO mainapp_usedauto VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    cursor.execute(SQL, (i, *auto))
    conn.commit()