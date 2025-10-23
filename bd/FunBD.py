import mysql.connector
from Banco import conectar


def RetFaturamento(ano, mes):
    conn = conectar()
    if conn is None:
        return False, "Erro conexão banco"
    try:
        cursor = conn.cursor(dictionary=True)  # Retorna cada linha como dict        
        query = (
            "SELECT a.NomeRepresentante, a.Faturamento FROM viewFletRetFaturamento a "
            "WHERE YEAR(a.Data) = %s AND MONTH(a.Data) = %s "
            "ORDER BY a.Faturamento DESC"
        )
        cursor.execute(query, (ano, mes))
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()         
        if resultado:
            return True, resultado  # Retorna lista de dicts com os dados
        else:
            return False, []
    except mysql.connector.Error as err:
        print(f"Erro ao executar consulta: {err}")
        return False, str(err)