from flask import Blueprint, request
from controllers.flashcard_controller import FlashCardController

flashcard_blueprint = Blueprint("flashcard", __name__)
controller = FlashCardController()

@flashcard_blueprint.route("/<folder_id>", methods=["GET"], endpoint="get_flashcards")
def get_folders(folder_id):
    return controller.get_flashcards(folder_id)

@flashcard_blueprint.route("/<folder_id>", methods=["POST"], endpoint="create_flashcard")
def create_flashcard(folder_id):
    flashcard_data = request.json
    return controller.create_flashcard(folder_id, flashcard_data)
    

@flashcard_blueprint.route("/<id>", methods=["PUT"], endpoint="update_flashcard")
def update_folder(id):
    if request.method == "PUT":
        flashcard_data = request.json
        return controller.update_flashcard(id, flashcard_data)

@flashcard_blueprint.route("/<id>", methods=["DELETE"], endpoint="delete_flashcard")
def update_folder(id):
    return controller.delete_flashcard(id)
