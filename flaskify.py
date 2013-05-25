import sys
import os
import traceback

from optparse import OptionParser

class APPINIT:
    @staticmethod
    def getBoilerplate(appName):
        return """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>%s</title>
    <link rel="stylesheet" href="css/style.css">
    <script src="js/script.js"></script>
    <!--[if lt IE 9]>
        <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
</head>
<body>

</body>
</html>"""%(appName)

    @staticmethod
    def getInitApp():
        return """
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()"""

class Flaskify:
    def __init__(self, path):
        self.globalPath = path
        if os.path.isabs(path):
            self.appName = os.path.basename(path)
        else:
            self.appName    = path
        self.paths      = ( "ENV", 
                            "SRC", 
                            "SRC/models",
                            "SRC/templates",
                            "SRC/templates/js",
                            "SRC/templates/css")

    def createFolderTree(self):
        try:
            if not os.path.exists(self.globalPath):
                os.makedirs(self.globalPath)
                os.chdir(self.globalPath)
                for path in self.paths:
                    os.makedirs(path)
                return True
            else:
                print "[ERROR]: Path already exists."
                return False
        except:
            print str(traceback.format_exc())
            return False

    def createEnv(self):
        try:
            print "Making virtualenv..."
            os.system("virtualenv %s"%self.paths[0])
            print "Done making virtualenv"
            return True
        except:
            print str(traceback.format_exc())
            return False

    def createFiles(self):
        try:
            print "Creating starter files..."

            baseApp      = open("%s/app.py"%self.paths[1], "wb")
            baseApp.write(APPINIT.getInitApp())
            baseApp.close()

 
            baseTemplate = open("%s/base.html"%self.paths[3], "wb")
            baseTemplate.write(APPINIT.getBoilerplate(self.appName))
            baseTemplate.close()

            baseJs       = open("%s/script.js"%self.paths[4], "wb")
            baseJs.close()

            baseCss      = open("%s/style.css"%self.paths[5], "wb")
            baseCss.close()
            print "Done creating starter files"
            return True
        except:
            print str(traceback.format_exc())
            return False

def doFlaskify():
    parser = OptionParser()
    parser.add_option(
            "-a",
            "--app",
            dest = "appName",
            default = None,
            metavar = "<STR>",
            help = "Set the app name, include the full path."
        )

    (args, options) = parser.parse_args()
    
    newApp = Flaskify(args.appName)
    if newApp.createFolderTree():
        print "%s paths were created successfully! :) Happy Coding!"%args.appName
        newApp.createEnv()
        newApp.createFiles()

if __name__ == '__main__':
    doFlaskify()