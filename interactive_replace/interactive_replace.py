"""
WARNING: THIS DOESN'T WORK. 
@vineeshvs: Work on this later
Do find and replace of strings on files with certain extensions interactively.

PREQREQUISITES:
* Vim 
* Python 2.7

TESTED ON:
None
"""

#TODO
"""
* 
"""

# FUTURE IMPROVEMENTS
"""
* 
"""
import sys
import os
import re
import time
from shutil import copyfile
from functions import *

DBG = 1
file_list = 'file_list.txt'
logFile = 'log.txt'

#-----------------------------------------------------------------------
# Make your changes here
#-----------------------------------------------------------------------
# Original string we are looking for.
find = 'hi'
# String which will replace the original string
replace = 'omg'
# 0: Do the find and replace without taking confirmation for each replace.
# 1: Ask for confirmation every time.
interactive = 1
# Specify extension of the files on which you want to do the replacement
file_extension = '*.v'
#-----------------------------------------------------------------------

def main(argv):
    print "Get the list of all file in which replacements have to be made."
    c = 'ls ' + file_extension + ' >' + file_list
    if(DBG): print c+'\n'
    bashComm(c,logFile,DBG)
    
    if interactive:
        with open(file_list, "r") as f1:
            for line1 in f1:
                #c1 = 'vim -c '+'\'%s/'+find+'/'+replace+'/gc\' -c \'wq\' ' + line1.split()[0]
                c1 = 'vim -c '+'\'%s/'+find+'/'+replace+'/gc\' ' + line1.split()[0]
                if(DBG): print c1+'\n'
                #exit("Exit")
                bashComm(c1,logFile,DBG)

    raw_input("Press enter to exit ;)")

if __name__ == '__main__':
    main(sys.argv)
