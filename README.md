# PYISAC-CORE - PYthon InfraStructure As Code Core Server

[![Build Status](https://travis-ci.org/r3alityc0d3r/pyisac-core.svg?branch=master)](https://travis-ci.org/r3alityc0d3r/pyisac-core)

#### Table of Contents
1. [About](#about)
2. [Requirements](#requirements)
3. [Installation](#installation)

## About

This project will hopefully be a new way to think about configuration management
and application deploment.  It is my hope to design a way to define your infra-
structure in regular python code and use that code to not only perform 
configuration management but also a simple way of deploying applications.

This project is the core server that runs configurations and application
deployement

## Requirements

Pyisac stores node configuration information in a mongo database located on the
same server.  Follow Mongo's documentation for installation instructions:

[MongoDB Installation Instructions](https://docs.mongodb.org/manual/administration/install-on-linux/)

## Installation

1. Make a directory for configuration information

    ```
    mkdir -p /etc/pyisac/config
    ```

2. Create a configuration file

    ```
    vim /etc/pyisac/config/config.json
    ```

    with the following contents

    ```
    { "nodes_path": "/etc/pyisac/config/nodes"} 
    ```

    Where nodes_path is the path to your node definition files.  You will need
    to create this directory

    ```
    mkdir /etc/pyisac/config/nodes
    mkdir /etc/pyisac/config/scripts
    ```
3. Create pyisac group and add your user to it. Also change the permissions of the /etc/pyisac folder


    ```
    sudo groupadd pyisac
    sudo usermod -a -G pyisac youruser
    sudo chown root:pyisac /etc/pyisac/ -R
    ```
 
4. Write json node information files

    ```
    vim /etc/pyisac/config/nodes/systems.json
    ```

    with the following contents substituting your node information:

    ```
    {
        "systems":[
        {
            "type":"linux", 
            "servername":"lnx-server-1.billcloud.local", 
            "location":"my datacenter",
            "username":"vagrant",
            "classes":["ntp","apache2"]
        }
        ]
    }
    ```

5. Create the pyisac service directory and copy everything there

    ```
    mkdir /opt/pyisac
    cd /opt/pyisac
    git clone https://github.com/r3alityc0d3r/pyisac-core.git
    ```

6. Create the python virtualenv

    ```
    sudo pip install virtualenv
    virtualenv venv
    source venv/bin/activate
    cd pyisac-core
    ```
7. Install some modules

    pyisac implements modules in order to extend its functionality.  Modules
    are installed in /etc/pyisac/config/modules.  Change directory to that
    directory and clone any modules

    ```
    cd /etc/pyisac/config/modules
    git clone git@github.com:r3alityc0d3r/pyisac-ntp.git ntp
    ```

    The example above installs the NTP module which gives pyisac the ability
    to manage NTP on your nodes.

8. Run the pyisac command to start configuration

    ```
    ./pyisac.py
    ```
    You should see some output

    ```
    Python InfraStructure As Code - Open Source
    Released under the GPU v2 - http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
    loading environment configuration from /etc/pyisac/config/config.json
    Found /etc/pyisac/config/nodes/systems.json
    Found /etc/pyisac/config/nodes/systems2.json
    Loading node configuration from /etc/pyisac/config/nodes/systems.json
    Successfully Loaded Nodes
    Loading node configuration from /etc/pyisac/config/nodes/systems2.json
    Successfully Loaded Nodes
    Found 4 Nodes
    ```

    At this point it really doesn't do much but list out the nodes in your
    configuration. More coming soon...

## Setup a test environment using vagrant

This repository comes with a test environment for testing your code in 
the test-nodes/ directory.  In order to get this to work you need to have
already generated an ssh key and add it to the ssh-agent:

```
ssh-keygen -t rsa
ssh-add ~/.ssh/id_rsa
```

Go to the test-nodes direstory and do a vagrant up.  Then login and get the ip
address of the vagrant system:

```
cd test-nodes/
vagrant up
vagrant ssh

vagrant@lnx-server-1:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 16436 qdisc noqueue state UNKNOWN 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000
    link/ether 08:00:27:88:0c:a6 brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global eth0
    inet6 fe80::a00:27ff:fe88:ca6/64 scope link 
       valid_lft forever preferred_lft forever
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000
    link/ether 08:00:27:e4:83:77 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.127/24 brd 192.168.1.255 scope global eth1
    inet6 fe80::a00:27ff:fee4:8377/64 scope link 
       valid_lft forever preferred_lft forever
vagrant@lnx-server-1:~$ exit
```

Next add the test system to your hosts file:

```
sudo vim /etc/hosts
192.168.1.127 lnx-server-1.billcloud.local lnx-server-1
```

You should now be able to ssh to your test box directly:

```
ssh lnx-server-1.billcloud.local
The authenticity of host 'lnx-server-1.billcloud.local (192.168.1.127)' can't be established.
ECDSA key fingerprint is SHA256:
ECDSA key fingerprint is MD5:
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'lnx-server-1.billcloud.local' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 12.04 LTS (GNU/Linux 3.2.0-23-generic x86_64)

 * Documentation:  https://help.ubuntu.com/
New release '14.04.3 LTS' available.
Run 'do-release-upgrade' to upgrade to it.

Welcome to your Vagrant-built virtual machine.
Last login: Sun Jan 31 19:55:32 2016 from 192.168.1.112
vagrant@lnx-server-1:~$
```

You are now ready to start testing pyisac!
