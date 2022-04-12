import sys
import sqlite3
from sqlite3 import Error
from createconn import create_connection
from main_menu import correct_option_list, accounts_db 


class Submenu():
    def __init__(self):
        self.conn = None

    def start(self, user_option):
        self.conn = create_connection(accounts_db)
        if user_option.lower() == 'x':
            self.restart_or_get_out(user_option, get_out=True)

        if user_option.lower() == 'a':
            print("You have chosen to add an account (a reminder just in case you're drunk)\n")
            
            account_name, account_username, account_password = self.get_data()
            self.add(account_name, account_username, account_password)

        elif user_option.lower() == 'r' or user_option.lower() == 'd' or user_option == 'e':
            print(f'Please choose an account to {correct_option_list[user_option]} ')
            self.list_accounts_in_db()
            print()
            selected_account = input('Please select the number related to your account: ')
            rows_counter = self.rows_in_db()

            while selected_account not in rows_counter:
                selected_account = input(f'Write a number associated with an account shown above: ')
            print(f'\n You have chosen to {correct_option_list[user_option]} an account\n')
            eval('self.' + correct_option_list[user_option] + '(selected_account)')

            print('You have correctly ' + correct_option_list[user_option] + ('d' if correct_option_list[user_option][-1] == 'e' else 'ed') + ' that account\n')

        else:
            print('WTF')

        return self.restart_or_get_out(user_option)

    def restart_or_get_out(self, user_option, get_out=False):
        self.conn.close()
        if get_out == False:
            user_option = input('Press any key + enter to continue or x + enter to leave the program: ')
            print()
        if get_out == True or user_option == 'x':
            print('Thank you. Come again')
            eval(correct_option_list[user_option])
        return 

    def add(self, name, user, password):
        add_table_sql = "INSERT INTO accounts (account_name, username, password) VALUES (?, ?, ?)"
        cursor = self.conn.cursor()
        cursor.execute(add_table_sql, (name, user, password))
        self.conn.commit()
        cursor.close()
        return

    def retrieve(self, index):
        retrieve_table_sql = "SELECT * FROM accounts WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(retrieve_table_sql, (index))
        for row in cursor:
            print(f'Username: {row[2]}\nPassword: {row[3]}')
            print()
        cursor.close()
        return

    def delete(self, index):
        delete_table_sql = "DELETE FROM accounts WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(delete_table_sql, (index))
        self.conn.commit()
        cursor.close()
        return

    def edit(self, index):
        account_name, account_username, account_password = self.get_data(index)
        edit_table_sql = "UPDATE accounts SET username = ?, password = ? WHERE id = ?"
        cursor = self.conn.cursor()
        cursor.execute(edit_table_sql, (account_username, account_password, index))
        self.conn.commit()
        cursor.close()
        return

    def get_data(self, index=None):
        account_name = None
        if index == None:
            account_name = input('Enter account name: ')
        account_username = input('Enter username for the account: ')            
        account_password = input('Enter password for the account: ')
        return (account_name, account_username, account_password)

    def list_accounts_in_db(self):
        list_sql_table = "SELECT id, account_name FROM accounts"
        cursor = self.conn.cursor()
        cursor.execute(list_sql_table)
        for row in cursor:
            print(f'{row[0]}. {row[1]}')
        print()
        cursor.close()
        return

    def rows_in_db(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id FROM accounts")
        counter = []
        for row in cursor:
            counter.append(str(row[0]))
        cursor.close()
        return counter

# list(map(str, range(1, len(accounts_db) + 1)))
# list(map(str, range(1, rows_counter + 1)))