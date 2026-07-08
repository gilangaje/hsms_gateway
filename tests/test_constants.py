from hsms_gateway.hsms.constants import PType, SType


def test_stype_values():
    assert SType.DATA_MESSAGE == 0
    assert SType.SELECT_REQ == 1
    assert SType.LINKTEST_REQ == 5


def test_ptype_values():
    assert PType.SECS2 == 0