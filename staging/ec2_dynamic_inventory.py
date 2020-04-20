#!/usr/bin/env python3
import json
import sys
try:
    import boto3
except Exception as e:
    print(e)
    print("Please rectify the boto3 exception and then try again")
    sys.exit(1)

def get_hosts(ec2_ob, filter_values):
    f={"Name": "tag:Environment", "Values": [filter_values]}
    hosts=[]
    for each_instance in ec2_ob.instances.f(Filters=[f]):
        print(each_instance.private_ip_address)
        hosts.append(each_instance.private_ip_address)
    return hosts
def main():
    ec2_ob=boto3.resource("ec2", "ap-south-1")
    os_group=get_hosts(ec2_ob, 'AMAZON/LINUX2')
    app_group=get_hosts(ec2_ob, 'STAGING')
    all_groups={ 'os' : os_group, 'app': app_group }
    print(json.dumps(all_groups))
    return None

if __name__ == "__main__":
    main()
