from hsms_gateway.secs.message import SecsMessage


def s1f14():

    return SecsMessage(
        stream=1,
        function=14,
        wbit=False,
    )