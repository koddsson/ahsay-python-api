Ahsay python API library
========================
A simple requests wrapper for the Ahsay API.

Usage
-----
```python
    api = AhsayAPI('username', 'password', 'host')
    # Optional arguments are passed into `call` as keyword arguments.
    results = api.call('ListBackupSets', LoginName='user1')
```
