import os
from flask import Flask, render_template, send_from_directory, request
from dotenv import load_dotenv
from app.python.posts.postPageGenerator import PostPageGenerator

load_dotenv()
app = Flask(__name__)

postGenerator = PostPageGenerator()
@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/blog')
def blog():
    postIndex = postGenerator.postIndex
    post = postGenerator.posts[postIndex]
    likeCount = post.postLikeCount
    comment = post.postCommentCount
    title = post.postTitle
    return render_template('blogEntry.html', postTitle = title, LikeCount = likeCount)

@app.route("/nextPost")
def loadNextPost():
    postIndex = postGenerator.postIndex
    postIndex = postIndex + 1 if postIndex  + 1 < len(postGenerator.posts) else 0
    postGenerator.postIndex = postIndex
    return blog()