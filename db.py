import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123",
  database="shoes_db"
)

# print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS jordan (id INT AUTO_INCREMENT PRIMARY KEY, img_src VARCHAR(255), name VARCHAR(255), type VARCHAR(255), nbr_color VARCHAR(255), price VARCHAR(255))")

def insert_jordan(value_data):
    sql = "INSERT INTO jordan (img_src, name, type, nbr_color, price) VALUES (%s, %s, %s, %s, %s)"
    val = value_data
    mycursor.executemany(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
