import sqlite3 as sql
from venv import create


def createDB():
    conn = sql.connect("ejercicio1.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("ejercicio1.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE alumnos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL
        )"""
    )
    conn.commit()
    conn.close()

def insertData(id, nombre, apellido):
    conn = sql.connect("ejercicio1.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO alumnos VALUES ({id}, '{nombre}', '{apellido}')"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def readData():
    conn = sql.connect("ejercicio1.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM alumnos WHERE nombre = 'Francisco'"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)
    
        
#createDB()
#createTable()
#insertData(1,"Francisco", "Marchant")
#insertData(2,"Alejo", "Azola")
#insertData(3,"Camilo", "Aros")
#insertData(4,"Felipe", "Pincheira")
#insertData(5,"Carolina", "Pardo")
#insertData(6,"Sandra", "Aravena")
#insertData(7,"Gabriel", "Montenegro")
#insertData(8,"Samuel", "Orellana")
readData()