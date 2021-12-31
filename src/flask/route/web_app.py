from flask import Blueprint, render_template

bp = Blueprint('web', __name__)
bp_name = __name__
@bp.route('/sample')
def sample():
    return render_template('index.html') 
