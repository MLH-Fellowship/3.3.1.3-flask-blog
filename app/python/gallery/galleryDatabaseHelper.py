import sqlite3
from .image import Image
from string import Template

class GalleryDatabaseHelper:
    def __init__(self):
        self.DB = sqlite3.connect('test.db', check_same_thread=False)
        self.cursor = self.DB.cursor()
        self.cursor.execute("""
        create table IF NOT EXISTS image(
	        imageID int auto_increment primary key,
            imageCode blob,
            imageTitle text,
            imageDescription text
        );""")
        self.DB.commit()
    
    def getAllImages(self):
        images = []
        query = \
        """
            SELECT * FROM image
        """
        self.cursor.execute(query)
        for element in self.cursor:
            imageID, imageFile, imageTitle, imageDescription = element
            images.append(Image(imageID, imageFile, imageTitle, imageDescription))
        return images

    def addImage(self, image):
        query = (
            """
                INSERT INTO image(imageCode, imageTitle, imageDescription) VALUES(?,?,?)
            """
        )
        code = image.imageFile
        title = image.imageTitle
        description = image.imageDescription
        self.cursor.execute(query,(code,title,description))
        self.DB.commit()
        image.imageID = self.getImageID(image)
        return image

    def getImageID(self, image):
        query = Template(
        """
        SELECT imageID FROM image
        WHERE imageCode = "$imageCode" and imageTitle = "$imageTitle" and imageDescription = "$imageDescription"
        """)

        code = image.imageFile
        title = image.imageTitle
        description = image.imageDescription
        self.cursor.execute(query.substitute({'imageCode': code, 'imageTitle':title, 'imageDescription': description}))
        for row in self.cursor:
            return row[0]