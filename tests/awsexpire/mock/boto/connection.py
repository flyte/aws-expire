from ..util import log_args
from .instance import Reservation, Instance


class EC2Connection:

    @log_args
    def get_all_instances(self):
        res = Reservation()
        res.instances = [Instance()]
        return [res]
