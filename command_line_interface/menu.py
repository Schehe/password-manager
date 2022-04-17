from command_line_interface.screen_message import ScreenMessage

class MainMenu():

    @staticmethod
    def create_menu(command_translator):
        ScreenMessage.intro()
        ScreenMessage.menu_options(command_translator)
        return MainMenu.get_user_choice(command_translator)

    @staticmethod
    def get_user_choice(command_translator):
        user_option = ScreenMessage.prompt_command()  
        while user_option not in command_translator.keys():
            user_option = ScreenMessage.reprompt_command()
        return command_translator[user_option]


class ExitMenu():

    @staticmethod
    def is_exiting(exit_shortcut):
    	return exit_shortcut == ScreenMessage.prompt_continue(exit_shortcut)
