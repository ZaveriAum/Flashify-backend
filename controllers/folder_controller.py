from services.folder_service import FolderService
from flask import jsonify, g

class FolderController:
    
    @staticmethod
    def get_folders():
        try:
            folders = FolderService.get_folders()
            return jsonify({
                "message": "Folders retrieved successfully",
                "folders":folders
                }), 200
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), getattr(e, "statusCode", 400)

    @staticmethod
    def create_folder(folder_data):
        try:
            folder = FolderService.create_folder(folder_data)
            return jsonify({
                "message": "Folder created successfully",
                "folder":folder
                }), 201
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), getattr(e, "statusCode", 400)

    @staticmethod
    def update_folder(id, folder_data):
        try:
            updated_folder = FolderService.update_folder(id, folder_data)
            return jsonify({
                "message": "Folder updated successfully",
                "updated folder": updated_folder
                }), 200
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), getattr(e, "statusCode", 400)

    @staticmethod
    def delete_folder(id):
        try:
            deleted_folder = FolderService.delete_folder(id)
            return jsonify({
                "message": "Folder deleted successfully",
                "deleted folder": deleted_folder
                }), 204
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), getattr(e, "statusCode", 400)
