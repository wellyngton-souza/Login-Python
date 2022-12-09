import config.infoBD as infoBD
import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=infoBD.host_name,
            port=infoBD.host_port,
            user=infoBD.user_name,
            passwd=infoBD.user_password,
            database = infoBD.BD_name
        )
        print("MySQL Database connection successful")

        def InsertPessoa(connection, query):
            cursor = connection.cursor()
            try:
                cursor.execute(query)
                print("Insert successfully")
            except Error as err:
                print(f"Error: '{err}'")

        InsertPessoa_query = "INSERT INTO tb_pessoa VALUES(null, 'aiaiai', 'pokemon@gmail.com', 'pokemon')"
        InsertPessoa(connection, InsertPessoa_query)

    except Error as err:
        print(f"Error: '{err}'")
