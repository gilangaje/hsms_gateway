from hsms_gateway.secs.message import SecsMessage

from hsms_gateway.secs.items import (
    L,
)


def s1f4(values):

    return SecsMessage(
        stream=1,
        function=4,
        wbit=False,
        body=L(values),
    )