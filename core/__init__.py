from sshexec import *

class Core(object):
    def exec_command(self,host,username,command):
        sshcmd = sshexec(host, username, command)
        result = sshcmd.run()
        return result[0]
