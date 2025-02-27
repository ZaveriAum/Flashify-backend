from flask import Blueprint, request
from controllers.folder_controller import FolderController
from decorators.RouteDecorator import validate_request
from models.folder import FolderSchema

folder_blueprint = Blueprint("folder", __name__)
controller = FolderController()

@folder_blueprint.route("/", methods=["GET"], endpoint="get_folders")
def get_folders():
    return controller.get_folders()

@folder_blueprint.route("/", methods=["POST"], endpoint="create_folder")
@validate_request(FolderSchema)
def create_folder():
    folder_data = request.json
    return controller.create_folder(folder_data)

@folder_blueprint.route("/<id>", methods=["PUT"], endpoint="update_folder")
@validate_request(FolderSchema)
def update_folder(id):
    folder_data = request.json
    return controller.update_folder(id, folder_data)

@folder_blueprint.route("/<id>", methods=["DELETE"], endpoint="delete_folders")
def delete_folder(id):
    return controller.delete_folder(id)
