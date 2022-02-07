#!/usr/bin/env python3

import sys
import os

class SSHClient():
    def __init__(self, host, pathToSh="./remoteExecCommands.sh"):
        self.host = host
        self.pathToSh = pathToSh
        
    def start(self):

        def parseSh():
            cmds = []
            with open(self.pathToSh) as file:
                cmds = [cmd.strip('\n') for cmd in file]
            return cmds
        
        os.system(f"ssh -t {self.host} {';'.join(parseSh())}; exit;")


def main(args=None):
    if args == 1:
        print("Empty arguments.")
        exit(1)
        
    [SSHClient(host).start() for host in args ]
            
if __name__ == "__main__":
    main(sys.argv[1:])