from hsms_gateway.hsms.constants import SType
from hsms_gateway.hsms.messages import select_req


def test_select_req():

    frame = select_req()

    assert frame.header.session_id == 0xFFFF
    assert frame.header.s_type == SType.SELECT_REQ
    assert frame.body == b""