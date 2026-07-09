from hsms_gateway.secs.message import SecsMessage


def test_message():

    msg = SecsMessage(

        stream=1,
        function=13,
        wbit=True,
        body=None,
    )

    assert msg.stream == 1
    assert msg.function == 13
    assert msg.wbit is True