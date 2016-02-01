#!/usr/bin/python

"""Define classes that represent servers

This is a module that is used to define
the servers in an infrastructure
"""

__author__ = 'Bill Ward'
__version__ = '0.1'

class BaseServer(object):
    """Generic Server Class"""
    def __init__(self,servername="test",location="test"):
        """Set default attribute values only

        Keyword arguments
        servername - - the name of the server
        location - - the physical location of the server
        """
        self.servername = servername
        self.location = location

    def show(self):
        """ member function to show details of the server """
        print "Servername: %s" % self.servername
        print "Location: %s" % self.location
