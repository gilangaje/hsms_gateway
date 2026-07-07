from hsms_gateway.hsms.header import HsmsHeader


def test_create_header():

    header = HsmsHeader(
        session_id=10,
        stream=1,
        function=13,
        p_type=0,
        s_type=0,
        system_bytes=1,
        w_bit=True,
    )

    assert header.session_id == 10
    assert header.stream == 1
    assert header.function == 13
    assert header.w_bit is True

def test_encode_header():

    header = HsmsHeader(
        session_id=10,
        stream=1,
        function=13,
        p_type=0,
        s_type=0,
        system_bytes=1,
        w_bit=True,
    )

    raw = header.encode()

    assert raw == bytes.fromhex(
        "00 0A 81 0D 00 00 00 00 00 01"
    )

def test_decode_header():

    raw = bytes.fromhex(
        "00 0A 81 0D 00 00 00 00 00 01"
    )

    header = HsmsHeader.decode(raw)

    assert header.session_id == 10
    assert header.stream == 1
    assert header.function == 13
    assert header.p_type == 0
    assert header.s_type == 0
    assert header.system_bytes == 1
    assert header.w_bit is True

def test_encode_decode_roundtrip():

    original = HsmsHeader(
        session_id=123,
        stream=5,
        function=17,
        p_type=0,
        s_type=0,
        system_bytes=999,
        w_bit=True,
    )

    raw = original.encode()

    decoded = HsmsHeader.decode(raw)

    assert decoded == original