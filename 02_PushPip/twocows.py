from cowsay import cowsay
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('-e', default='oo')
parser.add_argument('-f', default='default')
parser.add_argument('-E', default='oo')
parser.add_argument('-F', default='default')
parser.add_argument('-N', default='  ',)
parser.add_argument('first_msg')
parser.add_argument('second_msg')

args = parser.parse_args()

first_cow = cowsay(message=args.first_msg, cow=args.f, eyes=args.e).split('\n')
second_cow = cowsay(message=args.second_msg, cow=args.F, eyes=args.E, tongue=args.N).split('\n')

first_cow_size = len(first_cow)
second_cow_size = len(second_cow)
first_cow_width = max(len(line) for line in first_cow)
second_cow_width = max(len(line) for line in second_cow)
max_size = max(first_cow_size, second_cow_size)

second_cow = [" " * second_cow_width for _ in range(max_size - second_cow_size)] + second_cow
first_cow = [" " * first_cow_width for _ in range(max_size - first_cow_size)] + first_cow

for i in range(len(first_cow)):
    line1 = first_cow[i] + " " * (first_cow_width - len(first_cow[i]))
    line2 = second_cow[i]
    print(f"{line1} {line2}")
