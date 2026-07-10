from hsms_gateway.secs.messages.s1f14 import s1f14


def test_s1f14():

    msg = s1f14()

    assert msg.stream == 1
    assert msg.function == 14
    assert msg.wbit is False