#!/usr/bin/python
from baseserver import *

"""Define classes that represent windows servers

This is a module that is used to define
windows servers in an infrastructure
"""

__author__ = 'Bill Ward'
__version__ = '0.1'

class WindowsServer(BaseServer):
    """Windows Server Class"""
    def __init__(self,servername,location,version):
        BaseServer.__init__(self, servername, location)
        self.version = version

    def show(self):
        BaseServer.show(self)
        print "kernel: %s" % self.version
