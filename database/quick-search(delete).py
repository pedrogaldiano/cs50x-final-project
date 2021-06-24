import sqlite3

connect = sqlite3.connect('exercises-data.db')
db = connect.cursor()
# 
# db.execute('''SELECT * FROM muscles''')

db.execute("SELECT exercise, muscle_id FROM exercises where muscle_id=9 or muscle_id=11")

items = db.fetchall()



for item in items:
    print(item)

# connect.commit()
connect.close()


# (3, aerobic)
# (8, abductors)
# (8, neck)