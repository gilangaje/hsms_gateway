from hsms_gateway.hsms.client import HsmsClient
from hsms_gateway.secs.messages.s1f1 import s1f1
from hsms_gateway.secs.messages.s1f3 import s1f3


class GemClient(HsmsClient):

    def are_you_there(self):

        self.send_message(
            s1f1()
        )

        reply = self.receive_message()

        model = reply.body[0].value
        revision = reply.body[1].value

        return model, revision
    
    def read_status_variables(self, svids):

        self.send_message(
            s1f3(svids)
        )

        reply = self.receive_message()

        return reply.body