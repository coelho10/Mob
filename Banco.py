import mysql.connector

def conectar():
    try:
        conn = mysql.connector.connect(
            host="10.1.1.248", #local
            port=3306,
            user="Flet",
            password="FtSas1#4AS1s1sKa1",
            database="neilar",
            ssl_disabled=True
        )
        if not conn:
            conn = mysql.connector.connect(
            host="interno2.neilar.com.br", #186.211.98.22 
            port=3306,
            user="Flet",
            password="FtSas1#4AS1s1sKa1",
            database="neilar",
            ssl_disabled=True
        )
        if not conn:
            conn = mysql.connector.connect(
            host="interno.neilar.com.br", #177.54.11.188
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