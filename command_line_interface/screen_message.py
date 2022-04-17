from program_config import ProgramConfig

class ScreenMessage():

    @staticmethod
    def intro():
        print('\n' + '*' * 34 + '\n')
        print('Flaming Password Manager Lite Plus\n')
        print('Main Menu')
        print('\n' + '*' * 34 + '\n')
        return

    @staticmethod
    def menu_options(command_build):
        print('Options list:\n')        
        for option_shortcut, option_name in command_build.items():
            if option_name == ProgramConfig.VIEW_ALL_ACCOUNTS_COMMAND:
                print(f'{option_shortcut.upper()}. {option_name} all accounts stored')
            elif option_name == ProgramConfig.EXIT_COMMAND:
                print(f'{option_shortcut.upper()}. {option_name} program')
            else:
                print(f'{option_shortcut.upper()}. {option_name} an account') 
        print('\n' + '*' * 34 + '\n')
        return

    @staticmethod
    def prompt_command():
        return input('Choose an option: ').lower() 

    @staticmethod
    def reprompt_command():
        return input('Please choose a correct option from the list above: ').lower()

    @staticmethod
    def show_selected_option(created_class_name):
        print(f'You have chosen to {created_class_name}.')

    @staticmethod
    def show_skip_command_option():
        print(f'You may type {ProgramConfig.SKIP_COMMAND} to skip this step')

    @staticmethod
    def prompt_account_name():
        return input('Enter account name: ')

    @staticmethod
    def reprompt_account_name():
        return input('Enter a valid account name: ')

    @staticmethod
    def prompt_username():
        return input('Enter username for the account: ')

    @staticmethod
    def prompt_password():
        return input('Enter password for the account: ')

    @staticmethod
    def prompt_continue(exit_shortcut):
        user_option = input(f'Press any key + Enter to continue or {exit_shortcut} + Enter to leave the program: ')
        print()
        return user_option   

    @staticmethod
    def goodbye():
        print()
        print('Thank you. Come again')
        print('End of Program')
        return 

    @staticmethod
    def show_number_to_account_name(dictionary):
        print('*' * 37)
        print("Accounts currently stored in program:")
        print('*' * 37)
        for number, account_name in dictionary.items():
            print(f"{str(number)}. {account_name}")
        print()
        return    

    @staticmethod    
    def prompt_select_account(created_class_name):
        return input(f'Please enter number next to account you desire to {created_class_name}: ')

    @staticmethod
    def reprompt_select_account():
        return input(f'Please select a correct number shown above: ')

    @staticmethod
    def show_selected_account_data(account_name, username, password):
        print(f'This is your account data: ')
        print()
        print(f'Account : {account_name}')
        print(f'Username : {username}')
        print(f'Password : {password}')
        print()
        return

    @staticmethod
    def skip_command():
        print()
        print("Ok. Let's skip this command")
        return

    @staticmethod
    def manual_account_lookup_message(class_name):
        print()
        print(f"You have chosen to manually {class_name} an account.")

    @staticmethod
    def show_account_matches(matches):
        print(f"I've looked for partial matches too.")
        if not matches:
            print('But there were no matches. Sorry')
            return
        # Come back to do 1 / several cases
        print(f"Below are all the matches.")            
        for row in matches:
            for match in row:
                print(match)
        print()


