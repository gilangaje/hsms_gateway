from hsms_gateway.hsms.messages import (
    linktest_req,
    linktest_rsp,
)

from hsms_gateway.hsms.constants import SType


def test_linktest_req():

    frame = linktest_req()

    assert frame.header.s_type == SType.LINKTEST_REQ


def test_linktest_rsp():

    frame = linktest_rsp()

    assert frame.header.s_type == SType.LINKTEST_RSP