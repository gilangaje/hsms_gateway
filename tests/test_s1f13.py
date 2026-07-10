from hsms_gateway.secs.messages.s1f13 import s1f13


def test_s1f13():

    msg = s1f13()

    assert msg.stream == 1
    assert msg.function == 13
    assert msg.wbit is True