from hsms_gateway.secs.message import (
    SecsMessage,
)


def s1f1():

    return SecsMessage(
        stream=1,
        function=1,
        wbit=True,
    )