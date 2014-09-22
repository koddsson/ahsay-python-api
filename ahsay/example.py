"""Ahsay API example.

Usage:
  example.py <user> <backup_name> [--username=<username> | --password=<password> | --hostname=<hostname>]
  example.py (-h | --help)
  example.py --version

Options:
  -h --help                     Show this screen.
  --version                     Show version.
  --username=<username>         API username
  --password=<password>         API password
  --hostname=<hostname>         API hostname with scheme (https://)

"""
from docopt import docopt

import os

from api import AhsayAPI
from datetime import datetime, timedelta


def get_last_backup_time(api, user, backup_name):
    """
    Gets back the datetime of last time the backup schedule ran successfully

    :param user: The user that did the backup.
    :param backup_name: Name of backup file.
    """
    backups = api.call('ListBackupSets', LoginName=user)
    for b in backups:
        if b.attrib['Name'] != backup_name:
            continue
        bs = api.call(
            'GetBackupSet', LoginName=user, BackupSetID=b.attrib['ID'])
        timestamp = int(bs.attrib['LastBackupCompleted'])/1000
        return datetime.fromtimestamp(timestamp)

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Ahsay-API-Example 1.0')
    api_user = arguments.get('--username', None) or os.environ['AHSAY_API_USER']
    api_pass = arguments.get('--password', None) or os.environ['AHSAY_API_PASS']
    api_host = arguments.get('--hostname', None) or os.environ['AHSAY_HOST']
    api = AhsayAPI(api_user, api_pass,  api_host)
    user = arguments['<user>']
    backup_name = arguments['<backup_name>']
    last_backup = get_last_backup_time(api, user, backup_name)

    two_days_ago = datetime.now() - timedelta(days=1)
    if last_backup > two_days_ago:
        print('too old')
