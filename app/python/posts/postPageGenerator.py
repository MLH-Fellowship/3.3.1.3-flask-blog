from post import Post
from HTMLPostFactory import HTMLPostFactory
from postDatabaseHelper import PostDatabaseHelper

#postID, postTitle, postCategory, postContent, postDat
class PostPageGenerator:
    def __init__(self):
        self.DB = PostDatabaseHelper()
        self.Factory = HTMLPostFactory()
        self.posts = self.DB.getAllPosts()
        self.postsHTML = self.__getHTMLPosts()

    #def updatePost

    def filterPosts(self, category):
        filterResult = []
        for index in range(len(self.posts)):
            if self.posts[index].postCategory == category:
                filterResult.append(self.postsHTML[i])
        return self.__HTMLArrayToString(filterResult)

    def deletePost(self,postIndex):
        postToDelete = self.posts.pop(postIndex)
        startingNewIndex = postToDelete.arrayIndex + 1
        self.postsHTML.pop(postIndex)

        for index in range( startingNewIndex , len(self.post) ):
            self.post[index].arrayIndex -= 1

        self.postsHTML = self.__getHTMLPosts()
        self.DB.deletePost(postToDelete)
        return self.__HTMLArrayToString( self.postsHTML )

    def __getHTMLPosts(self):
        postsHTML = []
        for post in self.posts:
            postsHTML.append(self.Factory.createHTMLPost(post))
        return postsHTML

    def __HTMLArrayToString(self):
        htmlText = ""
        for element in self.postsHTML:
            htmlText += element
        return htmlText

for post in PostDatabaseHelper().getAllPosts():
    print(post.postTitle)