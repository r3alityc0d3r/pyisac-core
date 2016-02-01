#!/usr/bin/env python

import os
import sys
import infrastructure
import json
import getopt
import imp
import traceback

class Main(object):

    node_files = []
    nodes = []
    my_infrastructure = infrastructure.Infrastructure()
    deployment = False
    deploy_script = ""

    def banner(self):
        print "Python InfraStructure As Code - Open Source"
        print "Released under the GPU v2 - http://www.gnu.org/licenses/old-licenses/gpl-2.0.html"
    
    def load_configuration(self, config_file):
        with open(config_file) as data_file:                                       
            configuration = json.load(data_file)                                   
        nodes_path = configuration["nodes_path"]                                   
        for root, dirs, files in os.walk(nodes_path):                              
            for file in files:                                                     
                if file.endswith(".json"):                                         
                    node_file = os.path.join(root,file)                            
                    print "Found {0}".format(node_file)                            
                    self.node_files.append(node_file)                                   
    
    def check_configuration(self):
        if not os.path.isdir("/etc/pyisac/config/"):
            sys.exit("ERROR: Configuration Directory not found /etc/pyisac/config/")
        if not os.path.isfile("/etc/pyisac/config/config.json"):
            sys.exit("ERROR: Configuration File not found /etc/pyisac/config/config.json")
        else:
            print("loading environment configuration from /etc/pyisac/config/config.json")
            config_file = "/etc/pyisac/config/config.json"
            return config_file
    
    def load_nodes(self):
        for node_file in self.node_files:
            print "Loading node configuration from {0}".format(node_file)
            self.nodes = self.my_infrastructure.import_json(node_file)
        print "Found {0} Nodes".format(len(self.nodes))
    
    def run(self, argv):
        self.banner()
        try:
            opts, args = getopt.getopt(argv,"hd:",["deploy="])
        except getopt.GetoptError:
            print "pyisac.py --help"
            sys.exit(2)
            
        for opt, arg in opts:
            if opt in ("-h", "--help"):                                                
               print "pyisac help file"                                               
               sys.exit(0)                                                            
            if opt in ("-d", "--deploy"):                                              
                deploy_script = arg                                                    
                deployment = True                                                       
                                                                                   
        self.config_file = self.check_configuration()                                            
        self.load_configuration(self.config_file)                                                
        self.load_nodes()                                                                   
        if self.deployment:                                                                 
           print "Deploying Script: {0}".format(self.deploy_script)                         
           self.deploy(self.deploy_script)
    
    def deploy(script):
        if not os.path.isfile(script):
            print "Script Not found: {0}".format(script)
        else:
            print ""
            execfile(script)
    
def main():
    main = Main()
    try:
        main.run(sys.argv[1:])
    except SystemExit as e:
        if e.code != 0:
            print "Uncaught Exception raised, exiting:\n{0}".format(traceback.format_exc())
    except:
        print "Uncaught Exception raised, exiting:\n{0}".format(traceback.format_exc())

if __name__ == "__main__":
    main()
