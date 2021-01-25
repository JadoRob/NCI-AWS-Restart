import mysql.connector
from mysql.connector import connect 
from colorama import Fore, Back, Style
from os import getenv, system, environ
from dotenv import load_dotenv

system('clear')
load_dotenv()

conn = connect(
    host=getenv('DB_URL'),
    user=getenv('DB_USER'),
    password=getenv('DB_PASSWORD'),
    database=getenv('DB_NAME')
)

try:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')

    for row in cursor:
        print(Fore.RED, f'''
        id.............. {row[0]}
        First Name...... {row[1]}
        Last Name....... {row[2]}
        Age............. {row[3]}
        ''')
except(Exception, mysql.connector.Error) as error:
    print('Error while fetching data from MySQL', error)

