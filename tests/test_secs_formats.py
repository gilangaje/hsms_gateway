from hsms_gateway.secs.formats import SecsFormat


def test_ascii():

    assert SecsFormat.ASCII == 16


def test_list():

    assert SecsFormat.LIST == 0


def test_u1():

    assert SecsFormat.U1 == 41