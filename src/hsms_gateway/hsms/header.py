from dataclasses import dataclass


@dataclass(slots=True)
class HsmsHeader:

    session_id: int

    stream: int

    function: int

    ptype: int

    stype: int

    system_bytes: int