from enum import Enum, auto


class HsmsState(Enum):

    NOT_CONNECTED = auto()

    TCP_CONNECTED = auto()

    SELECTED = auto()