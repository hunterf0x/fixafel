
class GetTransactionsRequestContract:
    @staticmethod
    def contract() -> dict:
        return {
            "type": "object",
            "properties": {
                "list": {"type": "array"},
            },
            "required": ["list"],
        }
