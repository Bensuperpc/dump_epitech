#
#
# main.py - dump epitech
#
# Created by Benoît(Bensuperpc@gmail.com) 25th november 2019
# Updated by X for python 3.X
#
# Released into the Public domain with GNU licence
# ?
#
# Written with Sublime text 3 and python 3.7.3
# Script compatibility : Linux
# Script requirement : python 3.4 and above, git 2.X
#
# ==============================================================================

import os
import sys
import platform
#import os.path
#from pathlib import Path
#
#import platform

class git:
    def main():
        if not sys.hexversion >= 0x3000000:
            sys.exit("Error, please use python 3.X instead of python 2.X")
        print("Python version: OK")
        if not os.geteuid()==0:
            sys.exit('This script must be run as root!')
        print("Root user: OK")
        os.system("git clone git@github.com:Epitech/dump.git")
        #os.system("sudo apt-get install gcc-8")
    if __name__ == '__main__':
        main()
#def __init__(self):
#    self.name = "gitclonepull"
