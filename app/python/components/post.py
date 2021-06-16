class Post:
    def __init__(postID = -1, postTitle = "", postContent = "", postCategory = "", postDate = "", postLikeCount = "", postCommentCount = ""):
        self.postID = postID
        self.postTitle = postTitle
        self.postCategory = postCategory
        self.postDate = postDate
        self.postLikeCount = postLikeCount
        self.postCommentCount = postCommentCount
    
    def setPost(self,post):
        self.postID = post.postID
        self.postTitle = post.postTitle
        self.postCategory = post.postCategory
        self.postDate = post.postDate
        self.postLikeCount = post.postLikeCount
        self.postCommentCount = post.postCommentCount
