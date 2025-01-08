from services.ai_service import AIService
from flask import jsonify

class AIController:
    
    @staticmethod
    def generate_flashcards(data):
        try:
            topic = data.get('topic')
            text = data.get('text')
            flashcards = AIService.generate_flashcards(topic, text)
            return jsonify({
                "status": True,
                "flashcards": flashcards["flashcards"],
            }), 200
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            }), 400

    @staticmethod
    def interact_with_flashcards(folder_id, data):
        try:
            prompt = data.get('prompt')
            response = AIService.interact_with_flashcard(folder_id, prompt)
            return jsonify({
                "status": True,
                "response": response,
            }), 200
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            }), 400
