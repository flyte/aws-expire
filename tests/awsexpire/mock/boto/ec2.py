from ..util import log_args
from .connection import EC2Connection
from .instance import Reservation, Instance


@log_args
def connect_to_region(region, aws_access_key_id, aws_secret_access_key):
    return EC2Connection()


@log_args
def get_all_instances():
    res = Reservation()
    res.instances = [Instance()]
    return res
