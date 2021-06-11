import sqlite3
from image import Image
from string import Template

class PostDatabaseHelper:
    def __init__(self, db):
        self.DB = db
        self.cursor = self.DB.cursor()
    
    def getAllImages(self):
        images = []
        query = \
        """
            SELECT * FROM image
        """
        self.cursor.execute(query)
        for element in self.cursor:
            imageID, imageCode, imageTitle, imageDescription = element
            images.append(Image(imageID, imageCode, imageTitle, imageDescription))

    def addImage(self, image):
        query = Template(
            """
                INSERT INTO image(imageCode, imageTitle, imageDescription) VALUES
                ($imageCode, $imageTitle, $imageDescription)
            """
        )
        code = image.imageCode
        title = image.imageTitle
        description = image.imageDescription
        self.cursor.execute(query.substitute({"imageCode":code, "imageTitle": title, "imageDescription": description}))
        self.DB.commit()
        image.imageID = getImageID(image)
        return image

    def getImageID(self, image):
        query = Template(
        """
        SELECT imageID FROM image
        WHERE imageCode = "$imageCode" and imageTitle = "$imageTitle" and imageDescription = "$imageDescription"
        """)

        code = image.imageCode
        title = image.imageTitle
        description = image.imageDescription
        self.cursor.execute(query.substitute({'imageCode': code, 'imageTitle':title, 'imageDescription': description}))
        for row in self.cursor:
            return row[0]