from models.folder import Folder
from utils.database import db

class FolderService:
    
    @staticmethod
    def get_folders(user_id):
        folders = Folder.query.filter_by(user_id=user_id).all()
        return [folder.to_dict() for folder in folders]

    @staticmethod
    def create_folder(user_id, folder):
        new_folder = Folder(user_id=user_id, name=folder["name"], description=folder["description"])
        db.session.add(new_folder)
        db.session.commit()
        return new_folder.to_dict()

    @staticmethod
    def update_folder(id, folder):
        old_folder = Folder.query.filter_by(id=id).first()
        if old_folder:
            old_folder.name = folder["name"]
            old_folder.description = folder["description"]
            db.session.commit()
            return folder.to_dict()


    @staticmethod
    def delete_folder(id):
        folder = Folder.query.filter_by(id=id).first()
        if folder:
            db.session.delete(folder)
            db.session.commit()
            return folder.to_dict()