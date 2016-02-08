"""
Class to manage packages using pyisac
"""
from core import sshexec

class Package(object):

    def __init__(self, name, node, action):
        self.node = node
        self.os_type = node.facts["distro"]
        if self.os_type == "Redhat":
            self.provider = "dnf install "
        elif self.os_type == "Ubuntu":
            self.provider = "sudo apt-get install -y "
        self.name = name
        self.action = action
        self.remediate_package()

    def remediate_package(self):
        if self.action == "install":
            version = self.current()
            if version:
                print "Package {0} already installed [{1}]. Skipping".format(self.name, version)
            else:
                print "Package {0} not install.  Installing".format(self.name)
                self.install()

    def current(self):
        if self.os_type == "Ubuntu":
            command = "dpkg -s " + self.name + " | grep Version"
        cmd = sshexec(self.node.servername, self.node.username, command)
        result = cmd.run()
        
        #cleanup
        if self.os_type == "Ubuntu":
            if "not installed" in result[0]:
                return None
            else:
                result = result[0].split(' ')[-1]
                return result.rstrip()

    def install(self):
        if self.os_type == "Ubuntu":
            command = self.provider + self.name
            cmd = sshexec(self.node.servername, self.node.username, command)
            result = cmd.run()
