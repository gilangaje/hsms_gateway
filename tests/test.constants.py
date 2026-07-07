from hsms_gateway.hsms.constants import SessionType


def test_session_type():
    assert SessionType.SELECT_REQ == 1
    assert SessionType.SELECT_RSP == 2
    assert SessionType.DATA == 0