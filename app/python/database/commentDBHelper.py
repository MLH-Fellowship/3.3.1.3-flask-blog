from .databaseTemplate import DatabaseTemplate
from app.python.components.comment import Comment
class CommentDBHelper(DatabaseTemplate):

    def createHelper(self, DB, comment):
        cursor =  DB.cursor()
        author = comment.commentAuthor
        content = comment.commentContent
        date = comment.commentDate
        query = "INSERT INTO Comment(commentAuthor, commentBody, commentDatetCount) VALUES "
        query += '("' + title + '","' + content +  '","' + date + ');'
        cursor.execute(query)
        DB.commit()

    def readHelper(self, DB, Info):
        Index, postID = Info
        cursor = DB.cursor()
        query = "SELECT * FROM comment where postID = " + str(postID) + " LIMIT 1 OFFSET " + str(Index)
        cursor.execute(query) 
        for row in cursor:
            cID, author, content,date = row
            return Comment(cID, author, content,date)

    def updateHelper(self, DB,comment):
        pass
        #need to implement this
    
    def deleteHelper(self, DB,comment):
        cursor = DB.cursor()
        commentID = comment.commentID
        query = "DELETE FROM comment WHERE commentID = " + str(commentID)
        cursor.execute(query)
        DB.commit()

    def countHelper(self, DB, comment):
        cursor = DB.cursor()
        query = "SELECT COUNT(commentID) FROM comment"
        cursor.execute(query)
        for row in cursor:
            return row[0]