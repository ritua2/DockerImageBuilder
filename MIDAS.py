"""
BASICS

Main MIDAS standalone program
"""


import argparse
import color_print
import os
import parser as MIDAS_parser
import sys



parser = argparse.ArgumentParser()





# Processes boolean inputs
# Based on https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'y', "Y", '1'):
        return True
    elif v.lower() in ('no', 'n', "N", '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


parser.add_argument("--ignore-warnings", type=str2bool, nargs='?', const=True, default=False, help="Ignore all warnings, 'yes'/'y'/'Y'/'1' for True")
parser.add_argument("--ignore-cmd-warnings", type=str2bool, nargs='?', const=True, default=False, help="Ignore CMD warnings, 'yes'/'y'/'Y'/'1' for True")
parser.add_argument("--ignore-copy-warnings", type=str2bool, nargs='?', const=True, default=False, help="Ignore COPY warnings, 'yes'/'y'/'Y'/'1' for True")
parser.add_argument("--ignore-run-warnings", type=str2bool, nargs='?', const=True, default=False, help="Ignore RUN warnings, 'yes'/'y'/'Y'/'1' for True")
parser.add_argument("--strict", type=str2bool, nargs='?', const=True, default=False, help="Treat warnings as errors, stop program when one occurs, 'yes'/'y'/'Y'/'1' for True")

parser.add_argument("-f", "--file", type=str, nargs='?', const=True, default="midas.yml", help="Input file")
parser.add_argument("-o", "--output", type=str, nargs='?', const=True, default="Dockerfile", help="Output Dockerfile path")


args = parser.parse_args()


if not os.path.exists(args.file):
    print("ERROR: File "+args.file+" does not exist.")


provided_data = MIDAS_parser.parse_commands(args.file)

if MIDAS_parser.base_check(provided_data)[1]:
    print("Necessary argument 'Base' is missing from input file")
    sys.exit()



docker_instructions = MIDAS_parser.order_inputs(provided_data)

if docker_instructions[1]:
    print(docker_instructions[0])
    sys.exit()


docker_instructions = docker_instructions[0]


# Processes warnings
warnings_to_check = {"CMD": not args.ignore_cmd_warnings,
                    "COPY": not args.ignore_copy_warnings,
                    "RUN": not args.ignore_run_warnings
                    }


docker_translator = {
    "Contents":"COPY",
    "Setup":"RUN",
    "Default command":"CMD"
}

midas_translator = {v: k for k, v in docker_translator.items()}
instruction_types = []




if not args.ignore_warnings:
    for instruction in docker_instructions:
        instruction_types.append(instruction[2])
    else:
        if "Default command" in provided_data:
            instruction_types.append("Default command")

    provided_docker_instruction_types = [ docker_translator[b] for b in list(set(instruction_types)) if b in docker_translator]
    types_to_check = [inst for inst in warnings_to_check if warnings_to_check[inst]==True]

    for checking_type in types_to_check:

        if checking_type not in provided_docker_instruction_types:
            color_print.color_print("Warning: No '"+midas_translator[checking_type]+"' provided, this corresponds to a docker '"+checking_type+"' instruction", "YELLOW")
            if args.strict:
                color_print.color_print("Error: No '"+midas_translator[checking_type]+"' provided, strict parsing", "RED")
                sys.exit()



# Writes result to file 
print(MIDAS_parser.create_dockerfile(args.file, args.output))
