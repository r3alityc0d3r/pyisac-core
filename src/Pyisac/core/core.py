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
        return result[0]
