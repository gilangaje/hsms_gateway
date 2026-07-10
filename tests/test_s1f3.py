from hsms_gateway.gem.s1f3 import s1f3


def test_s1f3():

    msg = s1f3(
        [1, 2, 3]
    )

    assert msg.stream == 1
    assert msg.function == 3
    assert msg.wbit is True

    body = msg.body

    assert len(body.value) == 3