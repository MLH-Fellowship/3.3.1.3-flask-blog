class Comment:
    def __init__(commentID = -1, commentAuthor = "", commentContent = "", commentDate = ""):
        self.commentID = commentID
        self.commentAuthor = commentAuthor
        self.commentContent = commentContent
        self.commentDate = commentDate
    
    def setComment(self,comment):
        self.commentID = comment.commentID
        self.commentAuthor = comment.commentAuthor
        self.commentContent = comment.commentContent
        self.commentDate = comment.commentDate