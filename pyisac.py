#!/usr/bin/env python

import os
import sys
import infrastructure
import json
import getopt

node_files = []
nodes = []
my_infrastructure = infrastructure.Infrastructure()
deployment = False
deploy_script = ""

def banner():
    print "Python InfraStructure As Code - Open Source"
    print "Released under the GPU v2 - http://www.gnu.org/licenses/old-licenses/gpl-2.0.html"

def load_configuration(config_file):
    with open(config_file) as data_file:                                       
        configuration = json.load(data_file)                                   
    nodes_path = configuration["nodes_path"]                                   
    for root, dirs, files in os.walk(nodes_path):                              
        for file in files:                                                     
            if file.endswith(".json"):                                         
                node_file = os.path.join(root,file)                            
                print "Found {0}".format(node_file)                            
                node_files.append(node_file)                                   

def check_configuration():
    if not os.path.isdir("/etc/pyisac/config/"):
        sys.exit("ERROR: Configuration Directory not found /etc/pyisac/config/")
    if not os.path.isfile("/etc/pyisac/config/config.json"):
        sys.exit("ERROR: Configuration File not found /etc/pyisac/config/config.json")
    else:
        print("loading environment configuration from /etc/pyisac/config/config.json")
        config_file = "/etc/pyisac/config/config.json"
        return config_file

def load_nodes():
    global nodes
    for node_file in node_files:
        print "Loading node configuration from {0}".format(node_file)
        nodes = my_infrastructure.import_json(node_file)
    print "Found {0} Nodes".format(len(nodes))

def report():
    print "system,kernel version"
    for node in nodes:
        kernel_version = my_infrastructure.get_system_info(node.servername,"vagrant")
        print "{0},{1}".format(node.servername,kernel_version)

def run():
    banner()
    config_file = check_configuration()
    load_configuration(config_file)
    load_nodes()
    report()

def main(argv):
    global deploy_script
    global deployment

    banner()
    try:
        opts, args = getopt.getopt(argv,"hd:",["deploy="])
    except getopt.GetoptError:
        print "pyisac.py --help"
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print "pyisac help file"
            isys.exit(0)
        if opt in ("-d", "--deploy"):
            deploy_script = arg
            deployment = True

    config_file = check_configuration()
    load_configuration(config_file)
    load_nodes()
    if deployment:
        print "Deploying Script: {0}".format(deploy_script)

if __name__ == "__main__":
    main(sys.argv[1:])
