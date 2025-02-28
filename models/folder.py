from utils.database import db
from marshmallow import Schema, fields, validate, ValidationError

class Folder(db.Model):
    __tablename__ = "folders"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', name="fk_folders_users"), nullable=False)

    flashcards = db.relationship('Flashcard', backref='folder', lazy=True)
    notess = db.relationship('Note', backref='folder', lazy=True)

    def __init__(self, name, description, user_id):
        self.name = name
        self.description = description
        self.user_id = user_id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }

class FolderSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=2, max=25), error_messages={"required": "Name is required", "null": "Name cannot be empty"})
    description = fields.String(required=True, validate=validate.Length(min=8, max=200), error_messages={"required": "Description is required", "null": "Description cannot be empty"})
