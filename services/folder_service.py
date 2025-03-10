from models.folder import Folder
from models.user import User
from utils.database import db
from utils.error import AppError
from decorators import AuthDecorator
from flask import g
class FolderService:
    
    @staticmethod
    @AuthDecorator.jwt_auth
    def get_folders():
        try:
            email = g.user['email']
            user_subquery = User.query.with_entities(User.id).filter_by(email=email).subquery()
            folders = Folder.query.filter(Folder.user_id == user_subquery).all()
            return [folder.to_dict() for folder in folders]
        except Exception as e:
            raise AppError(getattr(e, 'message', 'Unknow Error'), getattr(e, 'statusCode', 400))
        
    @staticmethod
    @AuthDecorator.jwt_auth
    def create_folder(folder):
        try:
            email = g.user['email']
            user_id = User.query.with_entities(User.id).filter_by(email=email).scalar()
            new_folder = Folder(user_id=user_id, name=folder["name"], description=folder["description"])
            db.session.add(new_folder)
            db.session.commit()
            return new_folder.to_dict()
        except Exception as e:
            raise AppError(getattr(e, 'message', 'Unknow Error'), getattr(e, 'statusCode', 400))
    
    @staticmethod
    @AuthDecorator.jwt_auth
    def update_folder(id, folder):
        try:
            old_folder = Folder.query.filter_by(id=id).first()
            if old_folder:
                old_folder.name = folder["name"]
                old_folder.description = folder["description"]
                db.session.commit()
                return old_folder.to_dict()
        except Exception as e:
            raise AppError(getattr(e, 'message', 'Unknow Error'), getattr(e, 'statusCode', 400))

    @staticmethod
    @AuthDecorator.jwt_auth
    def delete_folder(id):
        try:
            folder = Folder.query.filter_by(id=id).first()
            if folder:
                db.session.delete(folder)
                db.session.commit()
                return folder.to_dict()
        except Exception as e:
            raise AppError(getattr(e, 'message', 'Unknow Error'), getattr(e, 'statusCode', 400))