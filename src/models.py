"""Data models for request/response objects."""


class ProcessRequest:
    """Request model for the process endpoint."""

    def __init__(self, data: str):
        self.data = data

    def validate(self) -> bool:
        return bool(self.data)


class ProcessResponse:
    """Response model for the process endpoint."""

    def __init__(self, result: str, length: int):
        self.result = result
        self.length = length

    def to_dict(self) -> dict:
        return {"result": self.result, "length": self.length}
