"""Module for defining the request contract for getting transactions."""

class ReInjectTransactionsRequestContract:
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
                "selectedTransactions": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "doc_id": {"type": "string"},
                            "id": {"type": "string"},
                            "TrxNro": {"type": "string"},
                            "body": {"type": "string"},
                        },
                        "required": ["doc_id", "id", "TrxNro", "body"],
                    },
                },
            },
            "required": ["selectedTransactions"],
        }
