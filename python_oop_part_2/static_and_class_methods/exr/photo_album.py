class PhotoAlbum:
    def __init__(self,pages: int):
        self.pages = pages
        self.photos = [] # only 4 on one page

    @classmethod
    def from_photos_count(cls, (photos_count: int):

