from dataclasses import dataclass

from .header import HsmsHeader


@dataclass(slots=True)
class HsmsFrame:

    header: HsmsHeader

    body: bytes = b""