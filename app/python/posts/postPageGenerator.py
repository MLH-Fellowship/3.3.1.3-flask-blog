from .post import Post
from .postDatabaseHelper import PostDatabaseHelper

#postID, postTitle, postCategory, postContent, postDat
class PostPageGenerator:
    def __init__(self):
        self.DB = PostDatabaseHelper()
        self.posts = self.DB.getAllPosts()
        self.postIndex = 0 if len(self.posts) > 0 else -1
        #self.postComment = self.DB.getAllPostComments(self.posts[0]) if self.postIndex > -1 else []
        #self.commentIndex = 0 if len(self.postComment) > 0 else -1

    def deletePost(self,postIndex):
        postToDelete = self.posts.pop(postIndex)
        startingNewIndex = postToDelete.arrayIndex + 1
        self.postsHTML.pop(postIndex)

        for index in range( startingNewIndex , len(self.post) ):
            self.post[index].arrayIndex -= 1

        self.DB.deletePost(postToDelete)