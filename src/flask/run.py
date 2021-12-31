import glob
import os
import yaml
from flask import Flask, render_template, blueprints
#route_import
from route import web_app
from route import mockup

app = Flask(__name__)

#route_register
app.register_blueprint(web_app.bp)
app.register_blueprint(mockup.bp)
@app.route('/')
def hello():
    #return name
    strtitle = 'sample_title'
    return render_template('html/index.html',strtitle=strtitle) 


if __name__ == "__main__":
    app.run(debug=True)