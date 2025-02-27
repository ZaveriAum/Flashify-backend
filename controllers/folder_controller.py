from services.folder_service import FolderService
from flask import jsonify, g

class FolderController:
    
    @staticmethod
    def get_folders():
        try:
            folders = FolderService.get_folders()
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
    def create_folder(folder_data):
        try:
            folder = FolderService.create_folder(folder_data)
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
                }), 200
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
