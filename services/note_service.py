from models.note import Note
from utils.database import db
from utils.error import AppError
from decorators import AuthDecorator

class NoteService:

    @staticmethod
    def get_note_content(note_id):
        try:
            note = Note.query.filter_by(id=note_id).first()
            return note.to_dict()
        except Exception as e:
            raise AppError("Unknow Error", 500)

    @staticmethod
    @AuthDecorator.jwt_auth
    def get_notes(folder_id):
        try:
            notes = Note.query.filter_by(folder_id=folder_id).all()
            return [Note.to_dict() for note in notes]
        except Exception as e:
            raise AppError(getattr(e, 'message', 'Unknow Error'), getattr(e, 'statusCode', 400))

    @staticmethod
    @AuthDecorator.jwt_auth
    def create_note(folder_id, note):
        try:
            new_note = Note(folder_id=folder_id, title=note["title"], note=note["note"])
            db.session.add(new_note)
            db.session.commit()
            return new_note.to_dict()
        except Exception as e:
            raise AppError(getattr(e, 'message', 'Unknow Error'), getattr(e, 'statusCode', 400))

    @staticmethod
    @AuthDecorator.jwt_auth
    def update_note(id, note):
        try:
            old_note = Note.query.filter_by(id=id).first()
            if old_note:
                old_note.title = note["title"]
                old_note.note = note["note"]
                db.session.commit()
                return old_note.to_dict()
        except Exception as e:
            raise AppError(getattr(e, 'message', 'Unknow Error'), getattr(e, 'statusCode', 400))

    @staticmethod
    @AuthDecorator.jwt_auth
    def delete_note(id):
        try:
            note = Note.query.filter_by(id=id).first()
            if note:
                db.session.delete(note)
                db.session.commit()
                return note.to_dict()
        except Exception as e:
            raise AppError(getattr(e, 'message', 'Unknow Error'), getattr(e, 'statusCode', 400))
