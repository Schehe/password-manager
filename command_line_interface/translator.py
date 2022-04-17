from program_config import ProgramConfig

class Translator():
    ''' Translate shortcuts from command-line user interface to commands for the program to work'''
    def __init__(self):
        pass

    @staticmethod
    def shortcut_to_command(names):
        aux_counter = 0
        shortcut_dictionary = {}
        for counter, name in enumerate(names):
            for char in name:
                if char.lower() in shortcut_dictionary.keys():
                    continue
                else:
                    shortcut_dictionary[char.lower()] = name
                    break
            if len(shortcut_dictionary) == counter:
                aux_counter += 1
                shortcut_dictionary[str(aux_counter)] = name
        return shortcut_dictionary


    @staticmethod
    def create_number_to_account_name(account_list):
        number_to_account_name = {}
        for i, row in enumerate(account_list):
            number_to_account_name[str(i+1)] = str(row[1])
        return number_to_account_name

    @staticmethod
    def add_skip_option_to_dictionary(number_to_account_name):
        number_to_account_name[ProgramConfig.SKIP_COMMAND] = ProgramConfig.SKIP_VALUE
        return number_to_account_name

    @staticmethod
    def get_exit_shortcut(builders):
        for key, value in builders.items():
            if str(value).capitalize() == ProgramConfig.EXIT_COMMAND:
                return str(key)
        else:
            print('Big problem, no exit, abort!')
            return False
