from image import Image
from galleryDatabaseHelper import GalleryDatabaseHelper

#postID, postTitle, postCategory, postContent, postDat
class PostPageGenerator:
    def __init__(self, db):
        self.DB = GalleryDatabaseHelper(db)
        self.images = self.DB.getAllImages()
        self.imageIndex = 0 if len(self.images) > 0 else -1
    
    def addImage(self,image):
        image = self.DB.addImage(image)
        self.images.append(image)