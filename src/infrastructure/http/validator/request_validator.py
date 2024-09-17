"""This module provides a decorator for validating request bodies using JSON schema."""

from functools import wraps
from typing import Callable, Any

from jsonschema import validate

from infrastructure.http.contracts.base_request_contract import BaseRequestContract


def validate_request_body(request, request_contract: BaseRequestContract) -> Callable[
    [Any], Callable[[tuple[Any, ...], dict[str, Any]], Any]]:
    """Decorator to validate the request body against a given JSON schema.

    Args:
        request: The request object containing the JSON body.
        request_contract (BaseRequestContract): The contract defining the JSON schema.

    Returns:
        Callable: The decorated function.
    """
    def validate_request_body_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            request_body = request.get_json()
            validate(request_body, request_contract.contract())
            return func(*args, **kwargs)

        return wrapper
    return validate_request_body_decorator
