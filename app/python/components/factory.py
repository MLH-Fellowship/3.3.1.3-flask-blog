from flask import url_for
class Factory:
    
    def createBlogPreview(self,posts):
        body = """
        <head>

            <meta charset="utf-8">
            <title>Jobegiar99's Blog</title>
            <meta name="description" content="The HTML5 Herald">
            <meta name="author" content="SitePoint">
            <meta content="width=device-width, initial-scale=1" name="viewport" />
            <link rel="stylesheet" href="../static/styles/blogPreview.css">
            <link 
                rel="stylesheet" 
                href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" 
                integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" 
                crossorigin="anonymous"
            >

        </head>

        <body class = "container fluid" id = "blogEntryContainer">
            <div class = "row">
                <div 
                    class = "col-12 content"
                    align = "center"
                    
                >
                    <a href = """ + url_for('addPostForm') + """ style = "font-size: 1.5vw; color:black">
                        <img class = "img-fluid" src = "../static/img/blogContentBackground.png"/>
                        <div class = "createContainer" style = "font-size: 70%; top: 49%; left: 51%">
                            Create Post

                        </div>
                    </a>
                
                </div>
            </div>
            <div class = "row" style = "overflow: auto; max-height: 80vh;">
  
        """
        for post in posts:
            content = post.content
            title = post.title
            date = post.date
            body += \
            """
            <div class = "col-12 titlePrev"  >
                <div 
                    class = "content" 
                    align = "center" 
                    style = "font-size: 1vw;"
                    
                >
                    <img class = "img-fluid imageHolder" src = "../static/img/blogContentBackground.png"/>
                        <div class = "dateContainer">""" + str(date) + """</div>
                     <a method = "get" style = "color:black" 
                        href = """ + url_for('postView', id = post.id, postTitle=title, postContent=content, postDate=date) + """>
                       
                        <div class = "titleContainer">
                            """ + title + """
                    </a>
                </div>
            </div>
            """

        
        body += \
        """
                                  
            </div>
        </body>

        """
        return body

    def createProjectPreview(self,projects):
        body = \
        """
        <head>

            <meta charset="utf-8">
            <title>Jobegiar99's Blog</title>
            <meta name="description" content="The HTML5 Herald">
            <meta name="author" content="SitePoint">
            <meta content="width=device-width, initial-scale=1" name="viewport" />
            <link rel="stylesheet" href="../static/styles/projectPreview.css">
            <link 
                rel="stylesheet" 
                href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" 
                integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" 
                crossorigin="anonymous"
            >

        </head>

        <body class = "container fluid" id = "blogEntryContainer">
            <div class = "row">
                <div 
                    class = "col-12 content"
                    align = "center"
                    
                >
                    <a href= """ + url_for('addProjectForm') + """ style = "font-size: 1.5vw; color:black">
                        <img class = "img-fluid" src = "../static/img/blogContentBackground.png"/>
                        <div class = "createContainer h1" style = " top: 49%; left: 50%">
                            Add Project
                        </div>
                    </a>
                



                </div>
            </div>
            <div class = "row" style = "overflow: auto; max-height: 80vh;">
        """

        for project in projects:
            name = project.name
            shortDescription = project.shortDescription
            gif = project.gif
            videoURL = project.videoUrl
            description = project.description
            githubURL = project.githubURL
            demoURL = project.demoURL

            body += """
            <div class = "col-xs-6 col-m-4 col-xl-4 titlePrev" align = "center">
                <br>
                <div class="card" style="width: 100%; border-radius: 0px; color: white;  box-shadow: 10px 10px 20px black; text-shadow: 2px 2px 2px black;">
                    <img class="card-img-top" src="../static/img/""" + gif + """" alt="Card image cap">
                    <div class="card-body">
                        <div align = "center">
                            <h5 class="card-title">""" + name + """</h5>
                            <p class="card-text">""" + shortDescription + """</p>
                            <a href=""" + url_for('projectBigView', id = project.id, projectName = name, videoURL = videoURL, description = description, githubURL = githubURL, demoURL = demoURL) + """  class="btn btn-dark" style = " border-radius: 0px;">Check this Project</a>
                        </div>
                    </div>
                </div>
            </div> 
            """
        
        body += \
        """
           </div>
            <br>
            
        </div>
            
        </body>
        """
        return body