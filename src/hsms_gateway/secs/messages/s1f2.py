from hsms_gateway.secs.message import SecsMessage
from hsms_gateway.secs.items import L, A


def s1f2(
    model_name: str,
    software_revision: str,
):

    return SecsMessage(
        stream=1,
        function=2,
        wbit=False,
        body=L([
            A(model_name),
            A(software_revision),
        ]),
    )