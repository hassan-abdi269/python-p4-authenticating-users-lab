from config import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username
        }


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    preview = db.Column(db.String)
    minutes_to_read = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "author": self.author,
            "title": self.title,
            "content": self.content,
            "preview": self.preview,
            "minutes_to_read": self.minutes_to_read
        }
