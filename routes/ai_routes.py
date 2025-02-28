from flask import Blueprint, request, jsonify
from controllers.ai_controller import AIController

ai_blueprint = Blueprint("ai", __name__)
controller = AIController()

@ai_blueprint.route("/note", methods=["POST"], endpoint="generate_note")
def generate_note():
    text = request.form.get('text')
    file = request.files
    return controller.generate_note(text, file)

@ai_blueprint.route("/note/<note_id>", methods=["POST"], endpoint="interact_note")
def interact_note(note_id):
    data = request.json
    return controller.interact_with_note(note_id, data)

@ai_blueprint.route("/flashcard", methods=["POST"], endpoint="generate_flashcards")
def generate_flashcards():
    text = request.form.get('text')
    file = request.files
    return controller.generate_flashcards(text, file)

@ai_blueprint.route("/flashcard/<folder_id>", methods=["POST"], endpoint="interact_flashcards")
def interact_flashcards(folder_id):
    data = request.json
    return controller.interact_with_flashcards(folder_id, data)
