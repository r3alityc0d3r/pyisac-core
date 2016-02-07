"""
Class to manage packages using pyisac
"""
import core

class package(object):

    def __init__(self, os_type):
        self.os_type = os_type
        if os_type == "Redhat":
            self.provider = "dnf"
        elif os_type == "Ubuntu":
            self.provider = "apt-get"
