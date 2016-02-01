"""
Execute a command over SSH
"""
import subprocess
import sys

class sshexec(object):
    """
    Executes a command over SSH
    """
    def __init__(self,host,username,command):
        """
        initializes the sshexec command

        :param host: host to run the command on
        :param username: user for SSH connection
        :param command: command to run 
        """
        self.host = host
        self.command = command
        self.username = username

    def run(self):
        """
        Runs the SSH command and gets output

        :return: result of running the command
        """
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
