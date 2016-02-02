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

    def show(self):
        BaseServer.show(self)
        print "username: %s" % self.username
        print "classes: %s" % self.classes
