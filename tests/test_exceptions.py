from hsms_gateway.hsms.exceptions import (
    HsmsError,
    ConnectionClosedError,
    ReceiveTimeoutError,
)


def test_exception_inheritance():
    assert issubclass(ConnectionClosedError, HsmsError)
    assert issubclass(ReceiveTimeoutError, HsmsError)