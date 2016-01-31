# pyisac script to run a report of systems configured

def get_kernel_version(host):
    command = "uname -r"
    return my_infrastructure.exec_command(host, "vagrant", command)

print "system,kernel version"
for node in nodes:
    kernel_version = get_kernel_version(node.servername)
    print "{0},{1}".format(node.servername,kernel_version)
