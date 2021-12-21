from flaskr.app import app
from flask import send_from_directory, redirect

@app.errorhandler(404)
def get_remocon():
    return redirect('/remocon')