from command_line_interface.translator import Translator
from command_line_interface.screen_message import ScreenMessage
from fetch import FetchAccounts
from abc import ABC
import submenu


class Submenu(submenu.Submenu):

    def __init__(self, class_name):
        super().__init__(class_name)

    def create_number_to_account_name(self):
        accounts_on_db = FetchAccounts.fetch()
        number_to_account_name = Translator.create_number_to_account_name(accounts_on_db)        
        ScreenMessage.show_number_to_account_name(number_to_account_name) 
        return number_to_account_name

    def create_dictionary_for_account_selection(self):      
        number_to_account_name = self.create_number_to_account_name()
        number_to_account_name_plus_skip = Translator.add_skip_option_to_dictionary(number_to_account_name)  
        ScreenMessage.show_skip_command_option()
        return number_to_account_name_plus_skip

    def select_account_name(self):        
        number_to_account_name = self.create_dictionary_for_account_selection()
        selected_number = ScreenMessage.prompt_select_account(self.class_name)
        while selected_number not in number_to_account_name:
            selected_number = ScreenMessage.reprompt_select_account()
        return number_to_account_name[selected_number]

    def get_user_new_account_data(self):
        account_name= ScreenMessage.prompt_account_name()   
        username, password = self.get_account_data()          
        return account_name, username, password

    def get_account_data(self):
        username = ScreenMessage.prompt_username()            
        password = ScreenMessage.prompt_password()   
        if password == None:
            sys.exit('blegh, no password')
        return username, password

    def show_account(self, account, username, password):
        ScreenMessage.show_selected_account_data(account, username, password)
        return 

    def no_account_selected(self):
        ScreenMessage.skip_command()

    def goodbye(self):
        ScreenMessage.goodbye()
        return

    def search_an_account(self):
        ScreenMessage.manual_account_lookup_message(self.class_name)
        account_inquired = ScreenMessage.prompt_account_name()
        if not account_inquired:
            ScreenMessage.reprompt_prompt_account_name()
        return account_inquired

    def show_account_matches(self, matches):
        ScreenMessage.show_account_matches(matches)
        return