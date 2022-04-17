from command_line_interface.screen_message import ScreenMessage
from abc import ABC

class GetInput(ABC):

    @staticmethod    
    def menu_choice(builders):
        # done
        user_option = ScreenMessage.prompt_command()  
        while user_option not in builders.keys():
            user_option = ScreenMessage.reprompt_command()
        return builders[user_option]

    @staticmethod 
    def user_account_name():
        #done
        account_username = ScreenMessage.prompt_account_name()   
        return account_username    

    @staticmethod
    def user_account_data():       
        #done
        account_username = ScreenMessage.prompt_username()            
        account_password = ScreenMessage.prompt_password()
        return account_username, account_password

    @staticmethod
    def select_account_name(number_to_account_name, created_class_name):
        #done             
        selected_account = ScreenMessage.prompt_select_account(created_class_name)
        while selected_account not in number_to_account_name:
            selected_account = ScreenMessage.reprompt_select_account()
        return number_to_account_name[selected_account]

    @staticmethod
    def is_exiting(exit_shortcut): 
        # done                               
        return exit_shortcut == ScreenMessage.prompt_continue(exit_shortcut)

    @staticmethod
    def account_for_searching(class_name):
        #done
        ScreenMessage.manual_account_lookup_message(class_name)
        account_inquired = ScreenMessage.prompt_account_name()
        if not account_inquired:
            ScreenMessage.reprompt_prompt_account_name()
        return account_inquired
