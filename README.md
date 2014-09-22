Ahsay python API library
========================
A simple requests wrapper for the Ahsay API.

Usage
-----
```python
    from ahsay.api import AhsayAPI
    api = AhsayAPI('username', 'password', 'host')
    # Optional arguments are passed into `call` as keyword arguments.
    results = api.call('ListBackupSets', LoginName='user1')
```

TODO
----

- Make python2 compatible.
