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
    def __init__(self,servername,location,kernel):
        BaseServer.__init__(self, servername, location)
        self.kernel = kernel

    def show(self):
        BaseServer.show(self)
        print "Kernel: %s" % self.kernel
