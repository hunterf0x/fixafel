"""This module defines the error handler for HTTP exceptions."""

from werkzeug.exceptions import HTTPException
from flask import Response, json

def handle_exception(e: Exception) -> Response:
    """Handle exceptions and return a JSON response.

    Args:
        e (Exception): The exception that was raised.

    Returns:
        Response: A Flask response object with the error details.
    """
    error_message = e.args[0] if len(e.args) > 0 else "Internal server error"
    print(f"Error: {error_message}")
    if isinstance(e, HTTPException):
        print(f"HTTPException: {e}")
        return Response(
            response=json.dumps({
                "message": e.description,
                "code": e.code
            }),
            status=e.code,
            mimetype='application/json'
        )
    return Response(
        response=json.dumps({
            "message": error_message,
            "code": 500,
            "details": "An unexpected error occurred. Please contact support."
        }),
        status=500,
        mimetype='application/json',
        headers={
            "Access-Control-Allow-Origin": "*",  # Soporte para CORS
            "Access-Control-Allow-Headers": "Content-Type,Authorization",
            "Access-Control-Allow-Methods": "GET,POST,PUT,DELETE,OPTIONS"
        }
    )
