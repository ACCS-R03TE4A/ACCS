from flask import Flask

app = Flask(__name__,static_folder="../resources/build",static_url_path="/")