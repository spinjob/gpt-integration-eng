class ErrorHandler:
    def handle_error(self, e):
        # Log error message and return it
        print(e)
        return str(e)
