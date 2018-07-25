import os
import subprocess as sp
from termcolor import colored as tcc
import numpy as np



def transmit_virion():
    '''
    No input, just recursively searches the current dir tree and
    builds a list of dirs it finds.
    '''
    files_to_infect = list()
    for root, dirs, fils in os.walk(os.getcwd()):
        for di in dirs:
            files_to_infect.append(os.path.join(root, di))

    # Should be its own function (TODO)
    for fil in files_to_infect:
        os.chdir(fil)
        sp.call(['touch', 'plague.virus'])
        # this is wild, this worked, very very scary well...
        # it was very hard to clean up after this.
        # but the antidote is:
        # find . -type f -name '*plague.virus*' -delete



if __name__ == "__main__":

    ## ~ VIRUS ~ ##
    transmit_virion()
