class AppError(Exception):
    def __init__(self, message, statusCode):
        self.message = message
        self.statusCode = statusCode
        super().__init__(self.message)