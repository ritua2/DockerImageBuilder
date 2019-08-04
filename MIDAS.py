"""
BASICS

Main MIDAS standalone program
"""


import argparse
import os
import parser as MIDAS_parser
import sys



parser = argparse.ArgumentParser()


# Processes boolean inputs
# Based on https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', "Y", '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', "N", '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


parser.add_argument("--ignore-warnings", type=str2bool, nargs='?', const=True, default=False, help="Do not show any warnings")
parser.add_argument("--ignore-cmd-warnings", type=str2bool, nargs='?', const=True, default=False, help="Do not show CMD warnings")
parser.add_argument("--ignore-copy-warnings", type=str2bool, nargs='?', const=True, default=False, help="Do not show COPY warnings")
parser.add_argument("--ignore-run-warnings", type=str2bool, nargs='?', const=True, default=False, help="Do not show RUN warnings")
parser.add_argument("--strict", type=str2bool, nargs='?', const=True, default=False, help="Treat warnings as errors, stop program when one occurs")

parser.add_argument("-f", "--file", type=str, nargs='?', const=True, default="midas.yml", help="Input file")
parser.add_argument("-o", "--output", type=str, nargs='?', const=True, default="Dockerfile", help="Output Dockerfile path")


args = parser.parse_args()


if not os.path.exists(args.file):
    print("ERROR: File "+args.file+" does not exist.")


provided_data = MIDAS_parser.parse_commands(args.file)

if MIDAS_parser.base_check(provided_data)[1]:
    print("Necessary argument 'Base' is missing from input file")
    sys.exit()



# Processes warnings
# TODO


# Writes result to file 
print(MIDAS_parser.create_dockerfile(args.file, args.output))
