import argparse

parser = argparse.ArgumentParser()
parser.add_argument('num1', type=float)
parser.add_argument('num2', type=float)

args = parser.parse_args()

print(args.num1 + args.num2)