Ahsay python API library
========================
![](https://travis-ci.org/koddsson/ahsay-python-api.svg?branch=master)

A simple requests wrapper for the Ahsay API.

Usage
-----
```python
    from ahsay.api import AhsayAPI
    api = AhsayAPI('username', 'password', 'host')
    # Optional arguments are passed into `call` as keyword arguments.
    results = api.call('ListBackupSets', LoginName='user1')
```
