
import mysql.connector
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

DB_HOST = config.get('Database', 'DB_HOST')
DB_USER = config.get('Database', 'DB_USER')
DB_PASSWORD = config.get('Database', 'DB_PASSWORD')
DB_NAME = config.get('Database', 'DB_NAME')

def get_database_connection():
    conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
    )
    return conn
    
