from flask import Flask, request, redirect
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form  = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
                color: blue;
            }}
        </style>
    </head>
    <body>
      <form method="POST">

        <label for="rotate-by">Rotate by:</label>
        <input type="text" id="rot" name="rot" value="0"><br>
        <textarea  class="textarea" name="text">{0}</textarea><br>
        <input type="submit"  value="submit query">


      </form>
    </body>
</html>

"""

@app.route("/")
def index():
    return form

@app.route("/", methods=["POST"])
def encrypt():
    rotation = int(request.form["rot"])
    messege = request.form["text"]

    encrypted_messsge = rotate_string(messege, rotation)
    #return "<h1>" + encrypted_messsge + "</h1>"
    return form.format(encrypted_messsge)

app.run()