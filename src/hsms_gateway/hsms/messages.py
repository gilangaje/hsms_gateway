from .constants import SType
from .frame import HsmsFrame
from .header import HsmsHeader


def select_req(system_bytes: int = 1) -> HsmsFrame:
    """
    Build HSMS Select.req frame.
    """

    header = HsmsHeader(
        session_id=0xFFFF,
        stream=0,
        function=0,
        p_type=0,
        s_type=SType.SELECT_REQ,
        system_bytes=system_bytes,
        w_bit=False,
    )

    return HsmsFrame(
        header=header,
        body=b"",
    )