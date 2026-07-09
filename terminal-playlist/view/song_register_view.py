from .first_view import clear_terminal

class SongRegisterView:
    def registry_song_initial(self) -> dict:
        clear_terminal()

        print("Implement new song")

        title = input("Set the name og the song -> ")
        artist = input("Set the name of the artist/group -> ")
        year = input("Set the publish year -> ")

        new_song_informations = {
            "title": title,
            "artist": artist,
            "year": year
        }

        clear_terminal()
        return new_song_informations