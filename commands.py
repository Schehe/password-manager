from db_app import DbApp
from abc import ABC
import encryption
from command_line_interface.submenu import Submenu
import sys


class Command(ABC):

    def __init__(self):
        self.submenu = Submenu(str(self.__class__.__name__).lower())      

    def execute(self):
        pass
 

class Add(Command):

    def __init__(self):
        super().__init__() 

    def execute(self, encryption: encryption.Encryption=None, **kwargs):
        account, username, password = self.submenu.get_user_new_account_data()        
        password = encryption.encrypt(password)
        if password == None:
            sys.exit('No password')
        DbApp.add(account, username, password)
        return


class Retrieve(Command):

    def __init__(self):
        super().__init__()     

    def execute(self, encryption: encryption.Encryption=None):
        selected_account_name = self.submenu.select_account_name()
        if not selected_account_name:
            self.submenu.no_account_selected()
            return 
        account_name, username, password = DbApp.retrieve_by_account_name(selected_account_name)[0]
        password = encryption.decrypt(password)
        self.submenu.show_account(account_name, username, password)
        return 


class Delete(Command):

    def __init__(self):
        super().__init__()     

    def execute(self, encryption: encryption.Encryption=None, **kwargs):
        selected_account_name = self.submenu.select_account_name()
        if not selected_account_name:
            self.submenu.no_account_selected()
            return 
        DbApp.delete_by_account_name(selected_account_name)
        return


class Edit(Command):
    def __init__(self):
        super().__init__()     

    def execute(self, encryption: encryption.Encryption=None, **kwargs):    
        selected_account_name = self.submenu.select_account_name()        
        if not selected_account_name:
            self.submenu.no_account_selected()
            return 
        username, password = self.submenu.get_account_data()
        password = encryption.encrypt(password)
        if password == None:
            sys.exit('No password')
        DbApp.edit_by_account_name(selected_account_name, username, password)
        return


class Exit(Command):

    def execute(self, encryption: encryption.Encryption=None):
        self.submenu.goodbye()
        sys.exit(0)
        return 

class View(Command):

    def execute(self, encryption: encryption.Encryption=None):
        self.submenu.create_number_to_account_name()
        return


class Search(Command): 
    """So far only partial searches, since it's a small database and it can handle up to 200 accounts max"""
    def execute(self, encryption: encryption.Encryption=None):
        account_inquired = self.submenu.search_an_account()
        matches = DbApp.search_accounts_in_db(account_inquired)
        self.submenu.show_account_matches(matches)
        return

    
class E(Command):
    def __init__(self):
        super(E, self).__init__()  
        print('You pressed 1, and I was an E, just a test')

    def execute(self, encryption: encryption.Encryption=None):
        return 
        

class Xa(Command):

    def __init__(self):
        super(Xa, self).__init__()  
        print('You pressed 2, and I was an Xa, just a test')

    def execute(self, encryption: encryption.Encryption=None):
        return 


class Encrypt(Command):
    '''Encrypt all passwords with the current encryption method, if they weren't already'''
    def execute(self, encryption: encryption.Encryption=None):    
        raw_passwords = DbApp.get_raw_passwords_with_indexes()
        for row in raw_passwords:
            index = row[0]
            password = row[1]
            try:
                password = encryption.decrypt(password)
            except:
                password = encryption.encrypt(password)
                DbApp.rewrite_pass(index, password)
                continue
        print('This command encrypted all unencrypted passwords,')
        print('leaving encrypted passwords as they were')
        return
