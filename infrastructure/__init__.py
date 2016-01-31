from servers import *

class Infrastructure(object):
    
    systems = []

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
