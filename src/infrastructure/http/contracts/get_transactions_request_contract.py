"""Module for defining the request contract for getting transactions."""

class GetTransactionsRequestContract:
    """Request contract for getting transactions."""

    @staticmethod
    def contract() -> dict:
        """Return the JSON schema for the request contract.

        Returns:
            dict: The JSON schema for the request contract.
        """
        return {
            "type": "object",
            "properties": {
                "list": {"type": "array"},
            },
            "required": ["list"],
        }
