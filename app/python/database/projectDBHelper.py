from .databaseTemplate import DatabaseTemplate

def ProjectDBHelper(DatabaseTemplate):

    def createHelper(DB, project):
        cursor =  DB.cursor()
        name = project.projectName
        description = project.projectDescription
        url = project.projectURL
        file = project.projectImageFile
        query = "INSERT INTO ImagePost(projectName, projectDescription, projectURl, projectFile) VALUES "
        query += f'(" {name} "," {description} "," {url} , {file} );'
        cursor.execute(query)
        DB.commit()

    def readHelper(DB, Index):
        cursor = DB.cursor()
        query = "SELECT * FROM post LIMIT 1 OFFSET " + str(Index - 1)
        cursor.execute(query) 
        for row in cursor:
            ipID, file, title, description = row
            return ImagePost(ipID, file, title,description)

    def updateHelper(DB,project):
        pass
        #need to implement this
    
    def deleteHelper(DB,project):
        cursor = DB.cursor()
        projectID = project.projectID
        query = "DELETE FROM projectPost WHERE projectID = " + str(projectID)
        cursor.execute(query)
        DB.commit()