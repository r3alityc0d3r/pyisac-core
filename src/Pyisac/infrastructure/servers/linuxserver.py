#!/usr/bin/python
from baseserver import *

"""Define classes that represent linux servers

This is a module that is used to define
linux servers in an infrastructure
"""

__author__ = 'Bill Ward'
__version__ = '0.1'

class LinuxServer(BaseServer):
    """Linux Server Class"""
    def __init__(self, servername, location, username, classes):
        BaseServer.__init__(self, servername, location)
        self.username = username
        self.classes = classes
        self.ref_id = None
        self.facts = None

    def show(self):
        BaseServer.show(self)
        print "username: %s" % self.username
        print "classes: %s" % self.classes
        print "ref_id: %s" % self.ref_id
        print "facts: $s" % self.facts

    def to_json(self):
        my_dict = {}
        node_dict = {}

        my_dict["location"] = self.location
        my_dict["username"] = self.username
        my_dict["classes"] = self.classes
        
        node_dict["node"] = self.servername
        node_dict["config"] = my_dict
        return node_dict
