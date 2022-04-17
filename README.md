This password manager stores triads of account_name, username and encrypted password, in a SQLite database and control its management.\
For the moment it has command-line interface, with menues resembling 90s software where the user selects an option writing a 1 or 2-char shortcut from an options menu.\
Commands include:
- Add an account
- Retrieve an account username and password (unencrypted)
- Delete an account
- Edit an account
- View all accounts stored in the database
- Search for a specific account in the database
- Plus some other tests options
Passwords are encrypted for storing with Fernet AES-128.\

This version uses Factory Method pattern for the creation of the command classes (Command Pattern) that will handle the user choice.\
Each command class have a submenu that handles the extra data required to finish the execute method, which is usually a SQLITE inquiry to access or modify the database.\
For the shortcuts I designed a Translator class that creates (shortcut-to-action) and (shortcut-to-an account stored) for easier selection.\
It also includes some unit testing using python unittest module. I didn't create unit tests for every class in this version, up to now is more of an exercise to add this feature to my toolbox in the future.

Known Limitations:\
It is a command-line program. As such it is limited to show up to 200 lines.\
It can't handle multiple usernames per account, nor is able to let the user manually write the command instead of choosing through menus.\
Sooner than later it will be upgraded to a graphic interface for windows.\
It will get a better adapter than the translator class.\
It needs real testing for easier maintenance.\
Messages to screen could be managed differently, less coupled with other classes.\
Should MainMenu and ExitMenu inherit from an abstract class? (Program to an interface).
