from python_oop_part_2.classes_and_objects.exr.spoopify.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return f"Cannot add songs. Album is published."
        elif song not in self.songs:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."
        return "Song is already in the album."

    def remove_song(self, song_name: str):
        if song_name not in [song.name for song in self.songs]:
            return "Song is not in the album."

        if self.published:
            return "Cannot remove songs. Album is published."

        self.songs = [song for song in self.songs if song.name != song_name]
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        deta = "\n".join([f"== {p.get_info()}" for p in self.songs])
        return (f"Album {self.name}" + "\n" +
                f"{deta}")
