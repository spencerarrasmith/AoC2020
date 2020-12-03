import sys, os
from datetime import datetime
import requests
import subprocess

def run():
    sys.path.append("..")

    os.chdir('..')

    now=datetime.now()
    offset = 0
    if int(now.strftime("%H")) > 20:
        offset = 1
    foldername = str(int(now.strftime("%Y%m%d")) + offset)
    day = int(foldername) - 20201200
    os.mkdir(foldername)

    os.chdir(foldername)

    template =\
    """
# --- Day %d: ####### ---
#
#   Part 1:
#   Part 2:
#

import sys
sys.path.append("..")

from AoCCommon.InputToArray import InputToArray

a = InputToArray()

mydata = a.array
    """ % day

    f = open('aoc_'+foldername+'.py', 'w')
    f.write(template)
    f.close()

    openinputcommand = '"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --app=https://adventofcode.com/2020/day/' + str(day) + '/input'
    subprocess.call(openinputcommand)

    #url = 'https://adventofcode.com/2020/day/2/input'
    #r = requests.get(url).text
    #print(r)

if __name__ == "__main__":
    run()