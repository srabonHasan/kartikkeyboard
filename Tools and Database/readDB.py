import sqlite3
conn= sqlite3.connect("kartik.db")
cursor = conn.cursor()

#cursor.execute('CREATE TABLE bangla (ID INTEGER PRIMARY KEY, broken TEXT, fixed TEXT)')


#cursor.execute('INSERT INTO bangla VALUES(?, ?, ?)', (1, 'নঅ', 'ন'))
#cursor.execute('INSERT INTO bangla VALUES(?, ?, ?)', (2, 'ঝএ', 'ঝে'))

cursor.execute('SELECT * FROM bangla WHERE id=?', (2, ))
row = cursor.fetchone()
id = str(row[0])
broken = row[1]
fixed =row[2]

print(id+'.'+broken+':'+fixed)



conn.commit()
