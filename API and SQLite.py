import requests
url = "https://api.agify.io/?name=michael"
try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("API response:", data
    else:
        print(f"Request failed with status code: {response.status_code}"
              except
        requests.exceptions.RequestException as e:
        print("Error during API request:", e)




import sqlite3
connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Michael", 25))
connection.commit()
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)
    connection.close()