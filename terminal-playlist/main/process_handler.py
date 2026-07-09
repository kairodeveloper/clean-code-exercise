from .constructor.song_register_constructor import song_registry_process
from src.view.first_view import *
from src.main.strings import *

def start() -> None:
    while True:
        command = introduction_page()

        if command == CODE_INSERT_SONG : song_registry_process()
        elif command == CODE_CREATE_PLAYLIST : print(LABEL_CREATE_PLAYLIST)
        elif command == CODE_EXIT : 
            print(goodbye_message())
            exit()
        else : print(LABEL_UNKNOWN_COMMAND)
