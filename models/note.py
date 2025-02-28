from utils.database import db

class Note(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    note = db.Column(db.Text, nullable=False)
    folder_id = db.Column(db.Integer, db.ForeignKey('folders.id', name="fk_notes_folders"), nullable=False)

    def __init__(self, title, note, folder_id):
        self.title = title
        self.note = note
        self.folder_id = folder_id

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "note": self.note,
            "folder_id": self.folder_id,
        }