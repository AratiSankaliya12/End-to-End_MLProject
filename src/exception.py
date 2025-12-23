import sys
import logging
from exception import CustomException


def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        "Error occurred in script: {} at line number: {} with message: {}".format(
            file_name, exc_tb.tb_lineno, str(error)
        )
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message


try:
    a = 1 / 0
except Exception as e:
    logging.exception("An error occurred", exc_info=True)
    raise CustomException(e, sys) from e
