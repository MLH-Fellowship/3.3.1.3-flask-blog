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

    def decideOperation(elementType, functionType, element, index = -1):
        
        dbToCall = None

        if elementType == "post":
            dbToCall = self.postDB

        elif elementType == "comment":
            dbToCall = self.commentDB

        elif elementType == "imagePost":
            dbToCall = self.imagePostDB

        elif: elementType == "project":
            dbToCall = self.projectDB
        
        else:
            return
        
        if functionType == "create":
            dbToCall.create(element)
            
        elif functionType == "read":
            dbToCall.read(element,index)

        elif functionType == "update":
            dbToCall.update(element)
        
        elif functionType == "delete":
            dbToCall.delete(element)

        elif functionType == "count":
            dbToCall.count(element)