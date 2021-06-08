import mysql.connector
from post import Post

class PostDatabaseHelper:
    def __init__(self):
        self.DB =mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="password",
                    database = "mlh"
                )
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
        self.cursor.execute("SELECT * from Post")
        posts = []
        for p in self.cursor:
            postID, postTitle, postBody, postCategory, postDate = p
            posts.append(Post(postID, postTitle, postBody, postCategory, postDate))
        return posts
