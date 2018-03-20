# Automatically generated by pb2py
import protobuf as p
from .NEMCosignatoryModification import NEMCosignatoryModification


class NEMAggregateModification(p.MessageType):
    FIELDS = {
        1: ('modifications', NEMCosignatoryModification, p.FLAG_REPEATED),
        2: ('relative_change', p.Sint32Type, 0),
    }

    def __init__(
        self,
        modifications: list = None,
        relative_change: int = None,
        **kwargs,
    ):
        self.modifications = [] if modifications is None else modifications
        self.relative_change = relative_change
        p.MessageType.__init__(self, **kwargs)