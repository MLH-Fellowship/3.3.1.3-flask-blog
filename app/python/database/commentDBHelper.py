from .databaseTemplate import DatabaseTemplate

def CommentDBHelper(DatabaseTemplate):

    def createHelper(DB, comment):
        cursor =  DB.cursor()
        author = comment.commentAuthor
        content = comment.commentContent
        date = comment.commentDate
        query = "INSERT INTO Comment(commentAuthor, commentBody, commentDatetCount) VALUES "
        query += '("' + title + '","' + content +  '","' + date + ');'
        cursor.execute(query)
        DB.commit()

    def readHelper(DB, Index):
        cursor = DB.cursor()
        query = "SELECT * FROM post LIMIT 1 OFFSET " + str(Index - 1)
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

    