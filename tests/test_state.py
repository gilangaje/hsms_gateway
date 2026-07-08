from hsms_gateway.hsms.state import HsmsState


def test_state_values():

    assert HsmsState.NOT_CONNECTED.name == "NOT_CONNECTED"

    assert HsmsState.TCP_CONNECTED.name == "TCP_CONNECTED"

    assert HsmsState.SELECTED.name == "SELECTED"