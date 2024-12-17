from flask import Blueprint, request, jsonify
from controllers.folder_controller import FolderController

folder_blueprint = Blueprint("folder", __name__)
controller = FolderController()

@folder_blueprint.route("/<user_id>", methods=["GET", "POST"])
def get_folders(user_id):
    if request.method == "POST":
        folder_data = request.json
        return controller.create_folder(user_id, folder_data)
    else:
        return controller.get_folders(user_id)

@folder_blueprint.route("/<id>", methods=["PUT", "DELETE"])
def update_folder(id):
    if request.method == "PUT":
        folder_data = request.json
        return controller.update_folder(id, folder_data)
    else:
        return controller.delete_folder(id)
