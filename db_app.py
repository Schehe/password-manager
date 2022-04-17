import sqlite3
from sqlite3 import Error
from program_config import ProgramConfig


class DbApp():

    @staticmethod
    def start():
        with sqlite3.connect(ProgramConfig.DB_FILE) as conn:    
            create_table_sql = """CREATE TABLE IF NOT EXISTS accounts ( 
                id INTEGER PRIMARY KEY NOT NULL, 
                account_name TEXT NOT NULL UNIQUE, 
                username TEXT NOT NULL, 
                password TEXT NOT NULL); """
            try:
                c = conn.cursor()
                c.execute(create_table_sql)
                c.close()
            except Error as e:
                print(e)

    @staticmethod
    def add(account_name, username, password):
        with sqlite3.connect(ProgramConfig.DB_FILE) as conn:
            try:
                add_table_sql = "INSERT INTO accounts (account_name, username, password) VALUES (?, ?, ?)"
                cursor = conn.cursor()
                cursor.execute(add_table_sql, (account_name, username, password))
                conn.commit()
            except sqlite3.IntegrityError:
                # Raised because or UNIQUE constraint for "name"
                return print(f'Account name "{account_name}" already exist')
            else:                
                return 
                       
    @staticmethod
    def retrieve_by_account_name(account_name):
        with sqlite3.connect(ProgramConfig.DB_FILE) as conn:
            retrieve_table_sql = "SELECT account_name, username, password FROM accounts WHERE account_name = ?"
            cursor = conn.cursor()
            cursor.execute(retrieve_table_sql, (account_name, ))
        return cursor.fetchall()

    @staticmethod
    def retrieve(index):
        with sqlite3.connect(ProgramConfig.DB_FILE) as conn:
            retrieve_table_sql = "SELECT account_name, username, password FROM accounts WHERE id = ?"
            cursor = conn.cursor()
            cursor.execute(retrieve_table_sql, (index, ))
        return cursor.fetchall()

    @staticmethod
    def delete(index):
        with sqlite3.connect(ProgramConfig.DB_FILE) as conn:
            delete_table_sql = "DELETE FROM accounts WHERE id = ?"
            cursor = conn.cursor()
            cursor.execute(delete_table_sql, (index, ))
            conn.commit()
            cursor.close()
        return

    @staticmethod
    def delete_by_account_name(account_name):
        with sqlite3.connect(ProgramConfig.DB_FILE) as conn:
            delete_table_sql = "DELETE FROM accounts WHERE account_name = ?"
            cursor = conn.cursor()
            cursor.execute(delete_table_sql, (account_name, ))
            conn.commit()
            cursor.close()
        return

    @staticmethod
    def edit(index, username, password):
        with sqlite3.connect(ProgramConfig.DB_FILE) as conn:
            edit_table_sql = "UPDATE accounts SET username = ?, password = ? WHERE id = ?"
            cursor = conn.cursor()
            cursor.execute(edit_table_sql, (username, password, index))
            conn.commit()
            cursor.close()
        
    @staticmethod
    def edit_by_account_name(account_name, username, password):
        with sqlite3.connect(ProgramConfig.DB_FILE) as conn:
            edit_table_sql = "UPDATE accounts SET username = ?, password = ? WHERE account_name = ?"
            cursor = conn.cursor()
            cursor.execute(edit_table_sql, (username, password, account_name))
            conn.commit()
            cursor.close()
        return 

    @staticmethod   
    def fetch_accounts_in_db():
        with sqlite3.connect(ProgramConfig.DB_FILE) as conn:
            list_sql_table = "SELECT id, account_name FROM accounts WHERE id IS NOT NULL ORDER BY account_name COLLATE NOCASE ASC"
            cursor = conn.cursor()
            cursor.execute(list_sql_table)
        return cursor.fetchall()

    @staticmethod
    def search_accounts_in_db(account_inquired):
        with sqlite3.connect(ProgramConfig.DB_FILE) as conn:
            accounts_sql_table = "SELECT account_name FROM accounts WHERE account_name LIKE ? ORDER BY account_name COLLATE NOCASE ASC"
            cursor = conn.cursor()
            cursor.execute(accounts_sql_table, ('%'+account_inquired+'%', ))
        return cursor.fetchall()

    @staticmethod
    def get_raw_passwords_with_indexes():
        with sqlite3.connect(ProgramConfig.DB_FILE) as conn:
            retrieve_table_sql = "SELECT id, password FROM accounts WHERE id IS NOT NULL"
            cursor = conn.cursor()
            cursor.execute(retrieve_table_sql, ())
        return cursor.fetchall()

    @staticmethod 
    def rewrite_pass(index, password):
        with sqlite3.connect(ProgramConfig.DB_FILE) as conn:
            retrieve_table_sql = "UPDATE accounts SET password = ? WHERE id = ?"
            cursor = conn.cursor()
            cursor.execute(retrieve_table_sql, (password, index))
        return

