"""Class that does the initial configuration of an infrastructure

This module loads the system configuration data
"""
import imp
import sys

__author__ = 'Bill Ward'
__version__ = '0.1'

class Configuration(object):
    """class to configure an infrastructure"""

    systems = []
    my_servers = []

    def __init__(self, servers):
        self.my_servers = servers

    def show_classes(self, node):
        print "classes:"
        if type(node).__name__ == "LinuxServer":
            if not type(node.classes).__name__ == "unicode":
                for config_class in node.classes:
                    print " - {0}".format(config_class)
            else:
                print " - {0}".format(node.classes)

    def get_system(self, fqdn):
        for server in self.my_servers:
            if server.servername == fqdn:
                return server
            else:
                return 1

    def load_modules(self):
        from os import listdir
        #sys.path.append('/etc/pyisac/config/modules') #include user modules 
        moduleNames = listdir("/etc/pyisac/config/modules/")
        modules = map(__import__, moduleNames) 
        moduleNum = len(modules)
        print "Imported {0} module(s) {1}".format(moduleNum,moduleNames)

    def load_facts(self, node):
        pass
