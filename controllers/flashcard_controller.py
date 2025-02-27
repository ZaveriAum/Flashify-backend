from services.flashcard_service import FlashCardService
from flask import jsonify

class FlashCardController:
    
    @staticmethod
    def get_flashcards(folder_id):
        try:
            flashcards = FlashCardService.get_flashcards(folder_id)
            return jsonify({
                "message": "Flashcards retrieved successfully",
                "flashcards":flashcards
                }), 200
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), getattr(e, "statusCode", 400)

    @staticmethod
    def create_flashcard(folder_id, flashcard_data):
        try:
            flashcard = FlashCardService.create_flashcard(folder_id, flashcard_data)
            return jsonify({
                "message": "Flashcard created successfully",
                "flashcard":flashcard
                }), 201
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), getattr(e, "statusCode", 400)

    @staticmethod
    def update_flashcard(id, flashcard_data):
        try:
            updated_flashcard = FlashCardService.update_flashcard(id, flashcard_data)
            return jsonify({
                "message": "Flashcard updated successfully",
                "updated flashcard": updated_flashcard
                }), 200
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), getattr(e, "statusCode", 400)

    @staticmethod
    def delete_flashcard(id):
        try:
            deleted_flashcard = FlashCardService.delete_flashcard(id)
            return jsonify({
                "message": "Flashcard deleted successfully",
                "deleted flashcard": deleted_flashcard
                }), 204
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), getattr(e, "statusCode", 400)
