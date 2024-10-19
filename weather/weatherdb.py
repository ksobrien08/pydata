# python3 -u "/Users/KB/Desktop/nothing/at/pydata/weather/weatherdb.py"
#----------------------------------------------------------------------------------------------
import mysql.connector, json 

def weather_db(city, description, temperature, humidity):
  print("Adding " + str(city) + " to the database.")
  with open('config.json') as key:
    config = json.load(key)
 
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=config['db_pw'],
    database="mydatabase"
  )

  cursor = mydb.cursor()
  cursor.execute("CREATE TABLE IF NOT EXISTS weather_tbl (city VARCHAR(255), description VARCHAR(255), temperature FLOAT(4), humidity FLOAT(4))")

  # Check if the city already exists
  cursor.execute("SELECT * FROM weather_tbl WHERE city = %s", (city,))
  result = cursor.fetchone()

  if result:
    # Update the record if it already exists
    cursor.execute("UPDATE weather_tbl SET description = %s, temperature = %s, humidity = %s WHERE city = %s", (description, temperature, humidity, city))
  else:
    # Insert a new record if it doesn't exist
    cursor.execute("INSERT INTO weather_tbl (city, description, temperature, humidity) VALUES  (%s, %s, %s, %s)", (city, description, temperature, humidity))

  mydb.commit()

  cursor.execute("SELECT * FROM weather_tbl")

  tbl = cursor.fetchall()

  count = 0
  for row in tbl:
    count += 1
    print(row)

  if count > 0:
    print("Added to database")
  
  cursor.execute("SELECT * FROM weather_tbl")

  mydb.close()


def delete_db():
  with open('config.json') as key:
    config = json.load(key)
 
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=config['db_pw'],
    database="mydatabase"
  )

  cursor = mydb.cursor()
  cursor.execute("DELETE FROM weather_tbl")
  mydb.commit()

  cursor.execute("SELECT * FROM weather_tbl")

  del_tbl = cursor.fetchall()

  for row in del_tbl:
    print(row)

  mydb.close()
