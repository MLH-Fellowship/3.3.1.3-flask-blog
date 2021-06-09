class Post:
    def __init__(self, arrayIndex, postID , postTitle, postBody, postCategory, postDate, postLikeCount = 0, postCommentCount = 0):
        self.arrayIndex = arrayIndex
        self.postID = postID
        self.postTitle = postTitle
        self.postCategory = postCategory
        self.postBody = postBody
        self.postDate = postDate 
        self.postLikeCount = postLikeCount
        self.postCommentCount = postCommentCount