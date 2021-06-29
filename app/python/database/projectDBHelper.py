from .databaseTemplate import DatabaseTemplate
from app.python.components.project import Project

class ProjectDBHelper(DatabaseTemplate):

    def createHelper(self, DB, project):
        cursor =  DB.cursor()
        name = project.projectName
        description = project.projectDescription
        url = project.projectURL
        file = project.projectImageFile
        query = "INSERT INTO ImagePost(projectName, projectDescription, projectURl, projectFile) VALUES "
        query += '("' + name + '","' + description +  '","' + url + ',' + file + ');'
        cursor.execute(query)
        DB.commit()

    def readHelper(self, DB, Index):
        cursor = DB.cursor()
        query = "SELECT * FROM post LIMIT 1 OFFSET " + str(Index )
        cursor.execute(query) 
        for row in cursor:
            ipID, file, title, description = row
            return ImagePost(ipID, file, title,description)

    def updateHelper(self, DB,project):
        pass
        #need to implement this
    
    def deleteHelper(self, DB,project):
        cursor = DB.cursor()
        projectID = project.projectID
        query = "DELETE FROM projectPost WHERE projectID = " + str(projectID)
        cursor.execute(query)
        DB.commit()

    def countHelper(self, DB, comment):
        cursor = DB.cursor()
        query = "SELECT COUNT(projectID) FROM project"
        cursor.execute(query)
        for row in cursor:
            return row[0]