import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, render_template, send_from_directory, request
from dotenv import load_dotenv
from datetime import date
from app.python.components.factory import Factory

from PIL import Image as IMG

load_dotenv()
app = Flask(__name__)


UPLOAD_FOLDER = '../app/static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.posts'
app.config ['SQLALCHEMY_BIND'] = {"projects": 'sqlite:///portfolio.projects'}
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column('postID', db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String())
    content = db.Column(db.String())  
    date = db.Column(db.Date())

    def __init__(self, title, content,date):
        self.title = title;
        self.content = content;
        self.date = date

class Projects(db.Model):
    __bind_key__ = "projects"
    id = db.Column('projectID', db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    prevImageName = db.Column(db.String())
    gifImageName = db.Column(db.String())
    githubRepoUrl = db.Column(db.String())
    youtubeVideoUrl = db.Column(db.String())

    
    def __init__(self, title, content, prevImageName, gifImageName, githubRepoUrl, youtubeVideoUrl):
        self.title = title;
        self.content = content;
        self.prevImageName = prevImageName
        self.gifImageName = gifImageName
        self.githubRepoUrl = githubRepoUrl
        self.youtubeVideoUrl = youtubeVideoUrl

db.create_all()

@app.route('/')
def index():
    return render_template('index.html', title="Jobegiar99", url=os.getenv("URL"))

@app.route('/blog')
def blog():

    return Factory().createBlogPreview(Post.query.all())

@app.route('/postView', methods = ["GET", "POST"])
def postView():
    postTitle = request.args.get("postTitle")
    postContent = request.args.get("postContent")
    postDate = request.args.get("postDate")
    return render_template("blogEntry.html", postTitle = postTitle, postContent = postContent, postDate = postDate)

@app.route("/aboutMe")
def character():
    return render_template('character.html', url=os.getenv("URL"))


@app.route("/postForm", methods=["GET", "POST"])
def addPostForm():
    return render_template("addPost.html")

@app.route("/createPost", methods = ["GET", "POST"])
def createPost():

    title = request.form["postTitle"]
    dateInfo = request.form['postDate'].split('-')
    Date = date(int(dateInfo[0]), int(dateInfo[1]), int(dateInfo[2]))
    content = request.form["postBody"]

    post = Post(title,content,Date)

    db.session.add(post)

    db.session.commit()

    return blog()

@app.route("/health")
def health():
    return "Hp: 100"