from services.folder_service import FolderService
from flask import jsonify

class FolderController:
    
    @staticmethod
    def get_folders(user_id):
        try:
            folders = FolderService.get_folders(user_id)
            return jsonify({
                "status": True,
                "message": "Folders retrieved successfully",
                "folders":folders
                }), 200
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            }), 400

    @staticmethod
    def create_folder(user_id, folder_data):
        try:
            folder = FolderService.create_folder(user_id, folder_data)
            return jsonify({
                "status": True,
                "message": "Folder created successfully",
                "folder":folder
                }), 201
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            }), 400

    @staticmethod
    def update_folder(id, folder_data):
        try:
            updated_folder = FolderService.update_folder(id, folder_data)
            return jsonify({
                "status": True,
                "message": "Folder updated successfully",
                "updated folder": updated_folder
                }), 204
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            }), 400

    @staticmethod
    def delete_folder(id):
        try:
            deleted_folder = FolderService.delete_folder(id)
            return jsonify({
                "status": True,
                "message": "Folder deleted successfully",
                "deleted folder": deleted_folder
                }), 204
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            }), 400
