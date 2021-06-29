from .commentDBHelper import CommentDBHelper
from .postDBHelper import PostDBHelper
from .projectDBHelper import ProjectDBHelper
from .imagePostDBHelper import ImagePostDBHelper

class DatabaseController:
    def __init__(self):
        self.commentDB = CommentDBHelper()
        self.postDB = PostDBHelper()
        self.imagePostDB = ImagePostDBHelper()
        self.projectDB = ProjectDBHelper()

    def decideOperation(self, elementType, functionType, element, sqliteDatabase, index = -1):
        
        dbToCall = None

        if elementType == "post":
            dbToCall = self.postDB

        elif elementType == "comment":
            dbToCall = self.commentDB

        elif elementType == "imagePost":
            dbToCall = self.imagePostDB

        elif elementType == "project":
            dbToCall = self.projectDB
        
        else:
            print("Failed lol", elementType)
            return
        
        if functionType == "create":
            dbToCall.create(sqliteDatabase, element)
            
        elif functionType == "read":
            return dbToCall.read(sqliteDatabase, element,index)

        elif functionType == "update":
            dbToCall.update(sqliteDatabase, element)
        
        elif functionType == "delete":
            dbToCall.delete(sqliteDatabase, element)

        elif functionType == "count":
            return dbToCall.count(sqliteDatabase,element)