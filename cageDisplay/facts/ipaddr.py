#!/usr/bin/env python

import sys
import subprocess
import socket

def getNetIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets
    return s.getsockname()[0]


if __name__ == '__main__':
    print 'IP: ' + getNetIp()
    try:
        retcode = subprocess.call("ip -o -f inet addr", shell=True)
        if retcode < 0:
            print >>sys.stderr, "Child was terminated by signal", -retcode
        else:
            print >>sys.stderr, "Child returned", retcode
    except OSError as e:
        print >>sys.stderr, "Execution failed:", e
