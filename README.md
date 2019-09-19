# synoindex-server
Simple synoindex server is a web service wrapper for Synology NAS native 'synoindex'.

## Introduction
Since Synology DSM 6.0 comes Docker support. Users run many media services in the docker. But we can't notify Synology NAS to reindexing new files in the docker's container.

We can run synoindex inside the docker's container and request simple-synoindex-server to calling native synoindex to reindexing your new files using 'simple-synoindex-server' (https://github.com/racklin/simple-synoindex-server) for x86 or x64 cpu. However, it only works on x86 or x64.

With 'synoindex-server' written in python, you can run synoindex on all platforms.

## Setup

### Requirement
Required python (>=3.0)
Tested in Synology DS918+(Apollolake) and DS218play(rtd1296).

### Install
1. Download python file to any directory. ```(ex. /volume1/homes/admin)```
2. Run 'synoindex_server_native.py' by task scheduler when boot-up.
```Shell
python3 /volume1/homes/admin/synoindex_server_native.py
```

### Configuration
Enter the IP of the host running server including port.
```Shell
config = {
    'bindAddr': 'localhost',
    'bindPort': 9998
}
```
