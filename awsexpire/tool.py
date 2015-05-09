import boto

tags_by_instances = lambda instances: {x: x.tags for x in instances}


def get_ec2_instances():
    ec2 = boto.connect_ec2()
    for res in ec2.get_all_instances():
        for box in res.instances:
            yield box
