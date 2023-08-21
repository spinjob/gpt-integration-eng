class ErrorHandler:
    def handle_error(self, error, data):
        return {
            'errorCode': str(error),
            'data': data
        }
