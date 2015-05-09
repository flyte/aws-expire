import types
import boto
from unittest import TestCase
from awsexpire import tool
from moto import mock_ec2

TEST_AMI = "ami-1234abcd"
LIST_TYPES = (types.ListType, types.GeneratorType)

get_ec2_conn = lambda: boto.connect_ec2("test_key", "test_secret")


def add_servers(amt):
    ec2 = get_ec2_conn()
    for _ in xrange(0, amt):
        ec2.run_instances(TEST_AMI)


class AWSExpireTestCase(TestCase):

    @mock_ec2
    def test_get_ec2_instances(self):
        """
        get_ec2_instances() should get all instances.
        """
        amt = 10
        add_servers(amt)
        instances = tool.get_ec2_instances()

        self.assertTrue(isinstance(instances, LIST_TYPES))
        instances = list(instances)
        self.assertEqual(len(instances), amt)

    @mock_ec2
    def test_get_ec2_tags_by_instances(self):
        """
        tags_by_instances() should get a dictionary of instances to tags for a list
        of instances.
        """
        ec2 = get_ec2_conn()
        res = ec2.run_instances(TEST_AMI)
        box = res.instances[0]
        box.add_tag("test_tag", "test_tag_value")

        tags = tool.tags_by_instances(tool.get_ec2_instances())
        self.assertIn(box.id, [x.id for x in tags.keys()])
