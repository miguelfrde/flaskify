#Welcome to flaskify!

The idea behind flaskify is to have an automated tool that helps you every time you need to create a Flask project.

Right now it creates a folder structure as follows:

.DemoProject/
<br />…ENV
<br />……(a_virtualenv)
<br />…SRC
<br />……app.py
<br />……models/
<br />……templates/
<br />………img/
<br />………fonts/
<br />………js/
<br />…………script.js
<br />………css/
<br />…………style.css
<br />………base.html

If the option --bootstrap is activated, then the latest version of Bootstrap is downloaded and the bootstrap files (js, css, fonts) are moved to their corresponding directory inside templates.

The base.html and app.py contain a basic boilerplate for each one.

This is just the beginning of the idea, fork and hack!


##License

This work is under the MIT OS License:

Copyright (c) 2013 Ismael Serratos <iaserrat@me.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.