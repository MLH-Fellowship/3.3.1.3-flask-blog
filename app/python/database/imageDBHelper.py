from .databaseTemplate import DatabaseTemplate

def ImagePostDBHelper(DatabaseTemplate):

    def createHelper(DB, imagePost):
        cursor =  DB.cursor()
        file = imagePost.imageFile
        title = imagePost.imageTitle
        description = imagePost.imageDescription
        date = imagePost.imagePostDate
        query = "INSERT INTO ImagePost(imagePostFile, imagePostTitle, imagePostDscription, imagePostDate) VALUES "
        query += '("' + file + '","' + title +  '","' + description + ',' + date + ');'
        cursor.execute(query)
        DB.commit()

    def readHelper(DB, Index):
        cursor = DB.cursor()
        query = "SELECT * FROM post LIMIT 1 OFFSET " + str(Index - 1)
        cursor.execute(query) 
        for row in cursor:
            ipID, file, title, description = row
            return ImagePost(ipID, file, title,description)

    def updateHelper(DB,imagePost):
        pass
        #need to implement this
    
    def deleteHelper(DB,imagePost):
        cursor = DB.cursor()
        imagePostID = imagePost.imageID
        query = "DELETE FROM imagepost WHERE imageID = " + str(imagePostID)
        cursor.execute(query)
        DB.commit()