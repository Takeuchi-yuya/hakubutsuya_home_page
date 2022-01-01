import glob
import os
import yaml
from flask import Flask, render_template, blueprints
from db.database import db
#route_import
from route import user
from route import web_app
from route import mockup

app = Flask(__name__)

#route_register
app.register_blueprint(user.bp)
app.register_blueprint(web_app.bp)
app.register_blueprint(mockup.bp)

app.config.from_object('config.Config')
db.init_app(app)
@app.route('/')
def hello():
    #return name
    strtitle = 'sample_title'
    return render_template('html/index.html',strtitle=strtitle) 


if __name__ == "__main__":
    app.run(debug=True)