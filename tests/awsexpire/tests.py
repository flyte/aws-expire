from unittest import TestCase
from .mock.boto import ec2, connection, instance


class BotoMockTestCase(TestCase):

    def test_ec2_connect_to_region(self):
        """
        connect_to_region() should return an EC2Connection object.
        """
        conn = ec2.connect_to_region(
            "eu-west-1", aws_access_key_id="access key", aws_secret_access_key="secret access key")
        self.assertEqual(type(conn), type(connection.EC2Connection()))

    def test_ec2_get_all_instances(self):
        """
        get_all_instances() should give us a Reservation with an Instance inside .instances.
        """
        conn = ec2.connect_to_region(
            "eu-west-1", aws_access_key_id="access key", aws_secret_access_key="secret access key")
        reservations = conn.get_all_instances()

        self.assertEqual(type(reservations), type([]), "Reservations should be in a list")
        self.assertEqual(
            type(reservations[0].instances),
            type([]),
            "Reservation should contain a list of instances")
        self.assertEqual(type(reservations[0].instances[0]), instance.Instance)
