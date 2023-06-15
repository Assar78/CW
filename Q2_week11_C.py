import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("path_inp")
parser.add_argument("--size", action="store_true")
args = parser.parse_args()
dirs = os.listdir(args.path)


if args.size is True:
    for dir in dirs:
        size = os.path.getsize(dir)
        print(dir,": ",size)

else:
    for dir in dirs:
        print(dir)