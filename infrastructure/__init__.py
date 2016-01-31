from servers import *
from core import *

class Infrastructure(object):
    
    systems = []
   
    def exec_command(self,host,username,command):
        sshcmd = core.sshexec(host, username, command)
        result = sshcmd.run()
        return result[0]

    def get_system_info(self,host,username):
        command = "uname -r"
        sshcmd = core.sshexec(host, username, command)
        result = sshcmd.run()
        return result[0]

    def import_json(self,filename):
        my_servers = servers.load(filename)
        for server in my_servers["systems"]:
            x = servers.LinuxServer(
                    server["servername"],
                    server["location"],
                    server["username"],
                    )
            self.systems.append(x)
        print "Successfully Loaded Nodes"
        return self.systems
