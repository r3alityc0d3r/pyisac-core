#!/usr/bin/python

"""Class that does the initial configuration of an infrastructure

This module loads the system configuration data
"""

__author__ = 'Bill Ward'
__version__ = '0.1'

class Configuration(object):
    """class to configure an infrastructure"""

    systems = []
    my_servers = []

    def __init__(self, servers):
        self.my_servers = servers

    def show_classes(self, node):
        if type(self.my_servers[0]).__name__ == "LinuxServer":
            print "Classes: {0}".format(self.my_servers[0].classes)
