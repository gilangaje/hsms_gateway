from hsms_gateway.hsms.frame import HsmsFrame
from hsms_gateway.hsms.header import HsmsHeader

from hsms_gateway.secs.message_codec import decode_message


def test_decode_empty_message():

    frame = HsmsFrame(

        header=HsmsHeader(
            session_id=0,
            stream=1,
            function=1,
            p_type=0,
            s_type=0,
            system_bytes=1,
            w_bit=True,
        ),

        body=b"",
    )

    msg = decode_message(frame)

    assert msg.stream == 1
    assert msg.function == 1
    assert msg.wbit is True
    assert msg.body is None