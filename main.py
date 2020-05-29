import argparse
# from problems.p1 import *
from problems import *

def main(problem_number, show_working):

    if problem_number == '1':
        p1()
    
    
if __name__ == '__main__':
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    parser = argparse.ArgumentParser()
    parser.add_argument('problem_number', default = 1)
    parser.add_argument('show_working', default = 1)
    args = parser.parse_args()

    main(args.problem_number, args.show_working)


