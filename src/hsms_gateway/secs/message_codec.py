from .message import SecsMessage
from .encoder import encode_item

from ..hsms.header import HsmsHeader
from ..hsms.frame import HsmsFrame


def encode_message(message: SecsMessage) -> HsmsFrame:

    if message.body is None:
        body = b""
    else:
        body = encode_item(message.body)

    header = HsmsHeader(
        session_id=0,
        stream=message.stream,
        function=message.function,
        p_type=0,
        s_type=0,
        system_bytes=1,
        w_bit=message.wbit,
    )

    return HsmsFrame(
        header=header,
        body=body,
    )


def decode_message(frame: HsmsFrame) -> SecsMessage:
    if frame.body:
        body = decode_item(frame.body)
    else:
        body = None

    return SecsMessage(
        stream=frame.header.stream,
        function=frame.header.function,
        wbit=frame.header.w_bit,
        body=body,
    )