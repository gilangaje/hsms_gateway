class HsmsSocket:

    def connect(self):
        ...

    def disconnect(self):
        ...

    def send(self, data: bytes):
        ...

    def receive(self, size: int) -> bytes:
        ...

    @property
    def connected(self) -> bool:
        ...