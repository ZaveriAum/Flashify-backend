from flask import Blueprint, request
from controllers.note_controller import NoteController

note_blueprint = Blueprint("note", __name__)
controller = NoteController()

@note_blueprint.route("/<folder_id>", methods=["GET"], endpoint="get_notes")
def get_notes(folder_id):
    return controller.get_notes(folder_id)

@note_blueprint.route("/<folder_id>", methods=["POST"], endpoint="create_note")
def create_note(folder_id):
    note_data = request.json
    return controller.create_note(folder_id, note_data)
    

@note_blueprint.route("/<id>", methods=["PUT"], endpoint="update_note")
def update_note(id):
    if request.method == "PUT":
        note_data = request.json
        return controller.update_note(id, note_data)

@note_blueprint.route("/<id>", methods=["DELETE"], endpoint="delete_note")
def update_note(id):
    return controller.delete_note(id)
