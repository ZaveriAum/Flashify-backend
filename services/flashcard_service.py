from models.flashcard import Flashcard
from utils.database import db

class FlashCardService:
    
    @staticmethod
    def get_flashcards(folder_id):
        flashcards = Flashcard.query.filter_by(folder_id=folder_id).all()
        return [flashcard.to_dict() for flashcard in flashcards]

    @staticmethod
    def create_flashcard(folder_id, flashcard):
        new_flashcard = Flashcard(folder_id=folder_id, question=flashcard["question"], answer=flashcard["answer"])
        db.session.add(new_flashcard)
        db.session.commit()
        return new_flashcard.to_dict()

    @staticmethod
    def update_flashcard(id, flashcard):
        old_flashcard = Flashcard.query.filter_by(id=id).first()
        if old_flashcard:
            old_flashcard.question = flashcard["question"]
            old_flashcard.answer = flashcard["answer"]
            db.session.commit()
            return old_flashcard.to_dict()


    @staticmethod
    def delete_flashcard(id):
        flashcard = Flashcard.query.filter_by(id=id).first()
        if flashcard:
            db.session.delete(flashcard)
            db.session.commit()
            return flashcard.to_dict()