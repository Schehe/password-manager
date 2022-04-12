import sqlite3
import os
from sqlite3 import Error
from createconn import create_connection

accounts_db = 'accounts.db'
correct_option_list = {'a': 'add', 'r': 'retrieve', 'd': 'delete', 'e': 'edit', 'x': 'sys.exit(0)'}


class MainMenu():
    def __init__(self):
        pass

    def __str__(self):
        return 'something'

    def start(self):
        conn = create_connection(accounts_db)
        self.create_table(conn)
        os.system('cls')
        print('*************************\n')
        print('Flaming Password Manager Lite Plus\n')
        print('Main Menu\n')
        print('Option list: ')
        print('A. Add an account')
        print('R. Retrieve an account')
        print('D. Delete an account')
        print('E. Edit an account')
        print('X. eXit program\n')
        print('*************************\n')
        print()

        user_option = input('Choose an option: ').lower()   
        print()
        while True:
            if user_option not in correct_option_list:
                user_option = input('Plese choose a correct option from the list above: ')
            else:
                break
        return user_option

    def create_connection(self, db_file):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn

    def create_table(self, conn):

        create_table_sql = """CREATE TABLE IF NOT EXISTS accounts ( 
            id INTEGER PRIMARY KEY NOT NULL, 
            account_name TEXT NOT NULL, 
            username TEXT NOT NULL, 
            password TEXT NOT NULL); """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
            c.close()
        except Error as e:
            print(e)





