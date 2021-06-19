
class Project:
    def __init__(self,projectID = -1, projectName = "", projectDescription = "", projectURL = "", projectImageFile = ""):
        self.projectID = projectID
        self.projectName = projectName
        self.projectDescription = projectDescription
        self.projectURL = projectURL
        self.projectImageFile = projectImageFile
    
    def setProject(self,project):
        self.projectID = project.projectID
        self.projectName = project.projectName
        self.projectDescription = project.projectDescription
        self.projectURL = project.projectURL
        self.projectImageFile = project.projectImageFile