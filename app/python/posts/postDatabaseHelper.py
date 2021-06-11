import sqlite3
from .post import Post
from .comment import Comment
from string import Template

class PostDatabaseHelper:
    def __init__(self):
        sqlite3.enable_callback_tracebacks(True)
        self.DB = sqlite3.connect('test.db')

        self.cursor = self.DB.cursor()

    
    def insertPost(self, post):
        title = post.postTitle
        body = post.postBody
        category = post.postCategory
        date = post.postDate
        query = "INSERT INTO post(postTitle, postBody, postCategory, postDate) VALUES "
        query += '("' + title + '","' + body + '","' + category + '","' + date +'");'
        self.cursor.execute(query)
        self.DB.commit()
        self.__insertNewPostLikes(post)
    
    def deletePost(self, post):
        postToDelete = str(post.postID)
        query = "DELETE FROM post WHERE postID = " + postToDelete
        self.cursor.execute(query)
        self.DB.commit()

    def updatePost(self, post):
        title = post.postTitle
        body = post.postBody
        category = post.postCategory
        date = post.postDate
        query = "UPDATE post SET "
        query += "postTitle = " + '"' + title + '", '
        query += "postBody = " + '"' + body + '", '
        query += "postCategory = " + '"' + category + '" '
        query += "where postID = " + str(post.postID)
        self.cursor.execute(query)
        self.DB.commit()

    def getAllPosts(self):
        print("We're getting all posts!")
        self.cursor.execute("SELECT * from Post")
        postQuery = [x for x in self.cursor]
        print(postQuery)
        posts = []
        index = 0
        for post in postQuery:

            postID, postTitle, postBody, postCategory, postDate = post
            likeCount = 0
            commentCount = 0
            self.cursor.execute("SELECT likeCount from Likes WHERE postID = " + str(postID) )
            likeQuery = [x for x in self.cursor]
            likeCount = 0 if len(likeQuery) == 0 else likeQuery[0][0]

            self.cursor.execute("select COUNT(postID) from comments WHERE postID  = " + str(postID))
            commentQuery = [x for x in self.cursor]
            commentCount = 0 if len(commentQuery) == 0 else commentQuery[0][0]

            posts.append(Post(index,postID, postTitle, postBody, postCategory, postDate,likeCount,commentCount))
            
            index += 1
        return posts


    def __insertNewPostLike(self, post):
        title = post.postTitle
        body = post.postBody
        category = post.postCategory
        date = post.postDate
        query = Template(
            """
            INSERT INTO likes( postID, likeCount) VALUES
            ((SELECT postID FROM post WHERE postTitle = "$title" and postBody = "$body" and  postCategory = "$category"and postDate = "$date"),
            0)
            """)
        query = query.substitute({"title": title, "body": body, "category": category, "date": date})
        self.cursor.execute(query)
        self.DB.commit()

    def insertComment(self, post, comment):
        postID = post.postID
        commentBody = comment.commentBody
        commentDate = comment.commentDate
        commentAuthor = comment.commentAuthor
        query = Template(\
        """
        INSERT INTO comments(postID , commentBody, commentDate, commentAuthor) VALUES
        ($postID, "$commentBody", "$commentDate", "$commentAuthor")
        """)
        query = query.substitute({"postID": postID, "commentBody": commentBody, "commentDate": commentDate, "commentAuthor": commentAuthor})
        self.cursor.execute(query)
        self.DB.commit()

    def deleteComment(self, post):
        commentToDelete = str(comment.commentID)
        query = "DELETE FROM post WHERE postID = " + commentToDelete
        self.cursor.execute(query)
        self.DB.commit()

    def getAllPostComments(self,postID):
        query = "SELECT * from comments WHERE postID =" + str(postID)
        self.cursor.execute(query)
        comments = []
        index = 0
        for element in self.cursor:
            commentID, _ , commentBody , commentDate , commentAuthor  = element
            comments.append(Comment(index, commentAuthor, commentBody, commentDate, postID))

        return comments

    def addALike(self,post):
        query = "update likes set likeCount = likeCount + 1 where postID = " + str(post.postID);
        self.cursor.execute(query)
        self.DB.commit()

