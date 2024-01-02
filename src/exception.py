import logging
import traceback

class CustomException(Exception):
    def __init__(self, error_message, error_traceback):
        super().__init__(error_message)
        self.error_message = error_message
        self.error_traceback = error_traceback

    def __str__(self):
        return f"{self.error_message}\n{self.error_traceback}"





        
    

