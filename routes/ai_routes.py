from flask import Blueprint, request, jsonify
from controllers.ai_controller import AIController

ai_blueprint = Blueprint("ai", __name__)
controller = AIController()

@ai_blueprint.route("/", methods=["POST"])
def generate():
    data = request.json
    return controller.generate_flashcards(data)

@ai_blueprint.route("/<folder_id>", methods=["POST"])
def interact(folder_id):
    data = request.json
    return controller.interact_with_flashcards(folder_id, data)
