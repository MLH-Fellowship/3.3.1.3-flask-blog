from post import Post
from comment import Comment
from string import Template

class HTMLFactory:
    def __init__(self):
        self.postTemplate =Template(
            """
            <br>
            <div id = "$postID" class = "container fluid postContainer" style ="border: 0.1em inset black;">
                <br>
                <div class = "row postHeader">
                    <div class = "col-1 postCategory">
                        $postCategory
                    </div>

                    <div class = "col postTitle" align = "center">
                        $postTitle
                    </div>
                
                    <div class = "co-1 postDate">
                        $postDate
                    </div>
                </div>
                <br>
                <div class = "row postContent">
                    <p align = "center">
                        $postBody
                    </p>
                </div>
                <br>
            </div>
            <br>
        """)

        self.commentTemplate = Template(
            """
            <div id = "$commentID" class = "container fluid commentContainer" style ="border: 0.1em inset black;"> 
                <div class = "row commentDateRow">
                    <div class = "col commentAuthor" align = "left">
                        By: $commentAuthor
                    </div>
                    <div class = "col commentDateColumn" align = "right" >
                        Comment Date: $commentDate
                    </div>
                </div>
            
                <br>

                <div class = "row commentTextRow" align = "center">
                    <div class = "col commentTextBody">
                        $commentBody
                    </div>
                </div>
                <br>
            </div>
            """
        )

    def createHTMLPost(self, post):
        postID = str(post.arrayIndex) + ";" + str(post.postID)
        postCategory = post.postCategory
        postTitle = post.postTitle
        postBody = post.postBody
        postDate = post.postDate
        postDictionary = {"postID" : postID, "postCategory": postCategory, "postDate" : postDate,
                          "postTitle" : postTitle, "postBody" : postBody}
        htmlPost = self.postTemplate.substitute(postDictionary)
        return htmlPost

    def createHTMLComment(self, comment):
        commentID = comment.commentID
        commentAuthor = comment.commentAuthor
        commentDate = comment.commentDate
        commentBody = comment.commentBody
        commentDictionary = {"commentID": commentID, "commentAuthor": commentAuthor, 
                          "commentDate": commentDate, "commentBody": commentBody}
        htmlComment = self.commentTemplate.substitute(commentDictionary)
        return htmlComment