from hsms_gateway.secs.message import SecsMessage


def s1f13():

    return SecsMessage(
        stream=1,
        function=13,
        wbit=True,
    )