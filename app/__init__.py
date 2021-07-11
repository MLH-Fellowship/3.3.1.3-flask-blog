import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, send_from_directory, request
from dotenv import load_dotenv
from datetime import date
from app.python.components.factory import Factory
from app.python.components.adminCheck import AdminCheck
from PIL import Image as IMG
from werkzeug.utils import secure_filename

load_dotenv()
app = Flask(__name__)


UPLOAD_FOLDER = 'app\\static\\img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio_post.sqlite3'
app.config ['SQLALCHEMY_BINDS'] = {"projects": 'sqlite:///portfolio_project.sqlite3'}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column('postID', db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String())
    content = db.Column(db.String())  
    date = db.Column(db.Date())

    def __init__(self, title, content,date):
        self.title = title;
        self.content = content;
        self.date = date

class Project(db.Model):
    __bind_key__ = 'projects'
    id = db.Column('projectID', db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String())
    shortDescription = db.Column(db.String(35))
    gif = db.Column(db.String())
    videoUrl = db.Column(db.String())
    description = db.Column(db.String())
    githubURL = db.Column(db.String())
    demoURL = db.Column(db.String())

    
    def __init__(self, name, shortDescription, gif, videoUrl, description, githubURL,demoURL):
        self.name = name
        self.shortDescription = shortDescription
        self.gif = gif
        self.videoUrl = videoUrl
        self.description = description
        self.githubURL = githubURL
        self.demoURL = demoURL

db.create_all()
db.session.commit()


@app.route('/')
def index():
    return render_template('index.html', title="Jobegiar99", url=os.getenv("URL"))

@app.route('/blog')
def blog():

    return Factory().createBlogPreview(Post.query.all())

@app.route('/projects')
def projects():
    return Factory().createProjectPreview(Project .query.all())

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
    adminPassword = AdminCheck().checkIfAdmin(request.form["adminPassword"])
    if adminPassword:
        post = Post(title,content,Date)

        db.session.add(post)

        db.session.commit()

        return blog()
    return "That's not the admin password :("

@app.route("/addProjectForm")
def addProjectForm():
    return render_template("addProject.html")

@app.route("/createProject", methods = ["GET","POST"])
def createProject():
    if request.method == "POST":
        name = request.form["projectName"]
        shortDescription = request.form["projectShortDescription"]
        gif = request.files["projectGIF"]
        videoURL = request.form["projectVideoURL"]
        description = request.form["projectDescription"]
        githubURL = request.form["projectGithubURL"]
        demoURL = request.form["projectDemoURL"]
        adminPassword = AdminCheck().checkIfAdmin(request.form["adminPassword"])
        if adminPassword:
            gifName = gif.filename.replace(" ","_")
            gif.filename = gifName
            gif.save(os.path.join(UPLOAD_FOLDER,secure_filename(gif.filename)))

            project = Project(name, shortDescription, gifName, videoURL, description, githubURL,demoURL)
            db.session.add(project)
            db.session.commit()
            return projects()
    return "That's not the admin password :("

@app.route('/projectBigView', methods = ["GET","POST"])
def projectBigView():
    projectName = request.args.get("projectName")
    videoURL = request.args.get("videoURL")
    description = request.args.get("description")
    githubURL = request.args.get("githubURL")
    demoURL = request.args.get("demoURL")
    
    return render_template("projectBigView.html", projectName=projectName,projectVideoUrl=videoURL, projectDescription=description, githubURL=githubURL,demoURL = demoURL)

    
@app.route("/health")
def health():
    return "Hp: 100"
