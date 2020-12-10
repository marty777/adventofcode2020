#adventofcode2020.py

import sys
import os.path

from src.day1 import day1
from src.day2 import day2
from src.day3 import day3
from src.day4 import day4
from src.day5 import day5
from src.day6 import day6
from src.day7 import day7
from src.day8 import day8
from src.day9 import day9
from src.day10 import day10

def usage(maxday):
    print("Usage:")
    print("\tpython adventofcode2020.py [DAY] [INPUT FILE] ...\n")
    print("\t[DAY]\t\tThe advent program day to run (between 1 and %d)" % maxday)
    print("\t[INPUT FILE]\tThe relative or absolute path to the input file.")
    print("\nExample:")
    print("\tpython adventofcode2020.py 1 data/day1/input.txt")
    
def main():
    days = {
        1:day1,
        2:day2,
        3:day3,
        4:day4,
        5:day5,
        6:day6,
        7:day7,
        8:day8,
        9:day9,
        10:day10,
    }
    # parse the day and input data file from command line args
    if len(sys.argv) < 3:
        usage(len(days))
        return
    day = 0;
    try:
        day = int(sys.argv[1])
    except ValueError:
        usage(len(days))
        return
    if(day < 1 or day > len(days)):
        usage(len(days))
        return
    if(not os.path.isfile(sys.argv[2])):
        usage(len(days))
        return
    inpath = sys.argv[2]
    days[day](inpath)
    
main()
