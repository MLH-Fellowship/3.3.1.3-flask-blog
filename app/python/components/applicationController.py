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
        self.DB = self.initializeDatabase()
        self.DBController = DatabaseController()
        self.PostController = self.initializeComponentController("post",Post())
        self.CommentController = self.initializeComponentController("comment", Comment())
        self.ProjectController = self.initializeComponentController("project",Project())

    def initializeComponentController(self,component, componentClass):
        componentCount = self.DBController.decideOperation(component,"count",componentClass, self.DB)
        print(componentCount, component)

        if componentCount != None and componentCount > 0:
            return ComponentController(0,componentCount,self.DBController.decideOperation(component,"read",0, self.DB))

        return ComponentController(-1,-1,componentClass)


    def initializeDatabase(self):
        DB = sqlite3.connect('database.db',check_same_thread=False)
        cursor = DB.cursor()
        postQuery = \
        """
            CREATE TABLE IF NOT EXISTS Post(
                postID iNTEGER PRIMARY KEY AUTOINCREMENT,
                postTitle TEXT NOT NULL,
                postContent TEXT NOT NULL,
                postCategory VARCHAR(2) NOT NULL,
                postDate DATE NOT NULL,
                postLikeCount INT NOT NULL,
                postCommentCount INT NOT NULL
            );
        """

        commentQuery = \
        """
            CREATE TABLE IF NOT EXISTS Comment(
 	            commentID iNTEGER PRIMARY KEY AUTOINCREMENT,
  	            commentAuthor TEXT NOT NULL,
  	            commentContent TEXT NOT NULL,
  	            commentDate DATE NOT NULL
            );
        """

        projectQuery = \
        """
        CREATE TABLE IF NOT EXISTS Project(
            projectID iNTEGER PRIMARY KEY AUTOINCREMENT,
            projectName TEXT NOT NULL,
            projectDescription TEXT NOT NULL,
            projectURL DATE NOT NULL,
            projectImageFile TEXT NOT NULL
        );
        """

        cursor.execute(postQuery)
        DB.commit()
        cursor.execute(commentQuery)
        DB.commit()
        cursor.execute(projectQuery)
        DB.commit()
        return DB
            

