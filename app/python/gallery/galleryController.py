from image import Image
from galleryDatabaseHelper import GalleryDatabaseHelper

#postID, postTitle, postCategory, postContent, postDat
class PostPageGenerator:
    def __init__(self):
        self.DB = GalleryDatabaseHelper()
        self.Factory = HTMLFactory()
        self.posts = self.DB.getAllPosts()
        self.postsHTML = self.__getHTMLPosts()
        print(self.postsHTML)