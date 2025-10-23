import mysql.connector

def conectar():
    try:
        conn = mysql.connector.connect(
            host="10.1.1.248",
            port=3306,
            user="Flet",
            password="FtSas1#4AS1s1sKa1",
            database="neilar",
            ssl_disabled=True
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco: {err}")
        return None