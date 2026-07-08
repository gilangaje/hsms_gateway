from .formats import SecsFormat


class SecsItem:

    format = None

    def __init__(self, value):

        self.value = value

    def __repr__(self):

        return (
            f"{self.__class__.__name__}"
            f"({self.value!r})"
        )
    
class A(SecsItem):

    format = SecsFormat.ASCII


class B(SecsItem):

    format = SecsFormat.BINARY


class U1(SecsItem):

    format = SecsFormat.U1


class U2(SecsItem):

    format = SecsFormat.U2


class U4(SecsItem):

    format = SecsFormat.U4

class L(SecsItem):

    format = SecsFormat.LIST

    def __init__(self, items):

        super().__init__(items)

    def __iter__(self):

        return iter(self.value)

    def __len__(self):

        return len(self.value)