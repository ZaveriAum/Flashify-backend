from utils.database import db
from marshmallow import Schema, fields, validate, ValidationError

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(15), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }

class SignupSchema(Schema):
    username = fields.String(required=True, validate=validate.Length(min=2, max=15), error_messages={"required": "Username is required", "null": "Username cannot be empty"})
    email = fields.Email(required=True, validate=validate.Length(min=5, max=55), error_messages={"required": "Valid email is required"})
    password = fields.String(required=True, validate=validate.Length(min=8, max=20), error_messages={"required": "Password is required", "null": "Password cannot be empty"})

class LoginSchema(Schema):
    email = fields.Email(required=True, validate=validate.Length(min=5, max=55), error_messages={"required": "Valid email is required"})
    password = fields.String(required=True ,validate=validate.Length(min=8, max=20), error_messages={"required": "Password cannot be empty"})
