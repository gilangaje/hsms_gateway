from hsms_gateway.secs.messages.s1f2 import s1f2


def test_s1f2():

    msg = s1f2()

    assert msg.stream == 1
    assert msg.function == 2
    assert msg.wbit is False