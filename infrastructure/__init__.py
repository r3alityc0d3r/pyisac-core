from servers import *

class Infrastructure(object):
    
    systems = []

    def import_json(self,filename):
        my_servers = servers.load(filename)
        print "Loading Infrastructure..."
        for server in my_servers["systems"]:
            x = servers.LinuxServer(
                    server["servername"],
                    server["location"],
                    server["kernel"],
                    )
            x.show()
            self.systems.append(x)
