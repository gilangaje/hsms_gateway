from hsms_gateway.hsms.frame import HsmsFrame
from hsms_gateway.hsms.header import HsmsHeader


def test_create_frame():

    header = HsmsHeader(
        session_id=10,
        stream=1,
        function=13,
        p_type=0,
        s_type=0,
        system_bytes=1,
        w_bit=True,
    )

    frame = HsmsFrame(
        header=header,
        body=b"ABC"
    )

    assert frame.header == header

    assert frame.body == b"ABC"

def test_encode_frame():

    header = HsmsHeader(
        session_id=10,
        stream=1,
        function=13,
        p_type=0,
        s_type=0,
        system_bytes=1,
        w_bit=True,
    )

    frame = HsmsFrame(
        header=header,
        body=b"",
    )

    raw = frame.encode()

    expected = (
        bytes.fromhex("00 00 00 0A")
        + bytes.fromhex("00 0A 81 0D 00 00 00 00 00 01")
    )

    assert raw == expected

def test_decode_frame():

    raw = (
        bytes.fromhex(
            "00 00 00 0A"
            "00 0A 81 0D"
            "00"
            "00"
            "00 00 00 01"
        )
    )

    frame = HsmsFrame.decode(raw)

    assert frame.header.session_id == 10
    assert frame.header.stream == 1
    assert frame.header.function == 13
    assert frame.body == b""

def test_frame_roundtrip():

    original = HsmsFrame(

        header=HsmsHeader(
            session_id=10,
            stream=1,
            function=13,
            p_type=0,
            s_type=0,
            system_bytes=123,
            w_bit=True,
        ),

        body=b"ABCDEF",
    )

    raw = original.encode()

    decoded = HsmsFrame.decode(raw)

    assert decoded == original