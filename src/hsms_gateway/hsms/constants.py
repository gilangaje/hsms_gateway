from enum import IntEnum


class SessionType(IntEnum):

    DATA = 0

    SELECT_REQ = 1
    SELECT_RSP = 2

    DESELECT_REQ = 3
    DESELECT_RSP = 4

    LINKTEST_REQ = 5
    LINKTEST_RSP = 6

    REJECT_REQ = 7

    SEPARATE_REQ = 9