from main_menu import MainMenu
from submenu import Submenu


class PwmGui():
    def __init__(self, main_menu=None, submenu=None):
        if main_menu == None:
            self._main_menu = MainMenu()
        if submenu == None:
            self._submenu = Submenu()

    @property
    def main_menu(self):
        return self._main_menu

    @property
    def submenu(self):
        return self._submenu


