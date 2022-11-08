import sqlite3
from .post import Post
from .comment import Comment
from string import Template

class PostDatabaseHelper:
    def __init__(self):
        self.DB = sqlite3.connect('test.db', check_same_thread=False)

        self.cursor = self.DB.cursor()

        self.cursor.execute("""
            create table IF NOT EXISTS Post(
	            postID INTEGER  PRIMARY KEY AUTOINCREMENT,
                postTitle VARCHAR(255) NOT NULL,
                postBody TEXT NOT NULL,
                postCategory VARCHAR(2) NOT NULL,
                postDate varchar(10) NOT NULL
            ); 
        """)
        self.DB.commit()
        self.cursor.execute("""
        create table IF NOT EXISTS Likes(
	        postID INTEGER PRIMARY KEY ,
            likeCount int,
            FOREIGN KEY (postID) REFERENCES POST(postID)
        );""")
        self.DB.commit()
        self.cursor.execute("""
            create table IF NOT EXISTS Comments(
	commentID INTEGER  PRIMARY KEY AUTOINCREMENT,
	postID int ,
    commentBody varchar(255),
    commentDate varchar(10),
    commentAuthor varchar(25),
    FOREIGN KEY (postID) REFERENCES POST(postID)
); 
        """)
        self.DB.commit()

    
    def insertPost(self, post):
        title = post.postTitle
        body = post.postBody
        category = post.postCategory
        date = post.postDate
        query = "INSERT INTO post(postTitle, postBody, postCategory, postDate) VALUES "
        query += '("' + title + '","' + body + '","' + category + '","' + date +'");'
        self.cursor.execute(query)
        self.DB.commit()
        post.postID = self.getPostID(post)
        self.__insertNewPostLike(post)
    
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
        postQuery = [x for x in self.cursor]
        posts = []
        index = 0
        for post in postQuery:

            postID, postTitle, postBody, postCategory, postDate = post
            likeCount = 0
            commentCount = 0
            self.cursor.execute("SELECT likeCount from Likes WHERE postID = " + str(postID) )
            likeQuery = [x for x in self.cursor]
            likeCount = 0 if not len(likeQuery) else likeQuery[0][0]

            self.cursor.execute("select COUNT(postID) from comments WHERE postID  = " + str(postID))
            commentQuery = [x for x in self.cursor]
            commentCount = 0 if  not len(commentQuery) else commentQuery[0][0]

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

    def insertComment(self, postID, comment):
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

    def getPostID(self, post):
        query = Template(
        """
        SELECT postID FROM post
        WHERE postTitle = "$postTitle" and postDate = "$postDate" and postCategory = "$postCategory" and postBody = "$postBody"
        """)
        title = post.postTitle
        date = post.postDate
        category = post.postCategory
        body = post.postBody
        self.cursor.execute(query.substitute({'postTitle': title, 'postDate':date, 'postCategory': category, 'postBody': body}))
        for row in self.cursor:
            return row[0]