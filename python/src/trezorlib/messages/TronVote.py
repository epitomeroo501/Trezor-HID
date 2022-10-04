# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class TronVote(p.MessageType):

    def __init__(
        self,
        vote_address: str = None,
        vote_count: int = None,
    ) -> None:
        self.vote_address = vote_address
        self.vote_count = vote_count

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('vote_address', p.UnicodeType, 0),
            2: ('vote_count', p.UVarintType, 0),
        }