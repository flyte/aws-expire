from unittest import TestCase
from .mock.boto import ec2, connection


class BotoMockTestCase(TestCase):

    def test_ec2_connect_to_region(self):
        """
        Connect to region should return an EC2Connection object.
        """
        conn = ec2.connect_to_region(
            "eu-west-1", aws_access_key_id="access key", aws_secret_access_key="secret access key")
        self.assertEqual(type(conn), type(connection.EC2Connection()))
