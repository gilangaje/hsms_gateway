from hsms_gateway.secs.message import SecsMessage
from hsms_gateway.secs.message_codec import encode_message


def test_encode_empty_message():

    msg = SecsMessage(
        stream=1,
        function=1,
        wbit=True,
        body=None,
    )

    frame = encode_message(msg)

    assert frame.header.stream == 1
    assert frame.header.function == 1
    assert frame.header.w_bit is True
    assert frame.body == b""