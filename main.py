"""
Created on Wed Sep 12 2018

@author: Fabien Tarrade fabien.tarrade@axa.ch
"""

import sys
import getopt
import src.programs as programs


def main(argv):

    # Read command line arguments
    program = None
    mode = None

    helpstring = 'run.sh --program <p> --mode <m>'

    try:
        options, remainder = getopt.getopt(argv, "", [
            'program=',
            'mode=',
            'help'
        ])
    except getopt.GetoptError as e:
        print(dict(e))
        print('Please provide the following arguments')
        print(helpstring)
        sys.exit(2)

    for opt, arg in options:
        if opt == '--help':
            print(helpstring)
            sys.exit()
        elif opt == '--program':
            try:
                assert arg in ["extract_data", "preprocess", "train", "predict", "test"]
            except AssertionError:
                print('program can only be "extract_data" or "preprocess" or "train" or "predict" or "test"')
                print(helpstring)
                sys.exit(2)
            program = arg
        elif opt == '--mode':
            try:
                assert arg in ["dev", "prod", "test"]
            except AssertionError:
                print('mode can only be "dev" or "prod" or "test')
                print(helpstring)
                sys.exit(2)
            mode = arg

    if any([arg is None for arg in [program, mode]]):
        print("program", program)
        print("mode", mode)
        print("All command-line arguments are required")
        print(helpstring)
        sys.exit(2)
    else:
        # Executing the function we pass as an argument
        getattr(programs, program)(program=program, mode=mode)


if __name__ == "__main__":
    main(sys.argv[1:])
