from services.ai_service import AIService
from flask import jsonify

class AIController:
    
    @staticmethod
    def generate_flashcards(text, file):
        try:
            flashcards = AIService.generate_flashcards(text, file)
            return jsonify({
                "flashcards": flashcards["flashcards"],
            }), 200
        except Exception as e:
            print(e)
            return jsonify({
                "message": str(e)
            }), getattr(e, "statusCode", 400)

    @staticmethod
    def interact_with_flashcards(folder_id, data):
        try:
            prompt = data.get('prompt')
            response = AIService.interact_with_flashcard(folder_id, prompt)
            return jsonify({
                "response": response,
            }), 200
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), getattr(e, "statusCode", 400)
