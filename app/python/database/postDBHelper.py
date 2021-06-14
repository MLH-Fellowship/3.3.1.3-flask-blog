from .databaseTemplate import DatabaseTemplate

def PostDBHelper(DatabaseTemplate):

    def createHelper(DB, post):
        cursor =  DB.cursor()
        title = post.postTitle
        content = post.postContent
        category = post.postCategory
        date = post.postDate
        query = "INSERT INTO post(postTitle, postBody, postCategory, postDate, postLikeCount, postCommentCount) VALUES "
        query += '("' + title + '","' + content + '","' + category + '","' + date +' , 0 , 0");'
        cursor.execute(query)
        DB.commit()

    def readHelper(DB, Index):
        cursor = DB.cursor()
        query = "SELECT * FROM post LIMIT 1 OFFSET " + str(Index - 1)
        cursor.execute(query) 
        for row in cursor:
            pID, title, content, category, date, likes, comments = row
            return Post(pID, title, content, category, date, likes, comments)

    def updateHelper(DB,Post):
        pass
        #need to implement this
    
    def deleteHelper(DB,Post):
        cursor = DB.cursor()
        postID = post.postID
        query = "DELETE FROM post WHERE postID = " + str(postID)
        cursor.execute(query)
        DB.commit()

    

