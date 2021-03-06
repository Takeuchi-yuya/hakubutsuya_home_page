from db.database import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def searchBy(id):
        return db.session.query(User).filter(User.id == id).one()