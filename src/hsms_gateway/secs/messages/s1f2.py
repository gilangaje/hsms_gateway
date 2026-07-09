from hsms_gateway.secs.message import (
    SecsMessage,
)


def s1f2():

    return SecsMessage(
        stream=1,
        function=2,
        wbit=False,
    )