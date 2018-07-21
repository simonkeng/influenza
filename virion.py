import os
import subprocess as sp
from termcolor import colored as tcc
import numpy as np


mRNA = 'import subprocess; subprocess.call(["open", "-n", "-a", "google chrome"]);'
rRNA = 'subprocess.call(["cp", "bug.py", "nest/"]);'

virus = 'bug.py'


def clone():
    sp.call(['mkdir', 'nest'])
    os.chdir('nest')


if __name__ == "__main__":

    ## ~ VIRUS ~ ##
    for i in range(5):

        with open(virus, 'w') as f:
            f.write(mRNA)
            f.write(rRNA)

        clone()
        sp.call(['python', virus])

