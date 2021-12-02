from flaskr.app import app
from flask import send_from_directory

@app.route("/remocon")
def get_remocon():
    return send_from_directory("../resources/build", "index.html")