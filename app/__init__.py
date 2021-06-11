import os
from flask import Flask, render_template, send_from_directory, request
from dotenv import load_dotenv
from app.python.posts.postPageGenerator import PostPageGenerator
from app.python.posts.comment import Comment
from app.python.posts.post import Post

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
    currentComment = commentIndex + 1
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

@app.route("/commentForm", methods=["GET", "POST"])
def addCommentForm():
    return render_template("addComment.html")

@app.route("/postForm", methods=["GET", "POST"])
def addPostForm():
    return render_template("addPost.html")

@app.route("/createComment", methods=["GET", "POST"])
def createComment():
    author = request.form["commentAuthor"]
    date = request.form["commentDate"]
    body = request.form["commentBody"]
    postID = postGenerator.posts[postGenerator.postIndex].postID
    arrayIndex = len(postGenerator.postComments)
    commentToAdd = Comment(arrayIndex, author, body, date, postID)
    postGenerator.addComment(commentToAdd)
    return blog()

@app.route("/createPost", methods = ["GET", "POST"])
def createPost():
    title = request.form["postTitle"]
    category = request.form["postCategory"]
    date = request.form["postDate"]
    body = request.form["postBody"]
    arrayIndex = len(postGenerator.postComments)
    postToAdd = Post(arrayIndex, -1, title, body, category, date)
    postGenerator.addPost(postToAdd)
    return blog()

