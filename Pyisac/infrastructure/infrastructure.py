from servers import *

class Infrastructure(object):
    
    systems = []
   
    def import_json(self,filename):
        my_servers = load(filename)
        for server in my_servers["systems"]:
            x = LinuxServer(
                    server["servername"],
                    server["location"],
                    server["username"],
                    )
            self.systems.append(x)
        return self.systems
