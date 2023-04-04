----------------Txt-editor V1----------------

Matthew Ng 2023 ©

This is a very simple text file editor that allows you to create files, add words and delete words.

----------------HOW TO USE----------------
1. Create a folder with the name "word-lists" in the same directory that you have the text editor script stored in. 

2. Run the script. You will be asked to enter the name of your text file. Enter the name of the text file to open within that directory. 
If a file with that name does not exit then you will be asked if you would like to create a new txt file with that name. If so type "y".

3. You will now be presented with a list of options to configure the file's contents. The list will look as follows:

+----------------------------------------------------------+
| Please chose an option                                   |
|                                                          |
| 1) Add words to file                                     |
| 2) Remove words from file                                |
| 3) Open new file                                         |
| 0) Quit                                                  |
+----------------------------------------------------------+

Enter a number option to choose your method of configuration.

----------------IMPORTANT----------------

These below portions of the script were not written by the author. All other lines are copyright of the author.

----------------start----------------
def displaybox(menuWidth=60, menuLines=[]):
    clearScreen()
    insideWidth = menuWidth - 4
    displayLine("-", menuWidth, "+")
    for aMenuLine in menuLines:
        print("| {1:{0}} |".format(insideWidth, aMenuLine))
    displayLine("-", menuWidth, "+")
    
def clearScreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
----------------end----------------
