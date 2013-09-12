import sys
import os
import traceback
import urllib2
import shutil

from optparse import OptionParser
from zipfile import ZipFile

BOOTSTRAP_URL = 'https://codeload.github.com/twbs/bootstrap/zip/master'

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
    def __init__(self, path, bootstrap=False):
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
                            "SRC/templates/css",
                            "SRC/templates/fonts",
                            "SRC/templates/img")

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

    def includeBootstrap(self):
        print "Downloading bootstrap..."
        response = urllib2.urlopen(BOOTSTRAP_URL)
        with open("temp.zip", "wb") as f:
            f.write(response.read())
        zip_file = ZipFile('temp.zip')
        zip_file.extractall()
        print "Done downloading bootstrap"

        print "Moving bootstrap files..."
        bdir = "bootstrap-master/dist/"
        for d in ("css/", "js/", "fonts/"):
            for fn in os.listdir(bdir + d):
                shutil.move(bdir + d + fn, "SRC/templates/" + d + fn)
        print "Done moving bootstrap files"

        print "Removing temp bootstrap files..."
        os.remove("temp.zip")
        shutil.rmtree("bootstrap-master")
        print "Done removing temp bootstrap files"
    

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
    parser.add_option(
            "-b",
            "--bootstrap",
            dest = "bootstrap",
            default = False,
            metavar = "<BOOL>",
            help = "Download and include Bootstrap"
        )

    (args, options) = parser.parse_args()
    
    newApp = Flaskify(args.appName)
    if newApp.createFolderTree():
        print "%s paths were created successfully! :) Happy Coding!"%args.appName
        newApp.createEnv()
        newApp.createFiles()
        if args.bootstrap:
            newApp.includeBootstrap()

if __name__ == '__main__':
    doFlaskify()