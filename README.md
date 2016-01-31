# PYISAC-CORE - PYthon InfraStructure As Code Core Server

[![Build Status](https://travis-ci.org/r3alityc0d3r/pyisac-core.svg?branch=master)](https://travis-ci.org/r3alityc0d3r/pyisac-core)

## About

This project will hopefully be a new way to think about configuration management
and application deploment.  It is my hope to design a way to define your infra-
structure in regular python code and use that code to not only perform 
configuration management but also a simple way of deploying applications.

This project is the core server that runs configurations and application
deployement

## Installation

1. Make a directory for configuration information

    ```
    mkdir /etc/pyisac/config
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
    ```

3. Wirite json node information files

    ```
    vim /etc/pyisac/config/nodes/systems.json
    ```

    with the following contents substituting your node information:

    ```
    {
        "systems":[
        {
            "type":"linux", 
            "servername":"lnx-server-1", 
            "location":"atc", 
            "kernel":"4.3.3-300.fc23.x86_64"
        },
        {
            "type":"linux",
            "servername":"lnx-server-2",
            "location":"atc",
            "kernel":"4.3.3-300.fc23.x86_64"
        }]
    }
    ```

4. Create the pyisac service directory and copy everything there

    ```
    mkdir /opt/pyisac
    cd /opt/pyisac
    git clone https://github.com/r3alityc0d3r/pyisac-core.git
    ```

5. Create the python virtualenv

    ```
    sudo pip install virtualenv
    virtualenv venv
    source venv/bin/activate
    cd pyisac-core
    ```

6. Run the pyisac command to start configuration

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
