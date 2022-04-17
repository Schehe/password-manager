import os, sys
from db_app import DbApp
from program_config import ProgramConfig
from encryption import Fernet_AES128
from command_line_interface.translator import Translator
from command_line_interface.menu import MainMenu, ExitMenu
from factory import Factory
from commands import Command


if __name__ == '__main__':

    ProgramConfig.start()
    commands = Factory(Command)
    command_translator = Translator.shortcut_to_command(commands.builders.keys())
    exit_shortcut = Translator.get_exit_shortcut(command_translator)      
    DbApp.start()
    encryption = Fernet_AES128(ProgramConfig.ENC_KEY)
    os.system('cls')

    while True:
        user_choice = MainMenu.create_menu(command_translator)
        command = commands.create(user_choice)
        command.execute(encryption=encryption)
        if ExitMenu.is_exiting(exit_shortcut):
            exit_command = commands.create(command_translator[exit_shortcut])
            exit_command.execute(encryption=encryption)
