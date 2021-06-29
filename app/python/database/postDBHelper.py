from .databaseTemplate import DatabaseTemplate
from app.python.components.post import Post

class PostDBHelper(DatabaseTemplate):

    def createHelper(self, DB, post):
        cursor =  DB.cursor()
        title = post.postTitle
        content = post.postContent
        category = post.postCategory
        date = post.postDate
        query = "INSERT INTO post(postTitle, postContent, postCategory, postDate, postLikeCount, postCommentCount) VALUES "
        query += '("' + title + '","' + content + '","' + category + '","' + date + '", 0 , 0);'
        cursor.execute(query)
        DB.commit()

    def readHelper(self, DB, Index):
        cursor = DB.cursor()
        query = "SELECT * FROM post LIMIT 1 OFFSET " + str(Index )
        cursor.execute(query) 
        for row in cursor:
            pID, title, content, category, date, likes, comments = row
            return Post(pID, title, content, category, date, likes, comments)

    def updateHelper(self, DB,Post):
        pass
        #need to implement this
    
    def deleteHelper(self, DB,Post):
        cursor = DB.cursor()
        postID = post.postID
        query = "DELETE FROM post WHERE postID = " + str(postID)
        cursor.execute(query)
        DB.commit()

    def countHelper(self, DB, comment):
        cursor = DB.cursor()
        query = "SELECT COUNT(postID) FROM post"
        cursor.execute(query)
        for row in cursor:
            return row[0]