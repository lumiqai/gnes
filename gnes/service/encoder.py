import zmq

from .base import BaseService, Message
from ..document import MultiSentDocument
from ..encoder import PipelineEncoder


class EncoderService(BaseService):
    def _post_init(self):
        if self.args.model_path:
            # trained, load binary dump
            self.encoder = PipelineEncoder.load(self.args.model_dump)
        elif self.args.yaml_path:
            self.encoder = PipelineEncoder.load_yaml(self.args.yaml_path)

    def _handler_default(self, msg: Message, out: 'zmq.Socket'):
        ds = MultiSentDocument.from_list(msg.msg_content)
        pass
