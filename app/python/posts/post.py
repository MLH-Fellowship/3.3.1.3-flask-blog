class Post:
    def __init__(self, arrayIndex = 0, postID =0 , postTitle = "No posts yet!", postBody = "", postCategory ="", postDate ="", postLikeCount = 0, postCommentCount = 0):
        self.arrayIndex = arrayIndex
        self.postID = postID
        self.postTitle = postTitle
        self.postCategory = postCategory
        self.postBody = postBody
        self.postDate = postDate 
        self.postLikeCount = postLikeCount
        self.postCommentCount = postCommentCount