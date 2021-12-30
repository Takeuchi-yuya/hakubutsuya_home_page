import glob
import os
from flask import Flask, render_template, Blueprint
from route import web_app
app = Flask(__name__)

app.register_blueprint(web_app.bp)

@app.route('/')
def hello():
    #return name
    strtitle = 'sample_title'
    return render_template('html/index.html',strtitle=strtitle) 


if __name__ == "__main__":
    app.run(debug=True)