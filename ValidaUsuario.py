import mysql.connector
from Banco import conectar


def validar_usuario(email, senha):
    conn = conectar()
    if conn is None:
        return False, "Erro conexão banco"
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM UsuarioWeb WHERE Email = %s AND Senha = %s"
        cursor.execute(query, (email, senha))
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()         
        return len(resultado) == 1, "Conectado"
    except mysql.connector.Error as err:
        print(f"Erro ao executar consulta: {err}")
        return False, str(err)