import os
import subprocess

def clear_terminal():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

def introduction_page() -> str:
    message = '''
                                                  __  
                                                 |__| 
        ==        ==   ==       ==     =======    ==     ======
        ===      ===   ==       ==    ===   ===   ==    =======  
        == ==  == ==   ==       ==    ==          ==   ==     
        ==  ====  ==   ==       ==     ======     ==   ==
        ==   ==   ==   ==       ==           ==   ==   ==     
        ==        ==    ==== ====     ===   ===   ==    =======   
        ==        ==      =====        =======    ==     ======

        * Add song               -> 1
        * Create playlist        -> 2
        * Sair                   -> 5 
    '''

    print(message)

    command = input("Command: ")

    return command


def goodbye_message() -> str:
    clear_terminal()
    
    message = '''
        =====    ==     ==  =======   ======
        ==   ==   ==   ==   ==         ==== 
        ==   ==    == ==    ==         ====
        =====       ===     ======      ==
        ==   ==     ==      ==         
        ==   ==    ==       ==          ==   
        =====     ==        =======     ==
    '''

    return(message)