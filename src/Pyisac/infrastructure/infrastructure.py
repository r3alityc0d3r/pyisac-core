from servers import *

class Infrastructure(object):
    
    systems = []
   
    def import_json(self,filename):
        my_servers = load(filename)
        for server in my_servers["systems"]:
            if "classes" in server:
                classes_json = server["classes"]
            else:
                classes_json = "{}"
            x = LinuxServer(
                    server["servername"],
                    server["location"],
                    server["username"],
                    classes_json
                    )
            self.systems.append(x)
        return self.systems
