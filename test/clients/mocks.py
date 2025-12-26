class ClientResponseMock:
    def __init__(self, status_code=200, json_data=None):
        self.status_code = status_code
        self._json_data = json_data

    async def json(self):
        return self._json_data

    @property
    def status(self) -> int:
        return self.status_code

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass