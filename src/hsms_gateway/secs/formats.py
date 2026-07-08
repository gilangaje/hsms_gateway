from enum import IntEnum


class SecsFormat(IntEnum):

    LIST = 0

    BINARY = 8

    BOOLEAN = 9

    ASCII = 16

    JIS8 = 17

    I8 = 24
    I1 = 25
    I2 = 26
    I4 = 28

    F8 = 32
    F4 = 36

    U8 = 40
    U1 = 41
    U2 = 42
    U4 = 44