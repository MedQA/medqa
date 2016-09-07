from app.extensions import db


class Testimonials(db.Model):
    __tablename__ = 'testmonials'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250),nullable=False)
    description = db.Column(db.Text(),nullable=False)
    upvotes = db.Column(db.Integer,nullable=True)
    downvotes = db.Column(db.Integer,nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
