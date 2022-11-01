import sqlite3

# creating table by importing file with all the names 

def connect():
    return c = sqlite3.connect("gmaps_database.db")

def creat_table(c, city: str):
    with c:
        return c.execute(CREATE_TABLE_CITY())
