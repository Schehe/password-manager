from pwmgui import PwmGui


program = PwmGui()
while True:
    user_option = program.main_menu.start()
    user_option = program.submenu.start(user_option)
    if user_option == 'x':
        break