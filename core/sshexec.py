import subprocess
import sys

class sshexec(object):

    def __init__(self,host,username,command):
        self.host = host
        self.command = command
        self.username = username

    def run(self):
        host_address = "{0}@{1}".format(self.username,self.host)
        ssh = subprocess.Popen(["ssh", "%s" % host_address, self.command],
                shell = False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        result = ssh.stdout.readlines()
        if result == []:
            error = "ERROR: " + ssh.stderr.readlines()
            return error
        else:
            return result
