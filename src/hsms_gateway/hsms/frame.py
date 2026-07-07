from dataclasses import dataclass

from .header import HsmsHeader


@dataclass(slots=True)
class HsmsFrame:
    """
    Represents one complete HSMS frame.
    """

    header: HsmsHeader

    body: bytes = b""