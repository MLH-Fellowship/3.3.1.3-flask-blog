from .imageFormatter import ImageFormatter

class ImagePost:
    def __init__(self,imageID = -1, imageFile = "", imageTitle = "", imageDescription = "", imagePostDate = ""):
        self.imageID = imageID
        self.imageFile = imageFile
        self.imageTitle = imageTitle
        self.imageDescription = imageDescription
        self.imagePostDate = imagePostDate
    
    def setPost(self,imagePost):
        self.imageID = imagePost.imageID
        self.imageFile = imagePost.mageFile
        self.imageTitle = imagePost.imageTitle
        self.imageDescription = imagePost.imageDescription
        self.imagePostDate = imagePost.imagePostDate