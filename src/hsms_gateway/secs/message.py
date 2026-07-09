from dataclasses import dataclass


@dataclass(slots=True)
class SecsMessage:

    stream: int
    function: int
    wbit: bool
    body: object | None = None