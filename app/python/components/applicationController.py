from .componentController import ComponentController
from ..database.databaseController import DatabaseController
from .post import Post
from .comment import Comment
from .imagePost import ImagePost
from .project import Project
from .imageFormatter import ImageFormatter
import sqlite3

class ApplicationController:
    def __init__(self):
        self.DB = sqlite3.connect('test.db', check_same_thread=False)
        self.DBController = DatabaseController()
        self.PostController = self.initializeComponentController("post",Post())
        self.CommentController = self.initializeComponentController("comment", Comment())
        self.ImagePostController = self.initializeComponentController("imagePost", ImagePost())
        self.ProjectController = self.initializeComponentController("project",Project())

    def initializeComponentController(self,component, componentClass):
        componentCount = self.DBController.decideOperation(component,"count")

        if componentCount != None and componentCount > 0:
            return ComponentController(0,componentCount,self.DBController.decideOperation(component,"read",0))

        return ComponentController(-1,-1,componentClass)
            

