from flask import Blueprint, render_template
import json

bp = Blueprint('mock', __name__, url_prefix='/mock')
bp_name = __name__
@bp.route('/')
def mock_main():
    return render_template('html/mock-main.html')
 
@bp.route('/tech-blog')
def tech_blog_main():
    return render_template('html/mock-main.html')


