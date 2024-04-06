from flask import jsonify

def create_response_success(message, data=None):
    """
    Create a success response.
    Args: message (str): The success message.
        message (str): The success message.
        data (any, optional): Additional data to include in the response. Defaults to None.
        Returns: dict: A JSON response with the success result.
    """
    response = {
        'result': 'success',
        'message': message,
        'data': data,
    }
    return jsonify(response)


def create_response_warning(message, data=None):
    """
    Create a warning response.

    Args:
        message (str): The warning message.
        data (any, optional): Additional data to include in the response. Defaults to None.

    Returns:
        dict: A JSON response with the warning result.
    """
    response = {
        'result': 'warning',
        'message': message,
        'data': data,
    }
    return jsonify(response)


def create_response_error(message, data=None):
    """
    Create an error response.

    Args:
        message (str): The error message.
        data (any, optional): Additional data to include in the response. Defaults to None.

    Returns:
        dict: A JSON response with the error result.
    """
    response = {
        'result': 'error',
        'message': message,
        'data': data,
    }
    return jsonify(response)