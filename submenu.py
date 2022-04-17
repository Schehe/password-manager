import abc


class Submenu(abc.ABC):
    '''Abstract class used as an interface'''
    def __init__(self, class_name):
        self.class_name = class_name

    def create_submenu_dictionary(self):
        pass

    def submenu_dictionary_for_user_selection(self): 
        pass

    def select_account_name(self):
        pass

    def get_user_new_account_data(self):
        pass

    def get_account_data(self, account_name):
        pass

    def show_account(self):
        pass

    def show_all_accounts(self):
        pass

    def no_account_selected(self):
        pass

    def goodbye(self):
        pass

    def search_an_account(self):
        pass

    def show_account_matches(self, matches):
        pass