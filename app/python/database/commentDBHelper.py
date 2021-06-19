from .databaseTemplate import DatabaseTemplate

class CommentDBHelper(DatabaseTemplate):

    def createHelper(DB, comment):
        cursor =  DB.cursor()
        author = comment.commentAuthor
        content = comment.commentContent
        date = comment.commentDate
        query = "INSERT INTO Comment(commentAuthor, commentBody, commentDatetCount) VALUES "
        query += '("' + title + '","' + content +  '","' + date + ');'
        cursor.execute(query)
        DB.commit()

    def readHelper(DB, Info):
        Index, postID = Info
        cursor = DB.cursor()
        query = "SELECT * FROM comment where postID = " + str(postID) + " LIMIT 1 OFFSET " + str(Index)
        cursor.execute(query) 
        for row in cursor:
            cID, author, content,date = row
            return Comment(cID, author, content,date)

    def updateHelper(DB,comment):
        pass
        #need to implement this
    
    def deleteHelper(DB,comment):
        cursor = DB.cursor()
        commentID = comment.commentID
        query = "DELETE FROM comment WHERE commentID = " + str(commentID)
        cursor.execute(query)
        DB.commit()

    def countHelper(DB, comment):
        cursor = DB.cursor()
        query = "SELECT COUNT(commentID) FROM comment"
        cursor.execute(query)
        for row in cursor:
            return row