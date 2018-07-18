import os
import subprocess as sp
from termcolor import colored as tcc
import numpy as np

# TODO remove
def dev_rm():
    if 'flu' in os.listdir(os.getcwd()):
        sp.call(['rm', '-r', 'flu/'])



def transmit(name):
    sp.call(['mkdir', name])
    path = os.getcwd()
    path = path + '/' + name
    os.chdir(path)
    print(tcc('transmitting virus', 'yellow'))

def mRNA():
   viral_mRNA = str(np.random.randint(1, 9999999) * 999)
   return viral_mRNA

def replicate():
    sp.call(['cp', 'virion.py', '..'])
    os.chdir('..')
    print(tcc('replicated virus and hopped', 'red'))

if __name__ == "__main__":
    # TODO remove
    dev_rm()

    ## ~ VIRUS ~ ##
    # transmit('flu')

    # mRNA()

    # replicate()

    mRNA()

#     replicate()

    print('current dir:')
    print(os.getcwd())




