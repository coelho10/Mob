import mysql.connector
from dialogo_modal import MsgInfo

def conectar():    
    conn = None
    hosts = [
        ("interno.neilar.com.br", "177.54.11.188"),    # externo 1
        ("10.1.1.2481", "local"),                       # local                
        ("interno2.neilar.com.br", "186.211.98.22")    # externo 2
    ]
    for host, comment in hosts:
        try:
            conn = mysql.connector.connect(
                host=host,
                port=3306,
                user="representante",
                #password="FtSas1#4AS1s1sKa1", Flet
                password="Rep140875####a82*As1As1s@87Gs",
                database="neilar",
                ssl_disabled=True,
                connection_timeout=2  # ajustável conforme sua necessidade (em segundos)
            )
            if conn.is_connected(): #faz 3 tentativas conforme os hosts
                return conn
        except mysql.connector.Error as err:
            print(f"Tentativa de conexão falhou ({host}): {err}")
            print("Erro ao conectar ao banco: Todas as tentativas falharam.")
    return None



            
