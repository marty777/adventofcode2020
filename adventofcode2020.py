#adventofcode2020.py

import sys
import os.path

from src.day1 import day1
from src.day2 import day2
from src.day3 import day3
from src.day4 import day4

MAXDAY = 4

def usage():
    print("Usage:")
    print("\tpython adventofcode2020.py [DAY] [INPUT FILE] ...\n")
    print("\t[DAY]\t\tThe advent program day to run (between 1 and %d)" % MAXDAY)
    print("\t[INPUT FILE]\tThe relative or absolute path to the input file.")
    print("\nExample:")
    print("\tpython adventofcode2020.py 1 data/day1/input.txt")
    

def main():
    # parse the day and input data file from command line args
    if len(sys.argv) < 3:
        usage()
        return
    day = 0;
    try:
        day = int(sys.argv[1])
    except ValueError:
        usage()
        return
    if(day < 1 or day > MAXDAY):
        usage()
        return
    if(not os.path.isfile(sys.argv[2])):
        usage()
        return
    inpath = sys.argv[2]
    days = {
        1:day1,
        2:day2,
        3:day3,
        4:day4,
    }
    days[day](inpath)
    
main()
