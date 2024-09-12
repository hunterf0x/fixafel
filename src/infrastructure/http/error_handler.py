from werkzeug.exceptions import HTTPException
from flask import Response, json

def handle_exception(e: Exception) -> Response:
    error_message = e.args[0] if len(e.args) > 0 else "Internal server error"
    print(f"Error: {error_message}")
    if isinstance(e, HTTPException):
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