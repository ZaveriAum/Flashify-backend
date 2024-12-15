from utils.database import db

class Flashcard(db.Model):
    __tablename__ = "flashcards"

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    folder_id = db.Column(db.Integer, db.ForeignKey("folders.id"), nullable=False)

    def __init__(self, question, answer, folder_id):
        self.question = question
        self.answer = answer
        self.folder_id = folder_id

    def to_dict(self):
        return {
            "id": self.id,
            "question": self.question,
            "answer": self.answer,
            "folder_id": self.folder_id,
        }
