"""
core package documentation
"""
from sshexec import sshexec

class Core(object):
    """
    Provides core scripting capabilities for pyisac
    """
    def exec_command(self,host,username,command):
        """
        Executes a command on a remote system using SSH

        :param host: Host to run the command on (as string)
        :param username: Username for SSH connection (as string)
        :param command: Command to be run on the system (as string)

        :return: result of the command 
        """
        sshcmd = sshexec(host, username, command)
        result = sshcmd.run()
        return result[0].rstrip()

    def get_node_facts(self, host, username):
        facts = {}
        kernel_version = self.exec_command(host, username, "uname -r")
        facts["kernel_version"] = kernel_version
        arch = self.exec_command(host, username, "uname -m")
        facts["arch"] = arch
        redhat_test = self.exec_command(host, username, "cat /etc/redhat-release")
        distro = "Unknown"
        if "no such file" not in redhat_test:
            distro = "RedHat"
        ubuntu_test = self.exec_command(host, username, "cat /etc/lsb-release | grep Ubuntu")
        if "Ubuntu" in ubuntu_test:
            distro = "Ubuntu"
        facts["distro"] = distro

        return facts
