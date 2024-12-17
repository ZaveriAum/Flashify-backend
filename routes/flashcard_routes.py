from flask import Blueprint, request
from controllers.flashcard_controller import FlashCardController

flashcard_blueprint = Blueprint("flashcard", __name__)
controller = FlashCardController()

@flashcard_blueprint.route("/<folder_id>", methods=["GET", "POST"])
def get_folders(folder_id):
    if request.method == "POST":
        flashcard_data = request.json
        return controller.create_flashcard(folder_id, flashcard_data)
    else:
        return controller.get_flashcards(folder_id)

@flashcard_blueprint.route("/<id>", methods=["PUT", "DELETE"])
def update_folder(id):
    if request.method == "PUT":
        flashcard_data = request.json
        return controller.update_flashcard(id, flashcard_data)
    else:
        return controller.delete_flashcard(id)
