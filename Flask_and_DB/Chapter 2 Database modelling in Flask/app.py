from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./temp_db.db'
db = SQLAlchemy(app)

app.app_context().push()

# Create database object
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    specification = db.Column(db.String(50))

    def __init__(self, name, specification):
        self.name = name
        self.specification = specification

    def __repr__(self, ):
        return "Author id {}".format(self.id)

db.create_all()

if __name__ == "__main__":
    app.run(debug=True)