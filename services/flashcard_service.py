from models.flashcard import Flashcard
from utils.database import db
from utils.error import AppError
from decorators import AuthDecorator

class FlashCardService:
    
    @staticmethod
    @AuthDecorator.jwt_auth
    def get_flashcards(folder_id):
        try:
            flashcards = Flashcard.query.filter_by(folder_id=folder_id).all()
            return [flashcard.to_dict() for flashcard in flashcards]
        except Exception as e:
            raise AppError(getattr(e, 'message', 'Unknow Error'), getattr(e, 'statusCode', 400))

    @staticmethod
    @AuthDecorator.jwt_auth
    def create_flashcard(folder_id, flashcard):
        try:
            new_flashcard = Flashcard(folder_id=folder_id, question=flashcard["question"], answer=flashcard["answer"])
            db.session.add(new_flashcard)
            db.session.commit()
            return new_flashcard.to_dict()
        except Exception as e:
            raise AppError(getattr(e, 'message', 'Unknow Error'), getattr(e, 'statusCode', 400))

    @staticmethod
    @AuthDecorator.jwt_auth
    def update_flashcard(id, flashcard):
        try:
            old_flashcard = Flashcard.query.filter_by(id=id).first()
            if old_flashcard:
                old_flashcard.question = flashcard["question"]
                old_flashcard.answer = flashcard["answer"]
                db.session.commit()
                return old_flashcard.to_dict()
        except Exception as e:
            raise AppError(getattr(e, 'message', 'Unknow Error'), getattr(e, 'statusCode', 400))

    @staticmethod
    @AuthDecorator.jwt_auth
    def delete_flashcard(id):
        try:
            flashcard = Flashcard.query.filter_by(id=id).first()
            if flashcard:
                db.session.delete(flashcard)
                db.session.commit()
                return flashcard.to_dict()
        except Exception as e:
            raise AppError(getattr(e, 'message', 'Unknow Error'), getattr(e, 'statusCode', 400))
