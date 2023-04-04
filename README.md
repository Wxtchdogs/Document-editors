<p>----------------Txt-editor V1----------------

<p>Matthew Ng 2023 ©

<p>This is a very simple text file editor that allows you to create files, add words and delete words.

<p>----------------HOW TO USE----------------
<p>1. Create a folder with the name "word-lists" in the same directory that you have the text editor script stored in. 

<p>2. Run the script. You will be asked to enter the name of your text file. Enter the name of the text file to open within that directory. 
<p>If a file with that name does not exit then you will be asked if you would like to create a new txt file with that name. If so type "y".

<p>3. You will now be presented with a list of options to configure the file's contents. The list will look as follows:

<p>+----------------------------------------------------------+
<p>| Please chose an option                                   |
<p>|                                                          |
<p>| 1) Add words to file                                     |
<p>| 2) Remove words from file                                |
<p>| 3) Open new file                                         |
<p>| 0) Quit                                                  |
<p>+----------------------------------------------------------+

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
