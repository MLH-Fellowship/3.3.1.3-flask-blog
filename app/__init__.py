import os
from flask import Flask, render_template, send_from_directory, request
from dotenv import load_dotenv
from app.python.posts.postPageGenerator import PostPageGenerator
from app.python.posts.comment import Comment

load_dotenv()
app = Flask(__name__)

postGenerator = PostPageGenerator()
@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/blog')
def blog():
    postIndex = postGenerator.postIndex
    commentIndex = postGenerator.commentIndex
    post = postGenerator.posts[postIndex] if postIndex > -1 and postIndex < len(postGenerator.posts) else Post()
    comment = postGenerator.postComments[commentIndex] if commentIndex > -1 and commentIndex < len(postGenerator.postComments) else Comment()

    #Template
    postCategory = post.postCategory
    postTitle = post.postTitle
    postDate = post.postDate
    postBody = post.postBody
    commentAuthor = comment.commentAuthor
    commentDate = comment.commentDate
    commentBody = comment.commentBody
    LikeCount = post.postLikeCount
    currentComment = commentIndex
    totalComments = len(postGenerator.postComments)

    title = post.postTitle
    return render_template('blogEntry.html', postCategory = postCategory , 
    postTitle = title, postDate = postDate, postBody = postBody, commentAuthor = commentAuthor,\
    commentDate = commentDate, commentBody = commentBody, LikeCount = LikeCount, currentComment = currentComment, totalComments = totalComments )

@app.route("/nextPost")
def loadNextPost():
    postIndex = postGenerator.postIndex
    postIndex = postIndex + 1 if postIndex  + 1 < len(postGenerator.posts) else 0
    postGenerator.postIndex = postIndex
    print(postGenerator.commentIndex)
    postGenerator.obtainPostCommentInfo()
    print(postGenerator.commentIndex, "END")
    return blog()

@app.route("/prevPost")
def loadPrevPost():
    postIndex = postGenerator.postIndex
    postIndex = postIndex - 1 if postIndex  -1 > -1 else len(postGenerator.posts) - 1
    postGenerator.postIndex = postIndex
    print(postGenerator.commentIndex)
    postGenerator.obtainPostCommentInfo()
    print(postGenerator.commentIndex, "END")
    return blog()

@app.route("/nextComment")
def loadNextComment():
    commentIndex = postGenerator.commentIndex
    commentIndex = commentIndex + 1 if commentIndex  + 1 < len(postGenerator.postComments) else 0
    postGenerator.commentIndex = commentIndex
    return blog()

@app.route("/prevComment")
def loadPrevComment():
    commentIndex = postGenerator.commentIndex
    commentIndex = commentIndex - 1 if (commentIndex  -1) > -1 else len(postGenerator.postComments) - 1
    postGenerator.commentIndex = commentIndex
    return blog()

@app.route("/giveLove")
def giveLove():
    postIndex = postGenerator.postIndex
    post = postGenerator.posts[postIndex]
    postGenerator.DB.addALike(post)
    postGenerator.posts[postIndex].postLikeCount += 1
    return blog()
