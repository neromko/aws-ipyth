import boto3
import click


session = boto3.Session(profile_name='pawels_linxsys_testing', region_name='us-east-1')
ec2 = session.resource('ec2')

@click.command()

def list_instances():
    "Lista"
    for i in ec2.instances.all():
       print('. '.join((
       i.id,
       i.instance_type,
       i.state['Name']
       )))
    return

if __name__ == '__main__':

    list_instances()
