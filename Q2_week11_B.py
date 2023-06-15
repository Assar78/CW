import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str)

args = parser.parse_args()

for item in os.listdir(args.path):
    print(item)