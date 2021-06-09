from post import Post

class HTMLPostFactory:
    def __init__(self):
        self.idTemplateOpening =\
            """
            <div id = \"
            """

        self.categoryTemplate =\
            """
            \"  class = "container fluid postContainer" style ="border: 0.1em inset black;">
                <br>
                <div class = "row postHeader">
                    <div class = "col-1 postCategory">
            """
        
        self.titleTemplate =\
            """
                    </div>

                    <div class = "col postTitle" align = "center">

            """

        self.dateTemplate =\
            """
                    </div>
                
                    <div class = "co-1 postDate">

            """

        self.bodyTemplate =\
            """
                    </div>
                </div>
                <br>
                <div class = "row postContent">
                    <p align = "center">
            """

        self.templateClosure =\
            """
                    </p>
                </div>
                <br>
            </div>
            <br>
            """

    def createHTMLPost(self, post):
        htmlPost = self.idTemplateOpening
        htmlPost += str(post.postID)
        htmlPost += self.categoryTemplate
        htmlPost += post.postCategory
        htmlPost += self.titleTemplate
        htmlPost += post.postTitle
        htmlPost += self.dateTemplate
        htmlPost += post.postDate
        htmlPost += self.bodyTemplate
        htmlPost += post.postBody
        htmlPost += self.templateClosure
        return htmlPost