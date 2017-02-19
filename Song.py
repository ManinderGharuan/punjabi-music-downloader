class Song():
    """
    Represents a single song extracted by scrapers
    """
    def __init__(self, name, artist, image_link='', mp3_links={}):
        self.name = name
        self.artist = artist
        self.image_link = image_link
        self.mp3_links = mp3_links

    def __repr__(self):
        return "<name: {} artist: {}>".format(self.name, self.artist)

    def to_dict(self):
        return {
            "name": self.name,
            "artist": self.artist,
            "image_link": self.image_link,
            "mp3_links": self.mp3_links
        }
