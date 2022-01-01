from db.model.user import User
from flask import Blueprint

bp = Blueprint('user_router', __name__ , url_prefix='/user')

@bp.route('/<int:id>',method=['GET'])
def user(id):
    user = User.searchBy(id)
    print(user)