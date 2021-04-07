
import sqlite3  
con = sqlite3.connect("list_pommes.db")  
print("Database opened successfully")  
con.execute("create table Student (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, prix TEXT NOT NULL)")  
print("Table created successfully")  
con.close()   