from hsms_gateway.secs.items import L
from hsms_gateway.secs.items import U4
from hsms_gateway.secs.message import SecsMessage


def s1f3(svids):

    return SecsMessage(
        stream=1,
        function=3,
        wbit=True,
        body=L(
            [
                U4(svid)
                for svid in svids
            ]
        ),
    )