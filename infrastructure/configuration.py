#!/usr/bin/python

"""Class that does the initial configuration of an infrastructure

This module loads the system configuration data
"""

__author__ = 'Bill Ward'
__version__ = '0.1'

class Configuration(object):
    """class to configure an infrastructure"""
    def __init__(self,filename):
        systems = []

        my_servers = servers.load(filename)
        print "Loading Infrastructure:"
        for server in my_servers["systems"]:
            if server["type"] == "linux":
                x = servers.LinuxServer(
                        server["servername"],
                        server["location"],
                        server["kernel"]
                        )
                x.show()
                self.systems.append(x)
