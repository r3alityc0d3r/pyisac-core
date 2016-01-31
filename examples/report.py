#
def report():                                                                   
    print "system,kernel version"                                               
    for node in nodes:                                                             
        kernel_version = my_infrastructure.get_system_info(node.servername,"vagrant")
        print "{0},{1}".format(node.servername,kernel_version)

report()
