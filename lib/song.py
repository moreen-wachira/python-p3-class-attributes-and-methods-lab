class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment count and add the song to genres and artists lists
        Song.count += 1
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        Song.genre_count[self.genre] = Song.genre_count.get(self.genre, 0) + 1

    def add_to_artist_count(self):
        Song.artist_count[self.artist] = Song.artist_count.get(self.artist, 0) + 1

# Example usage:
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
single_ladies = Song("Single Ladies", "Beyonce", "Pop")
hotline_bling = Song("Hotline Bling", "Drake", "Rap")

# Accessing attributes
print(ninety_nine_problems.name)  # "99 Problems"
print(ninety_nine_problems.artist)  # "Jay-Z"
print(ninety_nine_problems.genre)  # "Rap"

# Accessing class attributes
print(Song.count)  # 3
print(Song.genres)  # ['Rap', 'Pop']
print(Song.artists)  # ['Jay-Z', 'Beyonce', 'Drake']
print(Song.genre_count)  # {'Rap': 2, 'Pop': 1}
print(Song.artist_count)  # {'Jay-Z': 1, 'Beyonce': 1, 'Drake': 1}
