# pyisac script to run a report of systems configured

def get_kernel_version(host):
    command = "uname -r"
    my_core = Core()
    result = my_core.exec_command(host, "vagrant", command)
    return result

print "system,kernel version"
for node in self.nodes:
    kernel_version = get_kernel_version(node.servername)
    print "{0},{1}".format(node.servername,kernel_version)
