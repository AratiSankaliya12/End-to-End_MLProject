import sys
from typing import Any, Tuple

# import logging


def error_message_details(error: Exception, error_detail: Any) -> str:
    """
    Build a detailed error message using the traceback from error_detail.exc_info()
    error_detail is expected to be the sys module (so you pass sys when calling).
    """
    exc_type, exc_obj, exc_tb = error_detail.exc_info()
    if exc_tb is None:
        return f"Error: {str(error)}"
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    return f"Error occurred in script: {file_name} at line number: {line_no} with message: {error}"


class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: Any):
        super().__init__(error_message)
        self.error_message = error_message_details(
            error_message, error_detail=error_detail
        )

    def __str__(self) -> str:
        return self.error_message


"""Example usage of CustomException and logging
try:
    a = 1 / 0
except Exception as e:
    logging.exception("An error occurred", exc_info=True)
    raise CustomException(e, sys) from e
"""
