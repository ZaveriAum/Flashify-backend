from services.note_service import NoteService
from flask import jsonify, g

class NoteController:
    
    @staticmethod
    def get_notes(folder_id):
        try:
            notes = NoteService.get_notes(folder_id)
            return jsonify({
                "message": "Notes retrieved successfully",
                "notes":notes
                }), 200
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), getattr(e, "statusCode", 400)

    @staticmethod
    def create_note(folder_id, note_data):
        try:
            note = NoteService.create_note(folder_id, note_data)
            return jsonify({
                "message": "Note created successfully",
                "note":note
                }), 201
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), getattr(e, "statusCode", 400)

    @staticmethod
    def update_note(id, note_data):
        try:
            updated_note = NoteService.update_note(id, note_data)
            return jsonify({
                "message": "Note updated successfully",
                "note": updated_note
                }), 200
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), getattr(e, "statusCode", 400)

    @staticmethod
    def delete_note(id):
        try:
            deleted_note = NoteService.delete_note(id)
            return jsonify({
                "message": "Note deleted successfully",
                "note": deleted_note
                }), 204
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), getattr(e, "statusCode", 400)
