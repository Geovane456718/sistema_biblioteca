from mysql.connector import connect, Error

def conexao():
    conbd = connect(
        host='localhost',
        user='root',
        password='',
        database='sistema_biblioteca'
        )
    return conbd