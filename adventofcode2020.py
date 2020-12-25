#adventofcode2020.py

import sys
import os.path
from datetime import datetime

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
from src.day11 import day11
from src.day12 import day12
from src.day13 import day13
from src.day14 import day14
from src.day15 import day15
from src.day16 import day16
from src.day17 import day17
from src.day18 import day18
from src.day19 import day19
from src.day20 import day20
from src.day21 import day21
from src.day22 import day22
from src.day23 import day23
from src.day24 import day24
from src.day25 import day25

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
        11:day11,
        12:day12,
        13:day13,
        14:day14,
        15:day15,
        16:day16,
        17:day17,
        18:day18,
        19:day19,
        20:day20,
        21:day21,
        22:day22,
        23:day23,
        24:day24,
        25:day25,
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
    print("## DAY %d ##" % day)
    inpath = sys.argv[2]
    start = datetime.now()
    days[day](inpath)
    end = datetime.now()
    diff = end - start
    print("Completed in %d ms" % ((diff.microseconds/1000) + (1000 * diff.seconds)))
    
main()
